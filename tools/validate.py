#!/usr/bin/env python3
"""Standard-library checks for this public reference, not infrastructure tests."""
from pathlib import Path
import copy
from datetime import date
import ipaddress
import json
import re
import subprocess
import sys
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ROLES = {"apps-vm", "edge-vm", "agent-vm", "media-vm", "photos-vm"}
STATUSES = {"source-configured", "source-gated", "source-disabled", "source-pattern", "reference-pattern"}
RUNTIME = {"unit-active", "unit-inactive", "scheduled-job-observed", "not-assessed"}
REQUIRED = {
    "README.md", "AGENTS.md", "llms.txt", "fleet.json", "LICENSE", "SECURITY.md",
    "CONTRIBUTING.md", "docs/architecture.md", "docs/services.md",
    "docs/single-server.md", "docs/agent-runtime.md", "docs/repository-context.md",
    "docs/operations.md", "docs/adoption.md", "docs/provenance.md",
    "docs/references.md", "docs/current-state.md", "docs/pitfalls.md", "templates/README.md", "templates/AGENTS.md",
    "templates/handoff.md", "templates/decision.md", "templates/acceptance.md",
    ".github/workflows/validate.yml", "tools/validate.py", ".gitignore",
}


def files():
    if (ROOT / ".git").exists():
        names = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
        return [ROOT / n for n in names if n]
    return [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]


def validate_model(model):
    assert model["schema_version"] == 2
    assert model["kind"] == "sanitized-current-fleet-snapshot"
    assessment = model["assessment"]
    assert assessment["deployable"] is False
    assert assessment["live_status"] == "partially-assessed"
    reviewed = date.fromisoformat(assessment["review_date"])
    observed = date.fromisoformat(assessment["runtime_observation_date"])
    assert observed <= reviewed
    assert model["substrate"]["source_design"] == "Proxmox VE"
    assert model["substrate"]["guest_os"] == "NixOS"
    assert model["substrate"]["single_server_failure_domain"] is True
    roles = [r["id"] for r in model["roles"]]
    assert len(roles) == len(set(roles)) and set(roles) == ROLES
    assert {r["id"] for r in model["roles"] if r["core_for_adaptation"]} == {"apps-vm", "edge-vm", "agent-vm"}
    for role in model["roles"]:
        assert role["current_fleet_member"] is True
        assert isinstance(role["core_for_adaptation"], bool)
        assert role["guest_os"] == "NixOS"
        assert role["runtime_status"] == ("not-assessed" if role["id"] == "edge-vm" else "guest-observed")
    assert set(model["evidence_statuses"]) == STATUSES
    assert set(model["runtime_statuses"]) == RUNTIME
    ids = []
    fields = {"id", "name", "role", "software", "evidence_status", "notes", "live_status",
              "observed_on", "observation_method", "runtime_note", "acceptance_status"}
    for service in model["services"]:
        assert set(service) == fields
        assert all(isinstance(value, str) and value for key, value in service.items()
                   if key not in {"observed_on", "observation_method"})
        assert re.fullmatch(r"[a-z][a-z0-9-]*", service["id"])
        assert service["role"] in ROLES
        assert service["evidence_status"] in STATUSES - {"reference-pattern"}
        assert service["live_status"] in RUNTIME
        assert service["acceptance_status"] == "not-assessed"
        if service["live_status"] == "not-assessed":
            assert service["observed_on"] is None and service["observation_method"] is None
        else:
            assert service["observed_on"] == observed.isoformat()
            assert isinstance(service["observation_method"], str) and service["observation_method"]
            assert service["role"] != "edge-vm"
        ids.append(service["id"])
    assert ids and len(ids) == len(set(ids))
    recommendations = model["recommendations"]
    assert recommendations
    for item in recommendations:
        assert item["evidence_status"] == "reference-pattern"
        assert item["live_status"] == "not-assessed"
        assert item["role"] in ROLES
        assert re.fullmatch(r"[a-z][a-z0-9-]*", item["id"])
        ids.append(item["id"])
    assert len(ids) == len(set(ids))
    assert model["adjacent_systems"] == [{
        "id": "home-automation", "software": "Home Assistant OS",
        "relationship": "Separate appliance integrated through agent API tooling, outside five NixOS guest roles",
        "live_status": "not-assessed",
    }]
    assert len(model["invariants"]) >= 5


class ReferenceChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = json.loads((ROOT / "fleet.json").read_text())
        cls.paths = files()

    def test_required_files_and_explicit_allowlist(self):
        actual = {p.relative_to(ROOT).as_posix() for p in self.paths}
        self.assertEqual(actual, REQUIRED)

    def test_machine_contract(self):
        validate_model(self.model)

    def test_duplicate_service_rejected(self):
        bad = copy.deepcopy(self.model)
        bad["services"].append(copy.deepcopy(bad["services"][0]))
        with self.assertRaises(AssertionError):
            validate_model(bad)

    def test_unknown_role_rejected(self):
        bad = copy.deepcopy(self.model)
        bad["services"][0]["role"] = "unknown-role"
        with self.assertRaises(AssertionError):
            validate_model(bad)

    def test_unverified_health_claim_rejected(self):
        bad = copy.deepcopy(self.model)
        bad["services"][0]["live_status"] = "healthy"
        with self.assertRaises(AssertionError):
            validate_model(bad)

    def test_fabricated_evidence_label_rejected(self):
        bad = copy.deepcopy(self.model)
        bad["services"][0]["evidence_status"] = "proven-live"
        with self.assertRaises(AssertionError):
            validate_model(bad)

    def test_deployable_claim_rejected(self):
        bad = copy.deepcopy(self.model)
        bad["assessment"]["deployable"] = True
        with self.assertRaises(AssertionError):
            validate_model(bad)

    def test_catalog_matches_model(self):
        text = (ROOT / "docs/services.md").read_text()
        rows = [line.split("|")[1:-1] for line in text.splitlines() if line.startswith("| ")]
        actual = {row[0].strip(): row for row in rows if row[0].strip() not in {"ID", "---"}}
        expected = {s["id"] for s in self.model["services"]}
        self.assertEqual(set(actual), expected)
        for service in self.model["services"]:
            row = actual[service["id"]]
            self.assertEqual(row[1].strip(), service["role"])
            self.assertEqual(row[3].strip(), service["evidence_status"])
            self.assertIn(service["software"], row[2])
            self.assertEqual(row[4].strip(), service["live_status"])
            self.assertEqual(row[5].strip(), service["notes"])
            self.assertIn("- **" + service["id"] + "**: " + service["runtime_note"], text)

    def assert_bad_mutation(self, mutate):
        bad = copy.deepcopy(self.model)
        mutate(bad)
        with self.assertRaises((AssertionError, ValueError)):
            validate_model(bad)

    def test_missing_observation_date_rejected(self):
        self.assert_bad_mutation(lambda m: m["services"][0].update(observed_on=None))

    def test_missing_observation_method_rejected(self):
        self.assert_bad_mutation(lambda m: m["services"][0].update(observation_method=""))

    def test_unsupported_acceptance_rejected(self):
        self.assert_bad_mutation(lambda m: m["services"][0].update(acceptance_status="passed"))

    def test_edge_runtime_claim_rejected(self):
        def mutate(m):
            item = next(s for s in m["services"] if s["role"] == "edge-vm")
            item.update(live_status="unit-active", observed_on=m["assessment"]["runtime_observation_date"], observation_method="claimed")
        self.assert_bad_mutation(mutate)

    def test_recommendation_in_current_inventory_rejected(self):
        self.assert_bad_mutation(lambda m: m["services"][0].update(evidence_status="reference-pattern"))

    def test_duplicate_recommendation_rejected(self):
        self.assert_bad_mutation(lambda m: m["recommendations"].append(copy.deepcopy(m["recommendations"][0])))

    def test_current_role_cannot_be_marked_absent(self):
        self.assert_bad_mutation(lambda m: m["roles"][-1].update(current_fleet_member=False))

    def test_human_entry_snapshot_consistency(self):
        stamp = self.model["assessment"]["review_date"]
        for name in ["README.md", "AGENTS.md", "llms.txt", "docs/current-state.md", "docs/services.md", "docs/provenance.md", "docs/pitfalls.md"]:
            self.assertIn(stamp, (ROOT / name).read_text(), name)
        text = (ROOT / "AGENTS.md").read_text()
        for status in RUNTIME:
            self.assertIn(status, text)
        self.assertNotIn('Every service has `live_status: "not-assessed"`', text)
        for name in ["README.md", "AGENTS.md", "llms.txt"]:
            text = (ROOT / name).read_text()
            self.assertIn("docs/current-state.md", text)
            self.assertIn("docs/pitfalls.md", text)

    def test_snapshot_boundaries(self):
        services = {s["id"]: s for s in self.model["services"]}
        self.assertEqual(services["documents"]["live_status"], "unit-inactive")
        for sid in ["personal-hub", "mail-actions", "network-tools", "media", "photos"]:
            self.assertEqual(services[sid]["live_status"], "unit-active")
        for sid in ["location", "asset-inventory"]:
            self.assertEqual(services[sid]["evidence_status"], "source-disabled")
        for sid in ["edge-social", "budget-agent", "aux-workbench"]:
            self.assertEqual(services[sid]["evidence_status"], "source-gated")
        self.assertNotIn("edge-rss", services)
        self.assertNotIn("voice", services)
        catalog = (ROOT / "docs/services.md").read_text()
        for item in self.model["recommendations"]:
            self.assertIn("**" + item["id"] + " — " + item["name"] + "**: " + item["notes"], catalog)

    def test_pitfalls_have_complete_lesson_structure(self):
        text = (ROOT / "docs/pitfalls.md").read_text()
        lessons = re.split(r"(?m)^## [0-9]+\. ", text)[1:]
        self.assertEqual(len(lessons), 12)
        for lesson in lessons:
            for label in ["**Symptoms:**", "**Cause:**", "**Fix:**", "**Verify:**"]:
                self.assertIn(label, lesson)
        self.assertIn("supersed", (ROOT / "docs/provenance.md").read_text())

    def test_local_links(self):
        links = 0
        for path in self.paths:
            if path.suffix != ".md" and path.name != "llms.txt":
                continue
            for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", path.read_text()):
                parsed = urlsplit(target)
                if parsed.scheme or target.startswith("#"):
                    continue
                dest = (path.parent / unquote(parsed.path)).resolve()
                self.assertTrue(dest.is_relative_to(ROOT), (path, target))
                self.assertTrue(dest.is_file(), (path, target))
                links += 1
        self.assertGreater(links, 20)

    def test_no_private_address_or_runtime_material(self):
        for path in self.paths:
            self.assertFalse(path.is_symlink(), path)
            text = path.read_text()
            rel = path.relative_to(ROOT).as_posix()
            self.assertNotRegex(rel, r"(?i)(?:^|/)(?:secrets|profiles|sessions|logs)/|\.(?:pem|key|db|sqlite)$")
            self.assertNotIn("BEGIN " + "PRIVATE KEY", text)
            self.assertNotIn("BEGIN OPENSSH " + "PRIVATE KEY", text)
            self.assertNotRegex(text, r"gh[pousr]_[A-Za-z0-9]{20,}")
            self.assertNotRegex(text, r"AGE-SECRET-KEY-[A-Z0-9]+")
            self.assertNotRegex(text, r"[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.ts\.net")
            self.assertNotRegex(text, r"/home/[A-Za-z0-9_-]+/|/var/lib/hermes-[A-Za-z0-9_-]+/")
            self.assertNotRegex(text, r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}")
            for address in re.findall(r"(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])", text):
                ip = ipaddress.ip_address(address)
                self.assertTrue(ip.is_loopback, (rel, address))

    def test_ci_has_read_only_permissions_and_pinned_action(self):
        text = (ROOT / ".github/workflows/validate.yml").read_text()
        self.assertIn("contents: read", text)
        self.assertNotIn("pull_request_target", text)
        self.assertNotIn("self-hosted", text)
        self.assertNotRegex(text, r"(?m)^\s+\w[^:]*: write$")
        for action in re.findall(r"uses: ([^\n]+)", text):
            self.assertRegex(action, r"^[\w.-]+/[\w.-]+@[0-9a-f]{40}$")

    def test_human_overview_has_all_roles(self):
        text = (ROOT / "README.md").read_text()
        for role in ROLES:
            self.assertIn(role, text)
        self.assertIn("Proxmox", text)
        self.assertIn("no ready-to-deploy Nix flake", text)


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ReferenceChecks)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        model = json.loads((ROOT / "fleet.json").read_text())
        print(f"Validated {len(files())} allowlisted files, {len(model['roles'])} roles, {len(model['services'])} catalog entries; no live infrastructure tested.")
    sys.exit(not result.wasSuccessful())

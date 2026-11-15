#!/usr/bin/env python3
"""Standard-library checks for this public reference, not infrastructure tests."""
from pathlib import Path
import copy
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
REQUIRED = {
    "README.md", "AGENTS.md", "llms.txt", "fleet.json", "LICENSE", "SECURITY.md",
    "CONTRIBUTING.md", "docs/architecture.md", "docs/services.md",
    "docs/single-server.md", "docs/agent-runtime.md", "docs/repository-context.md",
    "docs/operations.md", "docs/adoption.md", "docs/provenance.md",
    "docs/references.md", "templates/README.md", "templates/AGENTS.md",
    "templates/handoff.md", "templates/decision.md", "templates/acceptance.md",
    ".github/workflows/validate.yml", "tools/validate.py", ".gitignore",
}


def files():
    if (ROOT / ".git").exists():
        names = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
        return [ROOT / n for n in names if n]
    return [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]


def validate_model(model):
    assert model["schema_version"] == 1
    assert model["kind"] == "sanitized-architecture-reference"
    assert model["assessment"]["deployable"] is False
    assert model["assessment"]["live_status"] == "not-assessed"
    assert model["substrate"]["source_design"] == "Proxmox VE"
    assert model["substrate"]["guest_os"] == "NixOS"
    assert model["substrate"]["single_server_failure_domain"] is True
    roles = [r["id"] for r in model["roles"]]
    assert len(roles) == len(set(roles)) and set(roles) == ROLES
    assert {r["id"] for r in model["roles"] if r["required"]} == {"apps-vm", "edge-vm", "agent-vm"}
    assert set(model["evidence_statuses"]) == STATUSES
    ids = []
    for service in model["services"]:
        assert set(service) == {"id", "name", "role", "software", "evidence_status", "notes", "live_status"}
        assert all(isinstance(x, str) and x for x in service.values())
        assert re.fullmatch(r"[a-z][a-z0-9-]*", service["id"])
        assert service["role"] in ROLES
        assert service["evidence_status"] in STATUSES
        assert service["live_status"] == "not-assessed"
        ids.append(service["id"])
    assert ids and len(ids) == len(set(ids))
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
            self.assertEqual(row[4].strip(), service["notes"])

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

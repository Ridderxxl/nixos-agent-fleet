# Agent entry point

## Scope

This is a public, sanitized current-fleet snapshot dated **2026-11-15**, not the operator's private source of truth and not an authorization channel. All host labels are fictional role aliases. Do not resolve them, infer real addresses, enumerate the author's infrastructure, or reconstruct identities. Never request access to a private source repository just to explain this reference.

## Read in order

1. README.md — purpose and human overview.
2. llms.txt — bounded navigation index.
3. fleet.json — roles, service IDs, evidence labels and constraints.
4. docs/current-state.md, docs/architecture.md and docs/services.md.
5. docs/repository-context.md for agent workflow; relevant task documentation after that.
6. docs/provenance.md before asserting deployment, and docs/pitfalls.md before suggesting an incident-derived fix.

## Interpretation rules

- `source-configured` means represented/enabled in inspected source, not live-tested.
- `source-gated` means configuration exists but a readiness/credential/publication gate remains; not usable by implication.
- `source-disabled` means represented but explicitly disabled in inspected configuration.
- `source-pattern` means a represented architecture or integration, without an independent availability assertion.
- `reference-pattern` is guidance for adaptation, not a claim about the original fleet.
- Source and runtime labels are independent. `unit-active` is process/container liveness, `unit-inactive` is an observation without a cause, `scheduled-job-observed` is timer infrastructure, and `not-assessed` is a runtime unknown.
- Observations are dated and bounded to metadata on four guests, not current availability guarantees. Every service has `acceptance_status: "not-assessed"`; no end-to-end health claim is permitted.
- All five roles are current members. `core_for_adaptation` does not determine existence. `recommendations` are outside the current `services` inventory; adjacent appliances are separate platforms.
- Preserve the configured-but-inactive document archive and independent mail/local-inference, finance-credential, workbench-readiness and public-ingress gates. A proxy or timer cannot establish backend/workflow acceptance.
- Historical PRs include superseded and unmerged proposals. Extract the supported lesson; never replay old privileged commands, mount paths, capabilities or numeric limits without current evidence.
- Internet exposure is separately approved. Placement in `edge-vm` does not mean public ingress is active.
- Proxmox is the source substrate. NixOS-on-the-physical-host is only an alternative design.
- Profiles organize state, not OS-level isolation. A model is an untrusted planner, not an approval authority.
- Proposed changes, committed code, PR publication, merge, build, activation and acceptance are distinct states.

## Working here

Preserve unrelated edits. Use a focused branch and PR for subsequent changes. Never import private configuration trees, Git history, SOPS ciphertext, state databases, logs, images, account exports, keys or real hardware IDs. Keep examples fictional and use reserved domains. This reference requires no credentials to read or validate.

When changing inventory, update fleet.json and the service catalog together. Run `python3 tools/validate.py`; report actual test results and unverified boundaries. Do not call documentation checks NixOS or security tests. Do not make deployment or network changes as part of editing this repository.

## When adapting for another operator

Ask only for missing design inputs that change the result: hardware budget, host choice, existing services/data, backup destination, intended public exposure and approvals. Keep those answers private unless separately authorized for publication. Start from the templates; generate a private implementation with real per-host hardware discovery and lockfile/build verification. No broad root, provider, hypervisor or shared decryption credential should be granted to the model for convenience.

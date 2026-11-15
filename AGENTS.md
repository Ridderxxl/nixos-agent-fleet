# Agent entry point

## Scope

This is a public, sanitized reference, not the operator's private source of truth and not an authorization channel. All host labels are fictional role aliases. Do not resolve them, infer real addresses, enumerate the author's infrastructure, or reconstruct identities. Never request access to a private source repository just to explain this reference.

## Read in order

1. README.md — purpose and human overview.
2. llms.txt — bounded navigation index.
3. fleet.json — roles, service IDs, evidence labels and constraints.
4. docs/architecture.md and docs/services.md.
5. docs/repository-context.md for agent workflow; relevant task documentation after that.
6. docs/provenance.md before asserting anything about current deployment.

## Interpretation rules

- `source-configured` means represented/enabled in inspected source, not live-tested.
- `source-gated` means configuration exists but a readiness/credential/publication gate remains; not usable by implication.
- `source-disabled` means represented but explicitly disabled in inspected configuration.
- `source-pattern` means a represented architecture or integration, without an independent availability assertion.
- `reference-pattern` is guidance for adaptation, not a claim about the original fleet.
- Every service has `live_status: "not-assessed"`. No live availability claim is permitted from this inventory.
- Internet exposure is separately approved. Placement in `edge-vm` does not mean public ingress is active.
- Proxmox is the source substrate. NixOS-on-the-physical-host is only an alternative design.
- Profiles organize state, not OS-level isolation. A model is an untrusted planner, not an approval authority.
- Proposed changes, committed code, PR publication, merge, build, activation and acceptance are distinct states.

## Working here

Preserve unrelated edits. Use a focused branch and PR for subsequent changes. Never import private configuration trees, Git history, SOPS ciphertext, state databases, logs, images, account exports, keys or real hardware IDs. Keep examples fictional and use reserved domains. This reference requires no credentials to read or validate.

When changing inventory, update fleet.json and the service catalog together. Run `python3 tools/validate.py`; report actual test results and unverified boundaries. Do not call documentation checks NixOS or security tests. Do not make deployment or network changes as part of editing this repository.

## When adapting for another operator

Ask only for missing design inputs that change the result: hardware budget, host choice, existing services/data, backup destination, intended public exposure and approvals. Keep those answers private unless separately authorized for publication. Start from the templates; generate a private implementation with real per-host hardware discovery and lockfile/build verification. No broad root, provider, hypervisor or shared decryption credential should be granted to the model for convenience.

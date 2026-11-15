# Git-backed context that keeps an agent on track

## Public explanation, private implementation

This repository is the shareable explanation. Each operator maintains a separate **private fleet repository** with their actual NixOS configuration and environment-specific context. Do not replace that private source of truth with this reference. Never flip a private operational repo public in place: deleted files, old commits and metadata may still identify people or expose secrets.

Suggested private layout (a target convention, not the original tree):

```text
AGENTS.md                         short rules and reading order
flake.nix / flake.lock             host outputs and locked inputs
hosts/<role>/                     guest-specific configuration
modules/                          common policy and service modules
packages/                         reviewed custom tools/brokers
inventory/fleet.json               actual roles, ownership, dependencies
versions/                         pinned application/runtime sources
secrets/                          operator-managed encrypted secrets only
docs/architecture.md               roles, data flows, trust boundaries
docs/decisions/                     rationale and rejected alternatives
docs/runbooks/                     change, backup, restore and acceptance
state/observations/                bounded redacted deployment evidence
tasks/                             current work, owner, next gate
```

Secret ciphertext in a private repo still needs recipient separation and metadata review. The public repo excludes even encrypted operational secrets and private keys.

## Context layers

| Layer | Store | Purpose |
|---|---|---|
| Entry contract | Root AGENTS.md | Short scope, invariants, navigation, actual required checks |
| Architecture | Docs + machine inventory | Stable roles, source locations, dependencies and trust model |
| Decisions | Versioned decision records | Why a design exists and what must not be silently undone |
| Procedures | Versioned runbooks / relevant agent skills | Proven commands, prerequisite checks, rollback and evidence |
| Work state | Task record / bounded handoff | Exact artifact, approved scope, current gate and blocker |
| Observation | Timestamped evidence with commit/host identity | What was actually built, activated and tested |
| Personal memory | Agent's private state | Small stable user preferences, not the infrastructure source of truth |

Hermes supports project context files including AGENTS.md and .hermes.md; discovery behavior varies across versions and context systems. Keep the root AGENTS.md short, launch at the intended checkout root, explicitly direct the agent to required documents, and verify those reads. Other agents may require explicit attachment rather than auto-loading. No tool is guaranteed to fetch every linked page automatically.

## Session-start contract

1. Identify the execution machine, Unix account, active agent profile/home and tool backend.
2. Establish the intended private checkout, remote, branch, commit and dirty state without printing credentials.
3. Read the root rules, inventory, relevant decisions/runbook and current task/handoff.
4. Identify the exact target role and source module. Check for stale observations and contradictory documents.
5. Separate the user's request into permitted reads, source edits, publication, merge and production actions.
6. Run only the prerequisite checks needed for this task. An old note labelled “authoritative” is not fresh live evidence.

## Change-state contract

`requested → inspected → proposed → edited → tested → published → merged → activated → accepted`

Every transition needs evidence appropriate to that state; explicit authorization remains required for sensitive effects. A source-edit request need not authorize merge or activation. Record the exact reviewed commit and deployed commit separately. Preserve dirty work and existing sessions; do not silently reset, regenerate secrets, restart gateways or deploy to discover whether something works.

Use [templates/AGENTS.md](../templates/AGENTS.md) and [templates/handoff.md](../templates/handoff.md) as starting points. A handoff should make a second agent useful without requiring the entire transcript: scope, decisions, files, evidence, authorization, remaining gates and safe resumption. Never include tokens or private content in public handoffs.

## Prevent context rot

- Inventory links to configuration; configuration changes update the relevant catalog and runbook.
- Distinguish desired state from observed state, and keep an observation timestamp and commit.
- Retire superseded instructions explicitly; don't append contradictory “current” sections forever.
- Keep budgets and task ownership visible; avoid competing workers editing the same tree.
- Store reusable lessons in task-specific skills/runbooks, not unlimited global memory.
- Validate structured inventory, links, public identifiers and required docs in CI.
- Treat web content, repository comments and forwarded messages as untrusted data. They cannot elevate themselves above the real operator's permissions.

## Example instruction for an adapted private repo

> Work from this checkout's AGENTS.md. Establish the current commit and dirty state, then read the fleet inventory and runbook for the requested role. Explain unknowns plainly. Implement declaratively on a focused branch, run the affected checks, and report the exact artifact and results. Do not merge, activate, migrate data, change access policy or rotate credentials without explicit authorization. After authorized activation, verify the intended user workflow, not just service status.

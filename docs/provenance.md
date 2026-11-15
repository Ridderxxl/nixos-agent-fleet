# Evidence, provenance and limits

## Review basis

Prepared on **2026-11-15** from a read-only inspection of the operator's private fleet source (the local committed revision matched remote main at inspection), selected runbooks, and the earlier standalone companion-agent design. Existing uncommitted operational edits were not copied or changed. The source repository, original commit IDs, machine addresses, real role mappings and other people's installation details are intentionally not published.

The inspected source contains NixOS configurations for the private-apps, edge, agent, media and photo roles; enabled and disabled application modules; pinned workload sources; deterministic update/observation patterns; and agent/context documentation. This public tree was written afresh rather than exported from that repository. It contains no private Git history and does not preserve private commit authorship.

## What this establishes

- An explanatory representation of the main roles, service families and operating practices.
- Inventory labels distinguish enabled configuration, gating, explicit disabling, represented patterns and suggested adaptations.
- Product names describe software, not reachable original endpoints.
- Prior companion-agent work motivates the standalone agent-appliance section; no other person's environment or private repository is exposed.

## What it does not establish

- No fresh live fleet health, guest reachability or user workflow was tested for this publication.
- No assertion that all service families are running, all integrations are connected, or security improvements have been fully rolled out.
- No claim that every source document was up to date. Some legacy snapshots describe old migration states; configuration was preferred for source-level enable/disable labels, never substituted for runtime evidence.
- No turnkey build, flake, hardware image, production controller, penetration test, disaster-recovery rehearsal or fully reproducible dependency closure is delivered here.
- No physical-host NixOS implementation: the reference substrate is Proxmox, with NixOS guests.
- No guarantee that upstream context discovery, plugin APIs, installation commands or provider support remain unchanged. Check the selected version's upstream documentation.

## Validation scope

`tools/validate.py` checks the public tree's documentation links, inventory contract, catalog consistency, aliases and publication-hygiene rules. Its negative self-tests ensure selected malformed inventory cases are rejected. Passing does not prove absence of every possible private identifier, runtime security, infrastructure correctness, or operational availability. Manual source-to-public review remains necessary.

The repository's own GitHub account association is public. Sanitizing names inside documents cannot make a repository owner anonymous. No private-to-public hostname crosswalk is included.

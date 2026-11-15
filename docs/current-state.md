# Current fleet snapshot — 2026-11-15

This is a dated account of an existing fleet with neutral aliases, not an aspirational template. The earlier companion-agent setup is background, not the scope ceiling. The [machine inventory](../fleet.json) and [service catalog](services.md) separate source declarations from bounded runtime observations and untested acceptance.

## Existing roles

| Alias | Current source role | Runtime evidence on 2026-11-15 |
|---|---|---|
| `apps-vm` | Private application hub: native services, declared OCI containers, per-service private ingress | NixOS guest observed; most principal app units active; Paperless application units inactive |
| `edge-vm` | External-service trust zone; authenticated social upload/review/publication application | Source only; application/private ingress and reviewed publishing enabled in source, public ingress disabled; operator-only management boundary respected |
| `agent-vm` | Hermes gateways, web/phone transports, retrieval, Personal Hub, mail review and bounded automation | NixOS guest observed; gateways/transports/Hub/broker units active; scheduled work observed |
| `media-vm` | Existing isolated media and automation workload | NixOS guest observed; all seven cataloged media containers active |
| `photos-vm` | Existing photo library, database, cache and ML workload | NixOS guest observed; relevant containers active, some reported healthy |

All five are current fleet members. `core_for_adaptation` in the model describes a smaller adopter design, not whether a guest exists. The existing substrate is **Proxmox VE**, not a NixOS physical host. Home Assistant OS is a separate integrated appliance; phones and provider services are adjacent dependencies. The single-server architecture shares hardware/storage/power risk; no fresh hypervisor or physical-placement audit was performed.

## Important present-state distinctions

- **Configured but inactive:** Paperless source is enabled, but web/consumer/scheduler/task-queue units were inactive. Redis and its private ingress sidecar were active. This is not a working document archive claim and does not diagnose why it was inactive.
- **Present, not merely suggested:** Personal Hub's authenticated live API and interface/publisher services were active. Current source replaces the synthetic page on the existing transport. A legacy preview-named unit does not establish synthetic-only behavior.
- **Mail review is layered:** isolated broker/Signal services were active and ingest/extract timers present. Local extractor inference is disabled in source. Processing-release, identity-migration and network-enforcement gates are independent; an idle one-shot or an active broker does not establish automatic extraction or approved destination writes.
- **Source-disabled:** location history and visual infrastructure inventory are represented but disabled. Historic activation PRs do not override current source.
- **Source-gated:** budget-categorization credentials are disabled independently of its installed workflow; auxiliary workbench readiness is false; public edge ingress is disabled independently of private application and publication features. Provider-migration connectors have separate credential gates despite an active mail bridge.
- **Scheduled, not constantly running:** updater, archive, backup, observer and independent dead-man timers exist. An inactive timer-driven one-shot is not automatically an outage. This publication does not establish their latest external effects.
- **Runtime unknown:** the edge guest was not accessed, and coding, browser/document tools, home-automation actions and deployment workflows were not exercised. No alternate hypervisor route was used to expand management access.
- **Acceptance unknown:** there were no fresh browser logins, phone messages, uploads, playback tests, finance/calendar/travel writes, restores or deployments for this snapshot. Container health is self-reported, not user acceptance.

## What changed from the initial public reference

The inventory now treats media/photos as existing members, records source and runtime evidence separately, adds current Hub/network/calendar/dead-man/controller/mail-bridge/workbench capabilities, and moves edge-RSS/voice design ideas into a separate recommendations list. It does not infer current public RSS availability from an old role name.

## Read this before using it operationally

Use [provenance](provenance.md) for evidence limits and [pitfalls](pitfalls.md) for incident-derived lessons. Operational procedures in [operations](operations.md), network policies in [architecture](architecture.md), and adoption suggestions remain guidance, not claims of complete live enforcement. Obtain private current evidence and explicit authority before acting on any real system.

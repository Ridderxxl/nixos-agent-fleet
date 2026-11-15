# Current fleet service and capability catalog

Snapshot date: **2026-11-15**. This describes the current fleet, not a generic template or a companion installation's subset. All five aliases are existing fleet roles; media/photos are optional only for an adopter. The catalog covers principal service families, not every package or endpoint.

Source and runtime are independent axes. Four guests have bounded read-only observations; the edge role is source-only. No application workflow was accepted for this snapshot. See [current state](current-state.md) and [provenance](provenance.md).

## Labels

- **source-configured:** enabled/represented in inspected committed configuration, not proof of deployment.
- **source-gated:** an independent readiness, credential or publication gate remains.
- **source-disabled:** explicitly disabled in inspected source.
- **source-pattern:** a represented integration/operating workflow, not an availability assertion.
- **reference-pattern:** adaptation guidance only; outside the current-services list.
- **unit-active:** relevant process/container units active; not complete application health.
- **unit-inactive:** application units inactive; no cause or failure diagnosis implied.
- **scheduled-job-observed:** timer infrastructure present; idle one-shots are not outages.
- **not-assessed:** no direct runtime evidence for that capability.

Product names are upstream software identifiers, not private hostnames. Edge placement does not establish public exposure. Every capability has `acceptance_status: not-assessed`.

| ID | Role | Capability / software | Source evidence | Runtime evidence | Important boundary |
|---|---|---|---|---|---|
| rss | apps-vm | RSS reading — Miniflux | source-configured | unit-active | Private feed reading; do not infer that an edge RSS endpoint is currently published. |
| bookmarks | apps-vm | Bookmark archive — Linkwarden | source-configured | unit-active | Bookmark storage and archived-page retrieval. |
| budget | apps-vm | Personal budgeting — Actual Budget | source-configured | unit-active | Private financial state; HTTPS and separate write approvals. |
| tasks | apps-vm | Task management and scoring — Vikunja / Task Coach | source-configured | unit-active | Task scoring and integrations; no automatic permission to modify tasks. |
| documents | apps-vm | Document archive and OCR — Paperless-ngx | source-configured | unit-inactive | Source enabled; application units inactive in snapshot. Active ingress is not backend readiness. |
| recipes | apps-vm | Recipes and meal planning — Recipe / meal-planning application | source-configured | unit-active | Personal recipe and meal records are never public examples. |
| calendars | apps-vm | Calendar collections and synchronization — CalDAV services / synchronization workers | source-configured | unit-active | Ownership, privacy and loop prevention require collection-level tests. |
| travel | apps-vm | Travel planning — Travel planning application | source-configured | unit-active | Imports and provider writes remain independently approved. |
| social-private | apps-vm | Private social analytics — Social archive / analytics application | source-configured | unit-active | Per-account analytics and optional publication workflows. |
| dashboard | apps-vm | Private service dashboard — Service launcher / dashboard | source-configured | unit-active | Navigation is not an authentication or health guarantee. |
| location | apps-vm | Location history — Dawarich | source-disabled | not-assessed | Represented but explicitly disabled at inspection. |
| asset-inventory | apps-vm | Visual infrastructure inventory — Homelable | source-disabled | not-assessed | Represented but explicitly disabled at inspection. |
| edge-social | edge-vm | External-user social application — Authenticated analytics / publishing application | source-gated | not-assessed | Source enables application and private ingress; public publication is disabled at inspection. |
| hermes | agent-vm | Agent runtime — Hermes Agent | source-configured | unit-active | Persistent sessions, memory, skills, tools and provider configuration. |
| signal | agent-vm | Phone messaging — Signal / signal-cli | source-pattern | unit-active | Sender allowlists and human-owned enrollment; linked account material is sensitive. |
| android | agent-vm | Android companion — Third-party Hermes-Relay plugin and companion | source-pattern | unit-active | Separate from the upstream hosted messaging-relay connector; pairing and grants are explicit. |
| web-chat | agent-vm | Private browser chat — Authenticated Hermes web surfaces | source-pattern | unit-active | Private ingress, session authentication and correct proxy routing must be tested. |
| coding | agent-vm | Coding workers and work tracking — Named coding profiles / task board | source-pattern | not-assessed | Explicit profile, isolated worktree, bounded budget, independent artifact review. |
| knowledge | agent-vm | Knowledge retrieval — Wiki / local knowledge / bookmark tools | source-pattern | not-assessed | Only approved documents and scoped retrieval sources. |
| mail | agent-vm | Searchable mail archive — Read-only mail archive / approved ingest | source-configured | scheduled-job-observed | Mailbox access, retention and outbound effects are separate capabilities. |
| mail-actions | agent-vm | Mail to proposed travel/calendar actions — Structured ingest / review pipeline | source-pattern | unit-active | Independent processing, identity and network-release gates; local extractor inference disabled. Untrusted mail cannot authorize effects. |
| home-control | agent-vm | Home automation capabilities — Home Assistant bridge | source-pattern | not-assessed | Prefer narrow capability services; do not grant a broad admin token by default. |
| budget-agent | agent-vm | Budget categorization automation — Reviewed categorization workflow | source-gated | not-assessed | Workflow enabled in source; its credentials independently disabled at inspection. |
| updates | agent-vm | Dependency update proposals — Deterministic updater / publication broker | source-pattern | scheduled-job-observed | Allowlisted pins, builds, reviewable PR and fixed-recipient report; no autonomous merge/deploy. |
| observation | agent-vm | Fleet failure observation — Deterministic watchdog / observers | source-pattern | scheduled-job-observed | Persist evidence; distinguish stale incident state from fresh failure. |
| agent-backup | agent-vm | Agent state backup — Declared state-backup jobs | source-pattern | scheduled-job-observed | SQLite consistency, provider auth, paired devices and isolated restore must be covered. |
| media | media-vm | Media playback and automation — Jellyfin / Sonarr / Radarr / SABnzbd / Jellyseerr / Pinchflat / Maintainerr | source-configured | unit-active | Declare OCI workloads; isolate library paths from private photos. |
| photos | photos-vm | Photo library — Immich / PostgreSQL / cache / machine learning | source-configured | unit-active | Database and media backup consistency; mount-writability and upload acceptance. |
| document-tools | agent-vm | PDF / Office / OCR tools — Document processing tooling | source-pattern | not-assessed | Explicitly approved files, pinned executables, bounded processing. |
| browser-tools | agent-vm | Browser automation — Browser tooling | source-pattern | not-assessed | Test actual NixOS browser launch; no public debugging endpoint or copied personal cookies. |
| personal-hub | agent-vm | Personal planning and review hub — Personal Hub API / web UI | source-configured | unit-active | Authenticated live interface and broker-mediated reviewed writes; legacy preview transport naming does not mean synthetic-only content. |
| network-tools | apps-vm | Private network companion — LAN-Orangutan | source-configured | unit-active | Private application on the existing apps guest, not another VM. No new network scan run. |
| calendar-sync | apps-vm | Availability synchronization — Keeper / Radicale integration | source-configured | unit-active | Availability projection is not blanket shared-calendar write permission. |
| deadman | apps-vm | Independent observer-failure notification — Deterministic dead-man checker / dedicated Signal transport | source-pattern | scheduled-job-observed | Independent of the agent runtime; timer presence does not prove delivered alerts. |
| deployment | agent-vm | Approval-triggered deployment controller — Fixed-scope deployment broker | source-pattern | not-assessed | Exact-target approval workflow represented in source, not an arbitrary model-controlled remote shell. |
| mail-provider | agent-vm | Private mail-provider bridge — Proton Mail Bridge / migration tooling | source-configured | unit-active | Bridge liveness does not prove mailbox migration completion; credentialed connectors are separately gated. |
| aux-workbench | agent-vm | Auxiliary agent workbench preparation — Readiness-gated workbench | source-gated | not-assessed | Preparation enabled, readiness false; not a running or usable listener claim. |

## Per-capability observation notes

- **rss**: Native RSS service active.
- **bookmarks**: Bookmark application and database container units active; application reported healthy.
- **budget**: Budget container active; no financial records read.
- **tasks**: Task API and scoring services active; auto-labeling timer present. Scoring and notifications not tested.
- **documents**: Application units inactive; Redis and ingress sidecar active. Cause not established.
- **recipes**: Recipe application and database services active; no private content read.
- **calendars**: CalDAV server active; collection rights and provider synchronization not tested.
- **travel**: Travel container active and reported healthy; no reservations or attachments read.
- **social-private**: Private analytics service active; provider connectivity and publication not tested.
- **dashboard**: Web-server and endpoint sidecar active; browser workflow not tested.
- **location**: Source-level representation only; no direct runtime or workflow assessment.
- **asset-inventory**: Source-level representation only; no direct runtime or workflow assessment.
- **edge-social**: Source-level representation only; no direct runtime or workflow assessment.
- **hermes**: Multiple agent gateway units active; provider-backed chat not retested for this snapshot.
- **signal**: Separate Signal daemon units active; no enrollment or test messages generated.
- **android**: Companion transport service active; physical-device pairing and reconnect not tested.
- **web-chat**: Dashboard and companion endpoint units active; authentication and chat acceptance not repeated.
- **coding**: Source-level representation only; no direct runtime or workflow assessment.
- **knowledge**: Source-level representation only; no direct runtime or workflow assessment.
- **mail**: Archive extraction and indexing timers present; search correctness and archive coverage not tested.
- **mail-actions**: Broker and Signal interaction services active; ingest/extract timers present, one-shots idle. No destination writes tested.
- **home-control**: Source-level representation only; no direct runtime or workflow assessment.
- **budget-agent**: Source-level representation only; no direct runtime or workflow assessment.
- **updates**: Updater timer present; PR publication and report delivery not verified.
- **observation**: Observer polling timer present; no incidents cleared or failures triggered.
- **agent-backup**: State-backup timer present; contents, off-host copies and restore not assessed.
- **media**: All seven listed media container units active; some report health. Playback/download/cleanup not exercised.
- **photos**: Photo server, database, cache and ML units active; server/database/ML reported healthy. Upload/restore not exercised.
- **document-tools**: Source-level representation only; no direct runtime or workflow assessment.
- **browser-tools**: Source-level representation only; no direct runtime or workflow assessment.
- **personal-hub**: Live API and interface/publisher units active; individual planning and approval workflows not retested.
- **network-tools**: Application container active and reported healthy.
- **calendar-sync**: Synchronization container and endpoint sidecar active; providers and collections not assessed.
- **deadman**: Dedicated linked-device transport active and timer present; no alert triggered.
- **deployment**: Source-level representation; no deployment or controller workflow exercised.
- **mail-provider**: Headless bridge unit active; no mailbox content or migration state read.
- **aux-workbench**: No runtime assessment; source readiness gate closed.

## Adjacent systems

Home Assistant OS is a separate appliance, not another NixOS guest in this inventory. The hypervisor, phones and external providers are separate platform/authority boundaries and were not runtime-assessed.

## Adaptation ideas — not current-fleet claims

These entries live in `recommendations`, outside `services` in the model:
- **edge-rss — Externally accessible RSS pattern**: Suitable role example, not a claim that a public RSS service is active.
- **voice — Voice input/output**: Optional; media tooling alone does not establish configured voice support.

## Integration boundaries

- Signal and Android companion are independent transports with separate enrollment and permission tests.
- Mail → isolated ingest/review broker → trusted human confirmation → intended travel/calendar destination. Broker liveness does not prove processing release, successful extraction, destination acceptance or consent for writes.
- Personal Hub's live application is enabled in source; a preview-named unit owns transport, not evidence of synthetic-only content.
- Tasks → scoring → dashboard/notifications requires independent correctness and delivery checks.
- Budget UI is separate from credential-gated categorization. Location history and visual infrastructure inventory remain source-disabled.
- Bridge liveness does not imply enabled credentialed migration connectors or completed migration.
- Watchdog and independent dead-man paths have separate evidence and delivery boundaries.

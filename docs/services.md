# Service and capability catalog

This table is generated as a human-readable companion to `fleet.json`. It covers the fleet's main service families, not every package, hidden integration or endpoint. No live service health was assessed. There are no public service URLs in this catalog.

## Evidence labels

- **source-configured:** represented/enabled in inspected source; runtime acceptance not established.
- **source-gated:** represented but readiness, credentials or public publication is gated.
- **source-disabled:** explicitly disabled in inspected source.
- **source-pattern:** represented workflow/integration; no independent availability assertion.
- **reference-pattern:** a suggested adaptation, not a current-fleet fact.

Product names are descriptive upstream identifiers, never the private VM or user names. `edge-vm` describes a trust class, not proof of internet exposure. In particular, a historic RSS-oriented role must not be mistaken for a currently published RSS instance.

| ID | Role | Capability / software | Evidence | Important boundary |
|---|---|---|---|---|
| rss | apps-vm | RSS reading — Miniflux | source-configured | Private feed reading; do not infer that an edge RSS endpoint is currently published. |
| bookmarks | apps-vm | Bookmark archive — Linkwarden | source-configured | Bookmark storage and archived-page retrieval. |
| budget | apps-vm | Personal budgeting — Actual Budget | source-configured | Private financial state; HTTPS and separate write approvals. |
| tasks | apps-vm | Task management and scoring — Vikunja / Task Coach | source-configured | Task scoring and integrations; no automatic permission to modify tasks. |
| documents | apps-vm | Document archive and OCR — Paperless-ngx | source-configured | Requires verified storage and actual application acceptance. |
| recipes | apps-vm | Recipes and meal planning — Recipe / meal-planning application | source-configured | Personal recipe and meal records are never public examples. |
| calendars | apps-vm | Calendar collections and synchronization — CalDAV services / synchronization workers | source-configured | Ownership, privacy and loop prevention require collection-level tests. |
| travel | apps-vm | Travel planning — Travel planning application | source-configured | Imports and provider writes remain independently approved. |
| social-private | apps-vm | Private social analytics — Social archive / analytics application | source-configured | Per-account analytics and optional publication workflows. |
| dashboard | apps-vm | Private service dashboard — Service launcher / dashboard | source-configured | Navigation is not an authentication or health guarantee. |
| location | apps-vm | Location history — Dawarich | source-disabled | Represented but explicitly disabled at inspection. |
| asset-inventory | apps-vm | Asset inventory — Asset-management application | source-disabled | Represented but explicitly disabled at inspection. |
| edge-social | edge-vm | External-user social application — Authenticated analytics / publishing application | source-gated | Source enables application and private ingress; public publication is disabled at inspection. |
| edge-rss | edge-vm | Externally accessible RSS pattern — Miniflux as an edge workload | reference-pattern | Suitable role example, not a claim that a public RSS service is active. |
| hermes | agent-vm | Agent runtime — Hermes Agent | source-configured | Persistent sessions, memory, skills, tools and provider configuration. |
| signal | agent-vm | Phone messaging — Signal / signal-cli | source-pattern | Sender allowlists and human-owned enrollment; linked account material is sensitive. |
| android | agent-vm | Android companion — Third-party Hermes-Relay plugin and companion | source-pattern | Separate from the upstream hosted messaging-relay connector; pairing and grants are explicit. |
| web-chat | agent-vm | Private browser chat — Authenticated Hermes web surfaces | source-pattern | Private ingress, session authentication and correct proxy routing must be tested. |
| coding | agent-vm | Coding workers and work tracking — Named coding profiles / task board | source-pattern | Explicit profile, isolated worktree, bounded budget, independent artifact review. |
| knowledge | agent-vm | Knowledge retrieval — Wiki / local knowledge / bookmark tools | source-pattern | Only approved documents and scoped retrieval sources. |
| mail | agent-vm | Searchable mail archive — Read-only mail archive / approved ingest | source-configured | Mailbox access, retention and outbound effects are separate capabilities. |
| mail-actions | agent-vm | Mail to proposed travel/calendar actions — Structured ingest / review pipeline | source-pattern | Untrusted source content is evidence, never an authorization instruction. |
| home-control | agent-vm | Home automation capabilities — Home Assistant bridge | source-pattern | Prefer narrow capability services; do not grant a broad admin token by default. |
| budget-agent | agent-vm | Budget categorization automation — Reviewed categorization workflow | source-gated | Workflow enabled in source; its credentials independently disabled at inspection. |
| updates | agent-vm | Dependency update proposals — Deterministic updater / publication broker | source-pattern | Allowlisted pins, builds, reviewable PR and fixed-recipient report; no autonomous merge/deploy. |
| observation | agent-vm | Fleet failure observation — Deterministic watchdog / observers | source-pattern | Persist evidence; distinguish stale incident state from fresh failure. |
| agent-backup | agent-vm | Agent state backup — Declared state-backup jobs | source-pattern | SQLite consistency, provider auth, paired devices and isolated restore must be covered. |
| media | media-vm | Media playback and automation — Jellyfin / Sonarr / Radarr / SABnzbd / Jellyseerr / Pinchflat / Maintainerr | source-configured | Declare OCI workloads; isolate library paths from private photos. |
| photos | photos-vm | Photo library — Immich / PostgreSQL / cache / machine learning | source-configured | Database and media backup consistency; mount-writability and upload acceptance. |
| voice | agent-vm | Voice input/output — STT / TTS provider or local runtime | reference-pattern | Optional; media tooling alone does not establish configured voice support. |
| document-tools | agent-vm | PDF / Office / OCR tools — Document processing tooling | source-pattern | Explicitly approved files, pinned executables, bounded processing. |
| browser-tools | agent-vm | Browser automation — Browser tooling | source-pattern | Test actual NixOS browser launch; no public debugging endpoint or copied personal cookies. |

## Integration map: intent versus acceptance

- Phone ↔ agent: Signal and Android companion are different transports; each requires its own enrollment, authorization, reconnect and actual reply tests.
- Agent → private services: use scoped API/tool capabilities. A functioning tool client does not grant permission for writes.
- Mail → structured proposal → human review → travel/calendar action: ingest and preview do not authorize downstream changes.
- Tasks → scoring → home dashboard/notifications: task state and user-visible scoring require end-to-end checks; do not claim notification delivery from a queue receipt alone.
- Travel + location + photos: possible complementary tools, not evidence of complete automatic synchronization. Location history is disabled in the inspected source.
- Budget UI + categorization workflow: running the budgeting service does not enable agent categorization credentials or approve financial writes.
- Observer → incident record → notifier: service liveness, incident freshness and delivered notification are distinct facts.

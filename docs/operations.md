# Operational contracts

These are adaptation runbooks, not commands preauthorized against an existing fleet. Resolve real target, account, privilege boundary and recovery console privately before any action.

## Source change and deployment

1. Preserve unrelated dirty work; use a focused branch from the intended baseline.
2. Read the relevant policy, source and current observation. Define one acceptance criterion per affected user workflow.
3. Implement configuration rather than a permanent live patch. Mark any unavoidable bootstrap explicitly and capture its reproducible replacement.
4. Validate syntax/evaluation, affected tests and host build under bounded concurrency. Review source pins and lockfile changes.
5. Publish a reviewable PR with actual command results, limitations, risk and rollback. No fabricated pass or silent skipped check.
6. Obtain approval for the exact merge and deployment scope. Preserve a second console/session and the previous generation.
7. For access/firewall/storage/SSH changes, test the candidate without making it the irreversible boot default; verify a second authorized connection and unauthorized denial before committing the rollout.
8. Activate one host at a time in dependency-aware order. Record exact commit and generation.
9. Verify unit/process state **and** authenticated application behavior, required mounts and user-visible action. Keep migration rollback separate from generation rollback.

This guide deliberately does not contain a copy/paste pull-and-switch command against a fictional host.

## Dependency proposal pattern

Use a dedicated deterministic job rather than a nightly unconstrained LLM shell:

- Discover releases only for an explicit source allowlist; validate version/digest formats, source identity, architecture and downgrade rules.
- Pin immutable inputs; permit only exact reviewed field/path changes.
- Build affected host closures sequentially or within a measured global budget; do not activate them.
- Hand publication to a constrained credential-holding broker with fixed repo/branch/ref rules; compare candidate, pushed and PR-head SHAs.
- Report risk and evidence to a fixed operator destination. A successful dry run is not a pushed PR or delivered report.
- Require separate exact approval for merge and rollout. A no-change second run and exercised rejection path are useful acceptance tests.

This is a source-backed design pattern, not a bundled or independently audited deployment engine in this public repository.

## Failure observation pattern

Prefer deterministic collection and persisted incident evidence over repeated LLM polling. Collect positive expected-service coverage and necessary authenticated probes. Distinguish observer heartbeat, observation time, incident last-seen time and notification delivery time. A stored unresolved incident is not proof of a fresh outage.

Read-only triage: identify target/commit/time → inspect the exact incident evidence → correlate unit exit state and bounded logs → reproduce the actual failing operation → propose a declarative fix → verify after the collector has actually run the new build. Do not clear incidents or reset failures merely to make a dashboard green. Use a separately functioning alert path for failures of the primary messaging transport itself.

## Backups and restore

| State | Backup requirement | Restore acceptance |
|---|---|---|
| Nix configuration | Private Git remote plus recovery access | Build intended revision with correct hardware/secrets |
| App databases | Consistent dump/snapshot with version metadata | Import into isolated compatible service and read records |
| Uploads, documents, photos | Matching durable file backup | Verify sample files and database/file consistency |
| Hermes state | Consistent session DB, config, skills, memory, auth, cron, plugins/pairings | Isolated startup, session read, approved workflow; avoid duplicate live jobs |
| Signal identity | Sensitive enrollment/client state, encrypted and access-controlled | Deliberate recovery without concurrently running duplicate identities |
| Host substrate | VM/disk/mapping/network definitions and console procedure | Reconstruct a test guest without touching production data |
| Decryption/recovery identities | Independent protected copy | Authorized recovery works; unrelated host identity cannot decrypt |

An existing directory, a recent timestamp, successful job, content coverage and exercised restore are different evidence levels. Keep an independent off-host encrypted copy. Test restores with networking/jobs disabled until duplicate Signal senders, schedules and write-capable integrations cannot act accidentally.

## Reporting format

State only: what changed; exact artifact/revision; checks that ran and results; merged/deployed/accepted status; remaining risks or approval gates. Do not call a PR “delivered” when the user requested production usability. Do not say a service is unavailable merely because a token is missing: HTTP authorization failure and network reachability are separate observations.

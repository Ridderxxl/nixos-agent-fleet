# Common pitfalls and operational lessons

Reviewed **2026-11-15**. These lessons derive from a recent companion installation's permission/gateway incident and selected incidents in the first 200 private PR records. They are sanitized retrospective accounts, not instructions to replay old fixes. No historical test result is claimed as newly reproduced. See [provenance](provenance.md).

Each fix below requires current target/version evidence, a declarative reviewed change, separate activation authority and a relevant acceptance test. Do not grant permissions, delete state or restart production just to make a diagnostic pass.

## 1. Filesystem ownership, Git trust, GitHub permission and sudo are different

**Symptoms:** permission denied writing a checkout, failed index/ref locks, dubious ownership, missing author identity, or a push denied after successful SSH authentication.

**Cause:** an agent was using a root-owned deployment checkout; changing execution user changed Git identity and the SSH key offered. Historical attempts alternated between running as administrator, running Git through sudo and forwarding an SSH agent. Later evidence showed a read-only key could authenticate before the intended write key. Neither `safe.directory` nor GitHub membership makes a filesystem writable.

**Fix:** prefer an agent-owned working checkout for branch/PR work and keep activation in a separate constrained administrator/controller path. Choose repository-specific SSH identity explicitly and inspect its registered permission. Apply Git trust exceptions only to an intended reviewed path. Do not treat broad sudo, blanket ownership changes, global trust wildcards, forwarded credentials or historical hard resets as a reusable fix.

**Verify:** as the real working identity, create/commit in its checkout, read the intended remote and publish an authorized branch; independently read back its SHA. Check privileged activation is still denied without its own approval. Never test a read-only key by writing to a protected reference repository.

## 2. Gateway identity refusal is not just a permission or stale-PID problem

**Symptoms:** the CLI worked as the runtime user, a preparation unit reported `active (exited)`, but chat returned `service_identity_unverified`. Gateway/phone services were not ready and a stale registration referred to a dead process.

**Cause:** the installed identity verifier did not recognize a Nix-generated shell wrapper as a gateway command. Independent onboarding gates also coupled local chat to unfinished optional phone enrollment. Removing a PID file alone could not fix either problem; the support identity intentionally lacked sudo.

**Fix:** inspect the exact installed verifier, rendered service `ExecStart`, execution identity and runtime home. In this incident a direct gateway command passed the unchanged verifier in an in-memory comparison, supporting a declarative service repair. Separate base local/provider chat readiness from optional Signal/Android enrollment. Have the local human perform privileged activation; do not disable identity verification, fabricate enrollment markers or expand support privileges.

**Verify:** distinguish failed live discovery, accepted in-memory candidate, built unit, activated generation and actual own-provider chat. The historical repair reached gateway/chat checks; that does not validate every phone feature or substitute for the owner's normal-launch acceptance. Re-test the pinned version rather than assuming all shell wrappers are unsupported forever.

## 3. Secret persistence and secret isolation are separate problems

**Symptoms:** applications disappeared after reboot despite intact networking; another verification accidentally exposed a provider key.

**Cause:** a secret file under volatile runtime storage had no boot-time reprovisioner. Separately, an agent-owned private directory was incorrectly treated as protecting a credential from the same agent UID.

**Fix:** provide reproducible boot-time delivery from an approved secret system, or document a deliberately protected persistent bootstrap and recovery path. Keep the Nix store and public Git free of secrets. A root-readable environment file protects that file, not automatically the credential after injection into a same-UID process. Use separate service identities or a credential-holding semantic broker when actual credential isolation is required; rotate exposed material.

**Verify:** inspect only existence, owner/mode and intended access denials; never print values. In an approved maintenance/recovery test, prove provisioning survives reboot and the consumer works. Distinguish file-level denial from process/environment/API isolation.

## 4. Container conventions change across images and versions

**Symptoms:** missing schema, invalid database URL, conflicting restart flags, failed user switch, cache ownership errors or SQLite access denial.

**Cause:** image entrypoints, supported secret variables, URL encoding, actual runtime UID, writable paths and required capabilities were assumed. systemd-managed OCI containers also had conflicting Docker restart behavior. One frontend initially appeared to have a name-resolution race; a later failure showed a separate capability-dependent ownership operation.

**Fix:** inspect the pinned image's upstream entrypoint and documented deployment contract. Match the real database role and correctly encode URL components. Give only evidenced capabilities or prepare writable ownership outside the container. Do not copy historical numeric UIDs, add blanket capabilities or use privileged mode to mask the cause. Bound retries and surface permanent failure rather than looping indefinitely.

**Verify:** examine the exact rendered container command, cold start, database migration and file ownership under the intended user. Read the failing operation after each change; a successful transient DNS retry does not close a distinct ownership failure.

## 5. A corrected mount path can strand the live data

**Symptoms:** the service builds/starts but appears empty, loses sessions or writes to the container layer.

**Cause:** the actual application data directory differed from the volume destination. A path corrected for one image was later obsolete; blindly repeating that earlier fix would reverse the current contract.

**Fix:** identify where the running pinned image truly writes databases, signing/encryption state, uploads and other durable data. Before changing the mount, quiesce, preserve the complete live state, migrate to the intended volume, verify it and retain rollback material. A source merge is not permission to activate a data migration.

**Verify:** compare complete required state with the preserved source; recreate the container and exercise an approved synthetic write/read after restart. A closure build cannot discover data stranded in an old writable layer.

## 6. Proxy reachability is not authenticated application readiness

**Symptoms:** a live private endpoint returned 404s, the wrong application, CORS errors or login sessions that would not stick over HTTPS.

**Cause:** unsupported path-prefix hosting, upstream-port collision, incorrect origin configuration or ignored forwarded HTTPS. Early prefix-stripping routing was later replaced by per-application endpoint identities; the stopgap is not today's universal prescription.

**Fix:** trace client → ingress → exact upstream → app origin/session behavior. Choose supported base-path/subdomain behavior and trust only the actual proxy hops. Keep secure cookies and authentication; do not disable CORS, broadly trust forwarded headers or make a private service public as a workaround.

**Verify:** unauthenticated denial, authenticated login/session persistence, redirects/assets and the intended application workflow from the real client. An active sidecar can front an inactive backend: that distinction is visible for the document archive in this snapshot.

## 7. Backups can leave dependent applications stopped

**Symptoms:** a backup completed but application dependents stayed down; a database dump failed because the assumed default database role did not exist.

**Cause:** stopping a cache/database propagated to reverse dependencies, while restart logic only restored the explicitly stopped unit. A separate dump command used a role different from the configured cluster owner.

**Fix:** quiesce dependents before dependencies, restore dependencies first and preserve each service's prior state. Use the actual database owner and a consistent database/files boundary. Fail visibly if recovery cannot safely complete; never blindly start everything that was previously stopped.

**Verify:** test success and failure paths with initially running and stopped services. Read the dump and restore it into an isolated compatible environment. A successful timer or file timestamp does not prove content coverage or restorability.

## 8. Readable storage does not prove writable uploads

**Symptoms:** existing photo paths could be read/stat-ed while new uploads failed with a filesystem resource error.

**Cause:** the original mount probe exercised metadata only and missed the failing create operation. Different directories on the same mapped storage could behave differently.

**Fix:** scope a synthetic create/close/delete probe to an approved directory and verify mount source/type/backing identity. Recovery must recognize the evidenced failure, quiesce the correct dependents, preserve prior state and remain stopped on unsafe paths. A guest remount can mitigate a symptom without proving the host-side cause is solved. Never generalize one errno/remount recipe to every I/O error.

**Verify:** approved write-path tests before and after repair, mount identity, negative wrong/missing-mount cases, and a real application upload when separately authorized. Do not perform production write probes as part of a documentation audit.

## 9. Correct hardware discovery still needs stable identity review

**Symptoms:** a plausible hardware scaffold built but did not match the live disk controller or unambiguous boot device.

**Cause:** guessed initrd drivers and interchangeable filesystem labels. Even an earlier discovery-based correction retained a label and was subsequently tightened to a filesystem UUID.

**Fix:** discover each real guest's hardware, prefer verified filesystem identities and keep formatting/provisioning consistent with the per-guest configuration. Do not clone another guest's UUID or use a universal deterministic UUID across co-visible disks. Preserve console recovery and avoid replacing the boot default before testing.

**Verify:** compare discovered controller/modules, actual disk UUID and evaluated root device; then authorized boot acceptance with recovery access. Evaluation alone cannot establish next-boot success.

## 10. Build resource limits and capacity failures need the right owner

**Symptoms:** a rebuild wedged a guest, the updater made no useful progress under memory pressure, or a nightly run refused immediately.

**Cause:** the interactive build path, Nix daemon and updater can use different cgroups. Soft memory throttling, hard limits and host headroom are different constraints. Other fast failures were a deliberate free-space preflight, not updater logic defects.

**Fix:** measure the actual failing process/cgroup and host capacity. Bound daemon workers and caller concurrency independently; size swap/reserves and garbage collection around measured demand and rollback needs. Do not copy historical memory sizes, remove preflights or purge every generation to get green output.

**Verify:** supervised build of the exact candidate while measuring pressure/headroom and guest responsiveness; confirm retained rollback artifacts. An updater limit does not establish containment of an unrelated manual rebuild.

## 11. A controller receipt must match the artifact and target set

**Symptoms:** source discovery/builds looked successful but publication lacked an acknowledgement, approved rollout rejected a receipt, or a harmless build-result symlink triggered a trust rejection.

**Cause:** socket EOF/ack races, inconsistent target scope across runner/report/controller, or an overbroad trust check. A correction in only one producer/consumer left the end-to-end contract broken.

**Fix:** use bounded request/response framing; bind receipts to exact artifact, independently derived targets and successful gates. Validate at the credentialed boundary, not only the proposer. Treat build artifacts narrowly without weakening rejection of unexpected links/ownership. Never treat a changed SHA or missing target receipt as close enough.

**Verify:** real acknowledgement round trip, rejected malformed/stale/wrong-target requests, remote candidate/PR head equality and controller validation of the same receipt. Publication, merge, approved activation and live acceptance remain separate.

## 12. NixOS runtime compatibility is not installer success

**Symptoms:** gateway reinstall loops, editable install failures on read-only source, or a browser working only until reinstall/garbage collection.

**Cause:** parsing the wrong version token; generic Linux binaries requiring an unavailable loader; a writable build step aimed at immutable source; or a launcher hardcoding a superseded store path. Historical proposals include unmerged fixes, so PR existence alone is not deployment evidence.

**Fix:** resolve the installed launcher → interpreter → pinned source → runtime home and required build-time writes. Use declared Nix dependencies and a deliberately managed writable build area when needed. Pin dependency policy separately from source pins. Do not assume a historical musl replacement, loader setup or browser shim is universally sufficient or current.

**Verify:** invoke the real service-account executable and actual browser navigation on the installed generation, including after an authorized reinstall/restart. A version string, source pin or passing package build is weaker than exercising the real launcher and consumer.

## Reusable triage order

Exact target/identity/version → failing layer and supported cause → preserved state/recovery path → scoped declarative fix and tests → reviewed artifact → explicit activation authority → real user-workflow verification. Keep inaccessible or untested stages visibly open instead of broadening access or claiming success from a nearby layer.

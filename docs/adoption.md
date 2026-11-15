# Adoption checklist

This is a design-to-implementation checklist. There is no installation script in this repository.

## 1. Choose scope privately

- [ ] Existing hypervisor or fresh NixOS/KVM host; preserve a working platform unless migration is required.
- [ ] Required roles: apps, edge, agent; decide independently on media/photos.
- [ ] Hardware/resource measurements, growth assumptions, actual disks and GPU ownership.
- [ ] Named human administrator and independent recovery console.
- [ ] Public applications and intended users; no default blanket exposure.
- [ ] Data classification, backup destination and restore acceptance.

## 2. Create a separate private implementation

- [ ] Initialize a private repository; adapt templates instead of copying private operational history.
- [ ] Discover real hardware configuration and disk/mount identities for each guest.
- [ ] Create reviewed host/module structure, flake outputs and lockfile for the chosen release.
- [ ] Separate human administration, model runtime, updater, notifier, deployer and backup identities.
- [ ] Generate host-specific decryption identities; do not place the operator's general identity on the edge.
- [ ] Add effective network allow/deny tests, state directories, secret rotation behavior and service restart rules.
- [ ] Put locked source/dependency policy, actual tests and documentation in CI.

## 3. Deliver the base agent first

- [ ] Agent account cannot sudo or access container sockets/admin keys.
- [ ] Pinned executable and documented dependency closure actually start.
- [ ] Human privately enrolls own provider and gets a real model-backed reply.
- [ ] Private browser ingress rejects anonymous requests and reaches the intended profile.
- [ ] Signal enrollment and allowlist verified by a real phone round trip and negative authorization test.
- [ ] Android companion version/pairing/grants tested on the actual device, separately from Signal.
- [ ] Reconnect/restart preserve intended state and routing.
- [ ] Encrypted off-host backup and isolated restore exercised.

## 4. Add services and integrations gradually

- [ ] Accept each app's real authenticated user workflow, database and storage paths.
- [ ] Introduce one agent capability at a time; read-only first, effects separately approved.
- [ ] Test private calendar/finance/mail boundaries with negative cases.
- [ ] Publish edge applications only after TLS, auth, isolation, rate/abuse controls, recovery and revocation checks.
- [ ] Add deterministic observation and proposal automation after manual workflow works.
- [ ] Record exact deployed commit and remaining unverified gates privately.

## 5. Share safely

Keep real inventory and observations private. Export only deliberately generalized documentation into a fresh public tree. Scan filenames, file contents, commits and metadata. Publishing under a personal GitHub account still associates that account with the reference; content sanitization is not author anonymity.

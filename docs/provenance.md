# Evidence, provenance and limits

## Snapshot basis — 2026-11-15

The subject is the **current fleet**, not a generic architecture or the subset useful for a companion installation. Evidence comprises the current committed private configuration, selected current runbooks, bounded read-only runtime observations collected on this date, and selected historical incident records. Existing unrelated uncommitted operational edits were not copied or changed. Private commit IDs, source URLs, role mappings, actual paths, network identities and raw operational output are deliberately excluded.

The public representation has five NixOS guest roles on a Proxmox-based design, alongside a separate Home Assistant OS integration. No deployable flake, guest image or physical-host implementation is supplied. A NixOS/KVM physical host is an alternative, not a deployed fact.

## Evidence axes

1. **Source:** enabled configuration, independent readiness/credential/publication gates, explicitly disabled features, or represented integration patterns. Current configuration takes precedence over old migration prose for these labels.
2. **Runtime:** on four guests, identity/platform plus bounded systemd unit/timer and container-state metadata. These establish process/timer presence and reported health only. Edge and hypervisor runtime were not inspected; management boundaries were not bypassed.
3. **Acceptance:** explicitly **not assessed** for every cataloged capability. No fresh end-to-end user workflow or external effect was exercised for publication.
4. **Recommendation:** adaptation ideas live separately from the current-services inventory. Normative security/backup contracts elsewhere are not attestation that every legacy component meets them.

Observations were collected earlier on the snapshot date and are not a continuously refreshed status page. A guest's checked-out commit is not its deployed source identity. Different checkouts and active generations were observed; this work does **not** establish that all guests run the same revision or canonical main. The machine model's observation date/method/notes are deliberately coarser than the private evidence.

## Historical lessons

The privately collected corpus contains the **200 earliest PR records**, spanning issue/PR numbers 1–211 because issue numbering has gaps. It is not equivalent to PR numbers 1–200, nor 200 verified deployments. Some proposals were not merged. Selected incident bodies and their superseding fixes were reviewed for the [pitfalls guide](pitfalls.md), together with the recent companion permission/gateway incident.

Those are retrospective source accounts, not a new reproduction or independent confirmation of every historical test claim. Lessons distinguish symptoms, supported causes, context-dependent remedies and verification to require now. No private PR URLs, original commit metadata, personal names or copied raw logs are published. Current enablement comes from current source, not those historical records.

## What remains unverified

- Complete deployment provenance and security enforcement across all roles.
- Edge reachability, external-publication readiness and actual public ingress.
- Individual authenticated app workflows, provider connectivity, pairing and delivered notifications.
- Archive/backup content coverage, independent off-host copies and successful restoration.
- Every package, runtime dependency closure and optional tool. Catalog coverage is principal service families, not a complete software bill of materials.
- Exact hypervisor state, guest placement and physical storage health at publication time.

## Publication validation

`tools/validate.py` checks document links, explicit file allowlist, schema/evidence labels, human/catalog/model consistency, privacy patterns, and negative cases. It runs locally and in read-only GitHub Actions. It does not build NixOS, probe production, audit software or prove isolation. There is no application dependency lockfile to audit in this documentation-only tree.

The exact staged blobs also require a private identifying-token scan, URL/email/address inventory and manual review. These are bounded safeguards, not proof that every possible identifier is absent. Remote blob comparison, anonymous reads and exact-revision Actions results establish publication, not live service acceptance.

The GitHub owner's account association remains public. Content sanitization is not account anonymity, and no private-to-public hostname crosswalk is included.

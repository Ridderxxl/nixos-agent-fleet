# Consolidating onto one physical server

## Start with the existing host distinction

The reference has a Proxmox substrate with NixOS VMs. Proxmox VM creation, disks, directory mappings, GPU attachment and consoles are a separate management layer. Do not claim NixOS rebuilds recover that layer automatically.

For an all-NixOS alternative, use a NixOS physical host with KVM/libvirt and separately declared NixOS guests. That requires its own reviewed implementation, hardware discovery, virtual networks, disk provisioning, console recovery and backup tests. This repository contains no such implementation and does not recommend migrating an existing working hypervisor merely for consistency.

## Three-role minimum

1. `apps-vm`: private personal services and their per-application state.
2. `edge-vm`: externally oriented applications, independently publishable and independently revocable.
3. `agent-vm`: unprivileged Hermes runtime and bounded integration tooling.

Add `media-vm` and `photos-vm` if using the broader service catalog. Keeping these separate is especially useful where storage, database upgrades, indexing, transcoding or machine learning would otherwise compete with the agent. A smaller installation can omit them entirely; merging data-heavy services is a new risk decision, not a requirement.

## Capacity planning, not invented sizing

Measure guest working sets, database sizes, growth, transcode demand, model workload, build peaks and restore staging space before assigning RAM/vCPU/disks. Reserve real host memory and storage headroom. Ballooning or overcommit is not extra physical RAM. Coordinate heavy builds across guests; Nix daemon workers need explicit build concurrency limits in addition to caller-side systemd limits.

Do not publish the original operator's hardware IDs or resource allocations. This guide gives no universal numeric VM sizes because no reader hardware has been assessed. A dedicated GPU may not support simultaneous full passthrough to multiple guests; choose and verify a supported device-sharing strategy rather than assuming it.

## Storage contract

| Dataset | Writer | Consumer policy |
|---|---|---|
| Private application databases/uploads | Owning application | No shared writable root across unrelated services |
| Photo originals and photo database | Photo workload | Exclude media scanners and agent bulk access by default |
| Media/downloads | Media workload | Restrict to required datasets; no whole-host mount |
| Agent state | Intended agent identity | Keep other identities, admin secrets and backup originals inaccessible |
| Backup copies | Dedicated backup identity | Independent storage/failure domain; protect deletion and encryption keys |

Prefer stable guest mount identities and verify the actual backing filesystem before activation. Host directory mappings and VirtioFS are substrate dependencies, not magical abstractions: inspect path → guest mount → host mapping → physical storage. A successful metadata lookup does not prove writable storage. A pooled filesystem is not necessarily a mirror, and a mirror is not automatically a recoverable backup.

For critical mount-backed applications: require the expected mount before start; reject fallback writes into an empty root-disk directory; test create/stat/rename/delete with synthetic files in an approved probe location; preserve service state during recovery. GPU and photo ingestion need application-level tests, not just unit status.

## Failure and recovery

All local VMs can disappear together during power, hardware or hypervisor failure. A separate VM on the same host is not an independent backup destination. Keep encrypted off-host copies, host/guest reconstruction notes and an independent console/recovery path. Restore databases and their matching application data together. NixOS generation rollback does not undo database migrations.

If physical separation is later wanted, move the edge or backup role first according to the actual threat/availability need; role-based documentation should survive without renaming every service. No such move is performed or assumed here.

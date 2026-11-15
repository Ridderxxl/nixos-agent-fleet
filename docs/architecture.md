# Architecture and trust boundaries

Snapshot: **2026-11-15**. All five aliases below are existing source-managed roles; bounded runtime evidence is in [current state](current-state.md). Network/security contracts below are guidance, not a complete enforcement audit.

## Role allocation

`apps-vm` is the private application zone. Native NixOS services and OCI workloads are both used; containers are declared through NixOS rather than maintained by manual shell history. Per-application databases and writable directories must remain distinct. A single private VM is an operational convenience, not strong isolation between all its applications.

`edge-vm` is the external-service zone. Put services intended for outside users here rather than adding port forwards into the private application hub. Treat input, uploaded content and a potentially compromised edge process as untrusted. Public ingress, DNS, certificates, application authorization and abuse controls each need independent acceptance. A product name in a hostname is a poor role description: an edge VM may outgrow its original RSS workload without changing its trust class.

`agent-vm` runs Hermes and its private integrations. The model consumes web pages, messages, documents and repositories, all of which may carry hostile instructions. Do not give it implicit control over the hypervisor, edge VM, private databases or all secret identities. Keep human administration, update publication and deployment capabilities separate from the model process.

`media-vm` separates scan/transcode/download workloads from private applications. `photos-vm` separates the photo library and its database/machine-learning workload. They remain on the same physical server in the consolidated design. Mounting the photo library read-only somewhere does not authorize scanners to index it.

## Control and data planes

| Plane | Contains | Does not imply |
|---|---|---|
| Private Git | Desired NixOS configuration, pins, rules, inventory, runbooks, decisions | Runtime secrets, application data, live health or deployment authority |
| Human administration | Console recovery, host setup, identity enrollment, explicit approvals | Credentials shared with every agent/tool |
| Deterministic automation | Bounded observation, update proposals, fixed-target approved jobs | Arbitrary SSH/shell, autonomous merge or blanket mutation |
| Application state | Databases, uploads, documents, calendar collections, provider auth | Rebuildability from Git alone |
| Public reference | Generalized architecture, service families and operating contracts | A replica of the private control plane |

## Network contract for an adaptation

This table is a **recommended policy**, not a claim that every existing rule matches it. Derive actual source/destination/protocol/port rules from your own topology and verify effective unions of tags, grants and firewall rules.

| Source | Destination | Default / allowed exception |
|---|---|---|
| Internet | edge application | Deny except explicitly published TLS application routes |
| Internet | apps, agent, media, photos, management | Deny |
| Edge workloads | Private services and hypervisor | Deny; no implicit management credential or route |
| Operator device | Management plane | Explicit named operator, necessary ports only |
| Approved private client | Private application | Per-service authenticated access |
| Agent | Private API or broker | Specific semantic capability only; prefer read-only |
| Agent | Edge shell / hypervisor shell | Deny by default; separate operator-controlled work |
| Update proposer | Git publication broker | Fixed repository, branch and field allowlist |
| Backup job | Backup target | Scoped job identity; restore/delete privileges separately controlled |

A VPN does not replace application authorization. A per-service VPN sidecar provides an endpoint identity; it is not another VM or necessarily an SSH host. Host administration and application ingress must stay separate. Loopback binding prevents remote access, not access by every local process; unauthenticated local APIs still need a suitable UID/socket/network boundary.

## Declarative does not mean stateless

NixOS can declare services, users, packages, containers, mounts, firewall rules and secret paths. It does not recreate private account enrollment, a growing media library, calendar ownership or Hermes conversations. Keep the desired config and the recoverable state model explicit. A hardware configuration is generated from the real guest, never copied from this public guide.

## Known trade-offs

A shared server is a shared power, kernel/hypervisor, storage and resource failure domain. VMs reduce accidental coupling but cannot provide physical availability or an off-host backup. GPU passthrough/sharing, host storage mappings and recovery consoles remain substrate concerns. The source design is not a proof that these concerns are fully declarative or that every proposed broker boundary is deployed. Security improvements are requirements until independently tested.

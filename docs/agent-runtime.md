# Hermes runtime and companion-agent pattern

## Server versus workstation

On the always-on server, `agent-vm` runs the agent independently of a laptop. A smaller companion installation can run a dedicated NixOS-WSL environment on Windows with the same ideas: non-admin runtime, separate human administrator, pinned setup source, Signal and private phone ingress. WSL is not equivalent to a full independent VM and cannot provide continuous availability while its PC sleeps. The Windows owner remains able to administer it.

The reusable lesson from the companion setup is a bounded agent appliance, not copying another person's state or deploying the entire private application hub on their workstation. A terminal/Start Menu launcher is a user interface, not proof that phone services stay running.

## Runtime layers

- **NixOS:** users, groups, service units, executable paths, source pins, listeners, writable state paths, secret delivery and restart policy.
- **Hermes:** model/provider selection, tools, sessions, memories, skills, profiles and chat surfaces. Use the selected upstream revision's documented commands rather than inventing configuration keys.
- **Private runtime state:** provider OAuth/API keys, session databases, memories, Signal account data and companion pairing state. Never import these from a public repository or blindly clone someone else's profile.
- **Operator context:** private Git checkout and versioned rules. Establish the actual checkout and profile in the executing session; a repository existing on disk does not prove its instructions were loaded.

A declared source revision does not guarantee every dependency is locked/offline. Bootstrap-installed Python/plugin dependencies must have a stated lock and supply-chain policy; measure that property instead of calling all mutable runtime state reproducible.

## Surfaces and acceptance

| Surface | Setup boundary | Acceptance evidence |
|---|---|---|
| Terminal | Intended unprivileged account, actual installed launcher, own provider login | Real model-backed reply and permitted tool call as that identity |
| Browser | Authenticated private ingress and verified proxy origin | Anonymous rejection, authenticated chat, intended profile/session |
| Signal | Human enrollment, sender allowlist, sensitive linked account state | Phone → intended agent → phone round trip; unauthorized sender rejected |
| Android companion | Pinned third-party plugin/client compatibility, one-time pairing, explicit grants | Actual device pairing, chat, approvals, reconnect and same-session continuity |
| Coding workers | Named worker profile, own working tree, budget and permissions | Actual executing identity/model and reviewable artifact/tests |

The third-party **Hermes-Relay Android companion** is not the same thing as upstream Hermes's hosted messaging-relay connector. Verify the relevant project and version before using a guide for one with the other. Pairing is not blanket permission for SMS, accessibility, notification reading, phone actions or terminals. Keep grants off until chosen and tested.

Signal enrollment, provider login, dashboard credentials and phone QR codes are human-only secrets. Do not send them to GitHub issues or ask the human to paste them into an LLM chat. A loopback Signal HTTP API may still be available to other local processes; separate Unix ownership of its files alone does not protect the API.

## Identity and containment

Hermes profiles separate configuration and state; under the same Unix identity they do not provide an OS security boundary. Use distinct Unix users/VMs/brokers for genuinely different trust principals. Give the model only the specific capabilities needed. In-process approvals and prompt instructions are useful but not independent authorization enforcement.

The server reference includes multiple integration patterns, not a claim that all legacy broad credentials have been removed. For a new installation, default to no sudo, no Docker socket, no hypervisor key, no broad home-automation token and no edge-management credential. Inspect actual identities, groups, writable paths, listeners and effective network access before describing isolation as established.

## Optional extras after base acceptance

Add one at a time: consistent agent-state backups, browser automation, document/OCR tools, STT/TTS, knowledge retrieval, task tools, read-only home automation, mail archive, cost reporting and coding workers. Each introduces its own data, cost and effect boundary. A tool being installed does not prove configuration, authentication, permission or end-to-end usability.

See [upstream references](references.md) for version-sensitive documentation and [context workflow](repository-context.md) for keeping the agent on track.

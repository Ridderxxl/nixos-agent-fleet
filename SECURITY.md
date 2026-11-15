# Security and privacy contract

This project publishes architecture, not infrastructure access. It includes no credentials, secret ciphertext, actual addresses, original VM names, real usernames, hardware IDs, private repository links, runtime databases or private logs. Do not submit those in issues or pull requests.

## Threat model

Assume the model may be manipulated by untrusted web pages, mail, messages, documents or repositories. Assume an external-service process could be compromised. A model should plan within capabilities granted by independent software/OS/network boundaries, not decide its own authority. Prompt rules, in-process approvals and model reviewers are useful defense in depth, not independent enforcement.

The recommended boundary is per-person/service identities, narrow brokers, explicit out-of-band approval for sensitive effects, deny-by-default network policy and protected audit evidence. This is a design target; it is not a blanket assertion about the source fleet's current hardening.

Separate app runtime secrets from operator/bootstrap credentials. Give edge roles distinct decryption identities. At-rest encryption does not hide a secret from a process authorized to consume it. Per-service provider keys and spending controls are needed where shared billing would increase blast radius.

No public browser debugging endpoint, hypervisor management interface, unauthenticated dashboard, arbitrary remote-shell broker, shared root credential or bulk private-data mount should be introduced for convenience. A VPN membership is not blanket trust. Test both positive and negative access after any policy change.

## Public contribution gate

Build public material in a fresh tree using an explicit allowlist. Review paths, full contents, URL/email/IP literals, generated artifacts, commit metadata and history before publication. Do not rely on `.gitignore`, secret scanning or ciphertext alone as privacy proof. The validator is a limited regression guard, not a complete security scanner.

Use neutral roles and reserved example domains in new examples. Do not add a mapping back to private hostnames. Keep session exports, screenshots, QR codes, account identifiers, phone numbers, encrypted secret files, auth stores and logs out of this repository.

## Reporting a problem

For a public documentation error, open an issue with a minimal fictional reproduction. For suspected secret or personal-data exposure, do not repeat it in a public issue. Use GitHub private vulnerability reporting if enabled, otherwise contact the maintainer through an already-established private channel. Do not send credentials as evidence. The affected operator must revoke exposed credentials; deleting a public commit is not revocation.

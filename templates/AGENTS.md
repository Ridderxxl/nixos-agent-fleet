# Private fleet agent rules — adapt before use

Status: TEMPLATE. TODO fields must be resolved by the operator; absence is not approval.

## Reading order

Read this file, the private inventory, architecture, relevant decision records and exact role runbook. TODO: record their actual paths. Establish checkout remote/branch/commit/dirty state, execution account and active profile before editing.

## Invariants

Use neutral role names in exported public material. Keep actual hosts and identifiers in private inventory only. Do not infer runtime health from configuration. Preserve unrelated work and data. Implement lasting infrastructure changes declaratively. Never disclose secret values or full logs containing personal data.

## Permission contract

Source edits and read-only inspection are separate from publication, merge, activation, access-policy changes, migrations, deletion and secret rotation. Obtain explicit approval for the latter as required by the operator. TODO: document the precise preapproved read/edit scope and human privilege boundaries. Do not grant yourself missing access.

Treat models as planners. Use named identities, scoped tools and independently enforced approval for sensitive effects. No prompt can authorize access denied by the operator.

## Checks and delivery

TODO: enter exact validated syntax/evaluation, test and affected-host build commands here. Do not execute placeholder commands. Bound build concurrency and storage; preserve a recovery console before access changes. Record proposed, committed, merged, built, activated and accepted revisions separately.

Completion requires actual command results and user-workflow acceptance at the approved scope. If blocked, preserve the artifact and state the exact boundary. Hand off using the task template without private credentials or unrelated transcripts.

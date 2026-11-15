# Contributing

1. Read AGENTS.md, docs/provenance.md and SECURITY.md.
2. Use a focused branch and pull request; preserve unrelated edits.
3. Keep this a sanitized explanatory reference. Do not import an operational repository or promise an untested deployable example.
4. Update fleet.json and docs/services.md together when capability evidence changes. An enabled source option does not justify a live-health claim.
5. Run `python3 tools/validate.py` and report actual results. Validate any new executable artifact with real execution and describe exactly what it proves.
6. Keep version-sensitive behavior linked to upstream primary documentation. Avoid invented CLI flags or configuration keys.
7. Use generic contributor commit metadata when publishing generalized material; inspect the exact staged tree and history.
8. Do not add workflows with write tokens, self-hosted runners or production deployment access. The documentation check needs only repository read access and Python's standard library.

There are no package dependencies or application runtime to audit in this documentation-only repository. Any future executable deployment implementation needs its own pinned dependencies, builds, integration tests, permission model, migration/recovery plan and operator approval.

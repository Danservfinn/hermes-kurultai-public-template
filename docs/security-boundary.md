# Security and privacy boundary

This public template is designed to be safe to clone, fork, and discuss publicly.

## Public

- Templates, schemas, docs, runbooks, sanitized manifests, and tests.

## Private

- Secrets, OAuth files, cookies, local DBs, raw transcripts, private Brain pages, customer/payment data, exact delivery targets, session histories, private identity/memory, production credentials.

## If a leak is detected

1. Stop pushing.
2. Rotate affected credentials if exposure is plausible.
3. Rewrite unpublished commits locally.
4. If already public, treat history as compromised and rotate; force-push only after a deliberate remediation plan.

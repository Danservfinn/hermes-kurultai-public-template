# Tool policy

Default posture for a replica:

- Local/file/git/read-only research tools are allowed after review.
- Shell commands run in Docker or another approved sandbox by default.
- Browser/computer-use, messaging gateways, cron delivery, payments, deploys, and MCP servers are opt-in.
- Secrets live in a secret manager or ignored local env files, never in Git.
- Production deploys, payment actions, hard deletes, security changes, and public incident statements remain explicit-approval gates.

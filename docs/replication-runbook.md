# Replication runbook

1. Install Hermes Agent on the target machine.
2. Clone this repo.
3. Run bootstrap in dry-run mode.
4. Run bootstrap for a new, separate Hermes home.
5. Add local secrets through a secret manager or ignored `.env`.
6. Enable tools one surface at a time: terminal, git, Brain, Kanban, cron, messaging, MCP.
7. Run `python3 tests/validate_repo.py` and `hermes doctor`.
8. Create a first local Brain page and verify search/indexing.
9. Enable cron only after delivery targets are local and confirmed.
10. Keep production deploy, payment, security, hard-delete, and public-statement gates explicit.

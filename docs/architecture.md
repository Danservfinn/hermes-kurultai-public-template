# Architecture

The replicated setup has five layers:

1. **Hermes runtime** — CLI/TUI, providers, toolsets, approvals, context governance, security redaction.
2. **Profiles** — independent Hermes homes/profiles with role-specific instructions and tool scopes.
3. **Coordination** — Kanban tasks, parent dependencies, completion notes, and review gates.
4. **Continuity** — cron jobs, canaries, dashboards, receipts, and recovery/proposal packets.
5. **Brain** — local wiki memory with raw-source capture, synthesis pages, private tiers, and indexes.

The public repo contains deterministic templates and manifests. Live state is supplied locally.

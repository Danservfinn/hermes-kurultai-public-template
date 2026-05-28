#!/usr/bin/env bash
set -euo pipefail
HERMES_HOME="${HOME}/.hermes-replica"
BRAIN_ROOT="${HOME}/brain-replica"
DRY_RUN=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --home) HERMES_HOME="$2"; shift 2 ;;
    --brain) BRAIN_ROOT="$2"; shift 2 ;;
    --dry-run) DRY_RUN=1; shift ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
done
run() { if [[ "$DRY_RUN" == "1" ]]; then printf '[dry-run] %q ' "$@"; printf '
'; else "$@"; fi; }
write_file() { local target="$1" src="$2"; run mkdir -p "$(dirname "$target")"; if [[ "$DRY_RUN" == "1" ]]; then echo "[dry-run] copy $src -> $target"; else cp "$src" "$target"; fi; }
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
echo "Hermes home: $HERMES_HOME"
echo "Brain root : $BRAIN_ROOT"
run mkdir -p "$HERMES_HOME" "$HERMES_HOME/profiles" "$HERMES_HOME/skills" "$BRAIN_ROOT" "$BRAIN_ROOT"/{entities,projects,infrastructure,concepts,analyses,docs/plans,raw/assets}
write_file "$HERMES_HOME/config.yaml" "$ROOT/config/config.template.yaml"
write_file "$BRAIN_ROOT/AGENTS.md" "$ROOT/brain/AGENTS.md"
write_file "$BRAIN_ROOT/home.md" "$ROOT/brain/templates/page.md"
touch_target="$BRAIN_ROOT/index.md"
if [[ "$DRY_RUN" == "1" ]]; then echo "[dry-run] create $touch_target"; else [[ -e "$touch_target" ]] || printf '# Brain Index
' > "$touch_target"; fi
echo "Done. Add local secrets outside git, then run: hermes doctor"

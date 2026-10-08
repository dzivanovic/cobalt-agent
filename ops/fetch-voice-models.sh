set -e
exec uv run --project "$(dirname "$0")/.." python "$(dirname "$0")/fetch_voice_models.py" "$@"

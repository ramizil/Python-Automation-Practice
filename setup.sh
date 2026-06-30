#!/usr/bin/env bash
# Cross-platform (macOS / Linux) setup for both stacks.
# Usage:  bash setup.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Pick a Python 3 interpreter.
PY="$(command -v python3 || command -v python)"
if [ -z "${PY}" ]; then
  echo "ERROR: Python 3.10+ not found. Install it and re-run." >&2
  exit 1
fi

echo "==> Python stack"
cd "${ROOT}/python-playwright"
"${PY}" -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install chromium
deactivate

echo "==> TypeScript stack"
cd "${ROOT}/ts-playwright"
npm install
npx playwright install chromium

echo ""
echo "Setup complete."
echo "  Python : cd python-playwright && source .venv/bin/activate && pytest"
echo "  TS     : cd ts-playwright && npx playwright test"

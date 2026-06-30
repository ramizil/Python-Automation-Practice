#!/usr/bin/env bash
# Cross-platform (macOS / Linux) setup for both stacks.
# Installs Node.js automatically if it's missing. Usage:  bash setup.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

ensure_node() {
  if command -v npm >/dev/null 2>&1; then return 0; fi
  echo "==> Node.js not found - installing it"
  if [ "$(uname)" = "Darwin" ]; then
    if command -v brew >/dev/null 2>&1; then
      brew install node
    else
      echo "Homebrew not found. Install it (https://brew.sh) or Node.js (https://nodejs.org), then re-run." >&2
      return 1
    fi
  else
    if command -v apt-get >/dev/null 2>&1; then
      sudo apt-get update && sudo apt-get install -y nodejs npm
    elif command -v dnf >/dev/null 2>&1; then
      sudo dnf install -y nodejs
    else
      echo "No supported package manager. Install Node.js 18+ from https://nodejs.org, then re-run." >&2
      return 1
    fi
  fi
  command -v npm >/dev/null 2>&1
}

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
if ensure_node; then
  cd "${ROOT}/ts-playwright"
  npm install
  npx playwright install chromium
else
  echo "Skipping TypeScript stack (Node.js unavailable)."
fi

echo ""
echo "Setup complete."
echo "  Python : cd python-playwright && source .venv/bin/activate && pytest"
echo "  TS     : cd ts-playwright && npx playwright test"

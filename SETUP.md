# Setup & installation (Windows / macOS / Linux)

This repo runs on any OS. You need **Git**, **Python 3.10+**, and **Node.js 18+**
(tested with Python 3.13 and Node 22). Each stack installs its own dependencies
and its own Playwright browser binaries.

## 1. Prerequisites

### Windows
- Git: https://git-scm.com/download/win
- Python 3.10+: https://www.python.org/downloads/ (tick **"Add python.exe to PATH"**)
- Node.js LTS: https://nodejs.org/

### macOS (Homebrew recommended)
```bash
brew install git python node
```
(Or download from python.org / nodejs.org.)

### Linux (Debian/Ubuntu)
```bash
sudo apt update && sudo apt install -y git python3 python3-venv python3-pip
# Node.js LTS via nodesource or your distro's package manager
```

Verify:
```bash
git --version
python --version    # or python3 --version  (>= 3.10)
node --version      # >= 18
npm --version
```

## 2. One-command setup

From the repo root:

- **Windows (PowerShell):** `./setup.ps1`
- **macOS / Linux:** `bash setup.sh`

Each script sets up **both** stacks: creates the Python venv + installs
`requirements.txt`, runs `npm install`, and downloads the Chromium browser for
each stack.

## 3. Manual setup (if you prefer)

### Python stack
```bash
cd python-playwright
python -m venv .venv                  # use python3 on macOS/Linux
# activate:
source .venv/bin/activate             # macOS/Linux
.\.venv\Scripts\Activate.ps1          # Windows PowerShell
pip install -r requirements.txt
playwright install chromium           # or: playwright install  (all browsers)
```

### TypeScript stack
```bash
cd ts-playwright
npm install
npx playwright install chromium       # or: npx playwright install
```

## 4. Run the suites

```bash
# Python  (from python-playwright/, venv activated)
pytest

# TypeScript  (from ts-playwright/)
npx playwright test
```

Expected: **14 reference tests pass per stack** (4 API + 10 UI). See each stack's
`README.md` for running individual tests and the exercises.

## 5. Notes for restricted / corporate networks

- **TLS-inspection proxy** ("self-signed certificate in chain"): both stacks
  default `IGNORE_HTTPS_ERRORS` ON, so tests run anyway. To enforce real
  certificate checks (recommended off-corp): set `IGNORE_HTTPS_ERRORS=false`.
- **Linux CI / containers** may need system libs for the browser:
  `npx playwright install --with-deps` (TS) or
  `playwright install --with-deps` (Python).
- **pip / npm behind a proxy**: if installs fail, configure your proxy
  (`pip config set global.proxy ...`, `npm config set proxy ...`) or your org's
  package mirror.

## 6. Versions are pinned

- Python deps are pinned in `python-playwright/requirements.txt`.
- Node deps are ranged in `ts-playwright/package.json`; run `npm ci` instead of
  `npm install` to install exactly from `package-lock.json` on a fresh machine.

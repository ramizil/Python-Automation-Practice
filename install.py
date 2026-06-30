#!/usr/bin/env python3
"""One-command, cross-platform installer for both stacks (Windows / macOS / Linux).

Run from the repo root with any Python 3.10+:

    python install.py          # Windows
    python3 install.py         # macOS / Linux

It sets up:
  * Node.js (LTS)      : installed automatically if missing (see ensure_node)
  * python-playwright/ : a .venv + requirements (pytest, playwright, ...) + Chromium
  * ts-playwright/     : npm install + Chromium

Options:
    --python-only   set up only the Python stack
    --ts-only       set up only the TypeScript stack
    --all-browsers  install every Playwright browser (not just Chromium)
    --skip-node     don't try to auto-install Node.js (skip TS stack if missing)
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PY_DIR = ROOT / "python-playwright"
TS_DIR = ROOT / "ts-playwright"
IS_WIN = os.name == "nt"
MIN_PY = (3, 10)


def info(msg: str) -> None:
    print(f"\n\033[1;36m==> {msg}\033[0m" if not IS_WIN else f"\n==> {msg}")


def run(cmd: list[str], cwd: Path | None = None) -> None:
    print(f"  $ {' '.join(cmd)}")
    subprocess.run(cmd, cwd=str(cwd) if cwd else None, check=True)


def venv_python(venv: Path) -> Path:
    return venv / ("Scripts/python.exe" if IS_WIN else "bin/python")


def setup_python(all_browsers: bool) -> None:
    info("Python stack")
    if sys.version_info < MIN_PY:
        sys.exit(f"ERROR: Python {MIN_PY[0]}.{MIN_PY[1]}+ required, found {sys.version.split()[0]}")

    venv = PY_DIR / ".venv"
    if not venv.exists():
        run([sys.executable, "-m", "venv", str(venv)])
    py = str(venv_python(venv))
    run([py, "-m", "pip", "install", "--upgrade", "pip"])
    run([py, "-m", "pip", "install", "-r", "requirements.txt"], cwd=PY_DIR)
    run([py, "-m", "playwright", "install"] + ([] if all_browsers else ["chromium"]), cwd=PY_DIR)


def _refresh_node_path() -> None:
    # A freshly installed Node may not be on PATH in the current process yet.
    if IS_WIN:
        node_dir = Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "nodejs"
        if (node_dir / "npm.cmd").exists():
            os.environ["PATH"] = str(node_dir) + os.pathsep + os.environ.get("PATH", "")
    else:
        for d in ("/usr/local/bin", "/opt/homebrew/bin", "/usr/bin"):
            if Path(d, "npm").exists() and d not in os.environ.get("PATH", ""):
                os.environ["PATH"] = d + os.pathsep + os.environ.get("PATH", "")


def ensure_node(*, auto: bool) -> bool:
    """Make sure Node.js/npm is available, installing the LTS if missing."""
    if shutil.which("npm") and shutil.which("npx"):
        return True
    if not auto:
        print("  Node.js/npm not found and --skip-node set - skipping TypeScript stack.")
        return False

    info("Node.js not found - installing the LTS")
    try:
        if IS_WIN:
            if shutil.which("winget"):
                run([
                    "winget", "install", "-e", "--id", "OpenJS.NodeJS.LTS", "--silent",
                    "--accept-package-agreements", "--accept-source-agreements",
                ])
            elif shutil.which("choco"):
                run(["choco", "install", "nodejs-lts", "-y"])
            else:
                print("  No winget/choco found. Install Node.js 18+ from https://nodejs.org and re-run.")
                return False
        elif sys.platform == "darwin":
            if shutil.which("brew"):
                run(["brew", "install", "node"])
            else:
                print("  Homebrew not found. Install it (https://brew.sh) or Node.js (https://nodejs.org), then re-run.")
                return False
        else:  # Linux
            if shutil.which("apt-get"):
                run(["sudo", "apt-get", "update"])
                run(["sudo", "apt-get", "install", "-y", "nodejs", "npm"])
            elif shutil.which("dnf"):
                run(["sudo", "dnf", "install", "-y", "nodejs"])
            else:
                print("  No supported package manager. Install Node.js 18+ from https://nodejs.org and re-run.")
                return False
    except subprocess.CalledProcessError:
        print("  Automatic Node.js install failed. Install it from https://nodejs.org and re-run.")
        return False

    _refresh_node_path()
    if shutil.which("npm") and shutil.which("npx"):
        return True
    print("  Node.js was installed but isn't on PATH in this shell yet.")
    print("  Open a NEW terminal and re-run:  python install.py --ts-only")
    return False


def setup_ts(all_browsers: bool, *, auto_node: bool) -> None:
    info("TypeScript stack")
    if not ensure_node(auto=auto_node):
        return
    npm = shutil.which("npm")
    npx = shutil.which("npx")
    assert npm and npx  # guaranteed by ensure_node
    run([npm, "install"], cwd=TS_DIR)
    run([npx, "playwright", "install"] + ([] if all_browsers else ["chromium"]), cwd=TS_DIR)


def main() -> None:
    ap = argparse.ArgumentParser(description="Install both Playwright practice stacks.")
    ap.add_argument("--python-only", action="store_true")
    ap.add_argument("--ts-only", action="store_true")
    ap.add_argument("--all-browsers", action="store_true")
    ap.add_argument("--skip-node", action="store_true")
    args = ap.parse_args()

    do_py = not args.ts_only
    do_ts = not args.python_only

    try:
        if do_py:
            setup_python(args.all_browsers)
        if do_ts:
            setup_ts(args.all_browsers, auto_node=not args.skip_node)
    except subprocess.CalledProcessError as exc:
        sys.exit(f"\nInstall step failed (exit {exc.returncode}). See the output above.")

    info("Setup complete")
    if do_py:
        act = ".venv\\Scripts\\Activate.ps1" if IS_WIN else "source .venv/bin/activate"
        print(f"  Python : cd python-playwright && {act} && pytest")
    if do_ts:
        print("  TS     : cd ts-playwright && npx playwright test")


if __name__ == "__main__":
    main()

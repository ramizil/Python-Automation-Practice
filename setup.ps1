# Cross-platform (Windows PowerShell) setup for both stacks.
# Usage:  ./setup.ps1
$ErrorActionPreference = "Stop"
$root = $PSScriptRoot

Write-Host "==> Python stack"
Push-Location (Join-Path $root "python-playwright")
python -m venv .venv
& ".\.venv\Scripts\python.exe" -m pip install --upgrade pip
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
& ".\.venv\Scripts\python.exe" -m playwright install chromium
Pop-Location

Write-Host "==> TypeScript stack"
Push-Location (Join-Path $root "ts-playwright")
npm install
npx playwright install chromium
Pop-Location

Write-Host ""
Write-Host "Setup complete."
Write-Host "  Python : cd python-playwright; .\.venv\Scripts\Activate.ps1; pytest"
Write-Host "  TS     : cd ts-playwright; npx playwright test"

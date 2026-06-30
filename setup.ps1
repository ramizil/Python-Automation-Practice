# Cross-platform (Windows PowerShell) setup for both stacks.
# Installs Node.js (LTS) automatically if it's missing. Usage:  ./setup.ps1
$ErrorActionPreference = "Stop"
$root = $PSScriptRoot

function Ensure-Node {
    if (Get-Command npm -ErrorAction SilentlyContinue) { return $true }
    Write-Host "==> Node.js not found - installing the LTS"
    if (Get-Command winget -ErrorAction SilentlyContinue) {
        winget install -e --id OpenJS.NodeJS.LTS --silent `
            --accept-package-agreements --accept-source-agreements
    } elseif (Get-Command choco -ErrorAction SilentlyContinue) {
        choco install nodejs-lts -y
    } else {
        Write-Host "No winget/choco found. Install Node.js 18+ from https://nodejs.org and re-run."
        return $false
    }
    # Refresh PATH for the current session so npm is usable right away.
    $nodeDir = Join-Path $env:ProgramFiles "nodejs"
    if (Test-Path (Join-Path $nodeDir "npm.cmd")) { $env:Path = "$nodeDir;$env:Path" }
    if (Get-Command npm -ErrorAction SilentlyContinue) { return $true }
    Write-Host "Node.js installed but not on PATH in this shell. Open a NEW terminal and re-run ./setup.ps1"
    return $false
}

Write-Host "==> Python stack"
Push-Location (Join-Path $root "python-playwright")
python -m venv .venv
& ".\.venv\Scripts\python.exe" -m pip install --upgrade pip
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
& ".\.venv\Scripts\python.exe" -m playwright install chromium
Pop-Location

Write-Host "==> TypeScript stack"
if (Ensure-Node) {
    Push-Location (Join-Path $root "ts-playwright")
    npm install
    npx playwright install chromium
    Pop-Location
} else {
    Write-Host "Skipping TypeScript stack (Node.js unavailable)."
}

Write-Host ""
Write-Host "Setup complete."
Write-Host "  Python : cd python-playwright; .\.venv\Scripts\Activate.ps1; pytest"
Write-Host "  TS     : cd ts-playwright; npx playwright test"

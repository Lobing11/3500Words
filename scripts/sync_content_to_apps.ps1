$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$curated = Join-Path $root "content\curated"
$android = Join-Path $root "android\app\src\main\assets\content"
$harmony = Join-Path $root "harmony\entry\src\main\resources\rawfile\content"

function Sync-Curated([string]$dest) {
    if (Test-Path $dest) {
        Get-ChildItem -Path $dest -File | Remove-Item -Force
    }
    New-Item -ItemType Directory -Force -Path $dest | Out-Null
    Copy-Item -Force (Join-Path $curated "*") $dest
}

Sync-Curated $android
Sync-Curated $harmony

Write-Host "Synced curated -> android assets & harmony rawfile"
Get-ChildItem $android | Select-Object Name

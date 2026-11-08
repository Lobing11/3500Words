$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$curated = Join-Path $root "content\curated"
$android = Join-Path $root "android\app\src\main\assets\content"
$harmony = Join-Path $root "harmony\entry\src\main\resources\rawfile\content"

New-Item -ItemType Directory -Force -Path $android | Out-Null
New-Item -ItemType Directory -Force -Path $harmony | Out-Null

Copy-Item -Force (Join-Path $curated "*") $android
Copy-Item -Force (Join-Path $curated "*") $harmony

Write-Host "Synced curated -> android assets & harmony rawfile"
Get-ChildItem $android | Select-Object Name

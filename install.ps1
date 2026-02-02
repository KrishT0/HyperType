# ============================================================
#   HyperType - Windows Installer (PowerShell)
#   Usage:
#     powershell -Command "Invoke-WebRequest -Uri https://raw.githubusercontent.com/yourusername/hypertype/main/install.ps1 -OutFile install.ps1; .\install.ps1; Remove-Item install.ps1"
# ============================================================

$REPO = "yourusername/hypertype"
$INSTALL_DIR = "$env:LOCALAPPDATA\Programs\hypertype"
$BINARY_NAME = "hypertype.exe"
$DOWNLOAD_URL = "https://github.com/$REPO/releases/latest/download/hypertype-windows.exe"
$FINAL_PATH = Join-Path $INSTALL_DIR $BINARY_NAME

# ============================================================
#   Welcome
# ============================================================
Write-Host "============================================"
Write-Host "  Installing HyperType for Windows..."
Write-Host "============================================"
Write-Host

# ============================================================
#   Step 1: Create directory
# ============================================================
Write-Host "  [1/3] Creating install directory..."
if (-not (Test-Path $INSTALL_DIR)) {
    New-Item -ItemType Directory -Path $INSTALL_DIR -Force | Out-Null
}
Write-Host "        Done!"

# ============================================================
#   Step 2: Download
# ============================================================
Write-Host "  [2/3] Downloading..."
try {
    Invoke-WebRequest -Uri $DOWNLOAD_URL -OutFile $FINAL_PATH -ErrorAction Stop
} catch {
    Write-Host "  ERROR: Download failed. Check your internet connection."
    exit 1
}

if (-not (Test-Path $FINAL_PATH)) {
    Write-Host "  ERROR: Download failed."
    exit 1
}
Write-Host "        Done!"

# ============================================================
#   Step 3: Add to PATH
# ============================================================
Write-Host "  [3/3] Adding to PATH..."
$currentPath = [System.Environment]::GetEnvironmentVariable('Path', 'User')

if ($currentPath -notlike "*$INSTALL_DIR*") {
    $newPath = "$currentPath;$INSTALL_DIR"
    [System.Environment]::SetEnvironmentVariable('Path', $newPath, 'User')
    Write-Host "        Added to PATH!"
} else {
    Write-Host "        Already in PATH."
}

# ============================================================
#   Success
# ============================================================
Write-Host
Write-Host "============================================"
Write-Host "  HyperType installed successfully!"
Write-Host "============================================"
Write-Host
Write-Host "  Open a NEW terminal and run:"
Write-Host "    hypertype            - Welcome screen"
Write-Host "    hypertype start 30   - Start a 30s test"
Write-Host "    hypertype stats      - View your stats"
Write-Host
Write-Host "============================================"

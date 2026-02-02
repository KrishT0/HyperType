#!/bin/bash
# ============================================================
#   HyperType - Linux/macOS Installer
#   Usage:
#     curl -sSL https://raw.githubusercontent.com/yourusername/hypertype/main/install.sh | bash
# ============================================================

set -e

REPO="yourusername/hypertype"
INSTALL_DIR="/usr/local/bin"
BINARY_NAME="hypertype"

# ============================================================
#   Detect OS
# ============================================================
OS_TYPE=$(uname -s)
case "$OS_TYPE" in
    Linux*)
        PLATFORM="Linux"
        DOWNLOAD_NAME="hypertype-linux"
        ;;
    Darwin*)
        PLATFORM="macOS"
        DOWNLOAD_NAME="hypertype-mac"
        ;;
    *)
        echo "ERROR: Unsupported OS: $OS_TYPE"
        exit 1
        ;;
esac

DOWNLOAD_URL="https://github.com/$REPO/releases/latest/download/$DOWNLOAD_NAME"

# ============================================================
#   Welcome
# ============================================================
echo "============================================"
echo "  Installing HyperType for $PLATFORM..."
echo "============================================"
echo

# ============================================================
#   Check sudo
# ============================================================
if [ "$(id -u)" -ne 0 ]; then
    echo "  Sudo access is required. You may be prompted for your password."
    SUDO="sudo"
else
    SUDO=""
fi

# ============================================================
#   Download
# ============================================================
echo "  [1/3] Downloading..."
$SUDO curl -sSL -o "$INSTALL_DIR/$BINARY_NAME" "$DOWNLOAD_URL"

if [ ! -f "$INSTALL_DIR/$BINARY_NAME" ]; then
    echo "  ERROR: Download failed. Check your internet connection."
    exit 1
fi
echo "        Done!"

# ============================================================
#   Make executable
# ============================================================
echo "  [2/3] Setting permissions..."
$SUDO chmod +x "$INSTALL_DIR/$BINARY_NAME"
echo "        Done!"

# ============================================================
#   Linux: Add to input group for keyboard access
# ============================================================
if [ "$PLATFORM" = "Linux" ]; then
    CURRENT_USER=$(whoami)
    if ! groups "$CURRENT_USER" | grep -q "input"; then
        echo "  [3/3] Adding keyboard permissions..."
        $SUDO usermod -aG input "$CURRENT_USER"
        echo "        Done! Please log out and back in for keyboard access."
    else
        echo "  [3/3] Keyboard permissions already set."
    fi
else
    echo "  [3/3] Finalizing..."
    echo "        Done!"
fi

# ============================================================
#   Success
# ============================================================
echo
echo "============================================"
echo "  HyperType installed successfully!"
echo "============================================"
echo
echo "  Run these commands:"
echo "    hypertype            - Welcome screen"
echo "    hypertype start 30   - Start a 30s test"
echo "    hypertype stats      - View your stats"
echo
echo "============================================"

# HyperType ⌨️
A fast, lightweight typing speed test tool built for your terminal.

Practice daily. Improve speed. Boost accuracy.

---

## ⬇️ Install

### Windows (PowerShell)
```powershell
powershell -Command "Invoke-WebRequest -Uri https://raw.githubusercontent.com/KrishT0/hypertype/main/install.ps1 -OutFile install.ps1; .\install.ps1; Remove-Item install.ps1"
```

### Linux / macOS
```bash
curl -sSL https://raw.githubusercontent.com/KrishT0/hypertype/main/install.sh | bash
```

> Open a **new terminal** after installing and run `hypertype`.

---

## 🗑️ Uninstall

### Windows (PowerShell)
```powershell
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Programs\hypertype"
$currentPath = [System.Environment]::GetEnvironmentVariable('Path', 'User')
$newPath = ($currentPath -split ';') | Where-Object { $_ -notlike '*\Programs\hypertype*' } | Join-String -Separator ';'
[System.Environment]::SetEnvironmentVariable('Path', $newPath, 'User')
```

### Linux / macOS
```bash
sudo rm /usr/local/bin/hypertype
```

---

## 💻 Usage

### Welcome Screen
```bash
hypertype
```

### Start a Typing Test
```bash
hypertype start 15   # 15 second test
hypertype start 30   # 30 second test
hypertype start 60   # 60 second test
```

### View Your Stats
```bash
hypertype stats
```

---

## 🎮 How to Play

1. Run `hypertype start <mode>` (15, 30, or 60)
2. Words will appear on screen
3. Start typing — the timer begins on your first keypress
4. Text will turn:
   - 🟢 **Green** — correct character
   - 🔴 **Red** — incorrect character
   - ⬜ **Dim** — not yet typed
5. Press `Backspace` to fix mistakes
6. Press `ESC` to quit early
7. Results (WPM + Accuracy) are shown and saved automatically

---

## ⚠️ Compatibility

This tool will **not work** in the following environments:

- **SSH sessions** without X forwarding
- **Headless servers**
- **Some terminal emulators**
- **WSL** without X11 configured

Make sure you have a terminal with full interactive keyboard input support and display capabilities.

---

## 📊 Results & Storage

After every test, your results are saved automatically.

| OS | Storage Location |
|----|-----------------|
| Windows | `C:\Users\YourUsername\.hypertype\results.json` |
| Linux / macOS | `/home/yourusername/.hypertype/results.json` |

---

## 🚀 Install From Source

If you want to run the source code directly instead of using the installer:

### Windows
```bash
git clone https://github.com/KrishT0/hypertype.git
cd hypertype
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### Linux / macOS
```bash
git clone https://github.com/KrishT0/hypertype.git
cd hypertype
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

---

## 🏗️ Build From Source

```bash
pip install pyinstaller
pyinstaller hypertype.spec
# Output will be in dist/
```

---

## 🔄 CI/CD

This project uses **GitHub Actions** to automatically build executables for all platforms.

```
Trigger workflow from Actions tab
        ↓
Builds run in parallel on 3 OS
        ↓
┌─────────────────────────────────────┐
│  Windows  →  hypertype-windows.exe  │
│  Linux    →  hypertype-linux        │
│  macOS    →  hypertype-mac          │
└─────────────────────────────────────┘
        ↓
All binaries attached to release
```

---

## 📁 Project Structure

```
hypertype/
├── .github/
│   └── workflows/
│       └── build.yml            # GitHub Actions CI/CD pipeline
├── .gitignore                   # Ignores build files, venv, etc.
├── install.sh                   # Linux/macOS installer
├── install.ps1                  # Windows installer (PowerShell)
├── main.py                      # CLI entry point (Typer)
├── screen.py                    # Typing screen + live rendering + results
├── storage.py                   # Save/load results from JSON
├── utils.py                     # Word generation utility
├── hypertype.spec               # PyInstaller build config
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Typer](https://typer.tiangolo.com/) | CLI framework |
| [Rich](https://github.com/Textualize/rich) | Terminal UI & live rendering |
| [pynput](https://pypi.org/project/pynput/) | Keyboard input capture |
| [PyInstaller](https://www.pyinstaller.org/) | Builds standalone executables |
| [GitHub Actions](https://github.com/features/actions) | Automated CI/CD builds |

---

## 📝 License

This project is licensed under the MIT License.
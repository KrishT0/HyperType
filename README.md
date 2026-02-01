# HyperType ⌨️
A fast, lightweight typing speed test tool built for your terminal.

Practice daily. Improve speed. Boost accuracy.

---

## ⬇️ Download

Don't want to install Python? Download the pre-built binary for your OS:

| OS | Download |
|----|----------|
| Windows | [hypertype-windows.exe](../../releases/latest/download/hypertype-windows.exe) |
| Linux | [hypertype-linux](../../releases/latest/download/hypertype-linux) |
| macOS | [hypertype-mac](../../releases/latest/download/hypertype-mac) |

> **Linux/Mac:** You may need to give execute permission after downloading:
> ```bash
> chmod +x hypertype-linux
> ./hypertype-linux
> ```

---

## 📦 Requirements

- Python 3.8 or higher
- pip (comes with Python)

---

## 🚀 Installation (From Source)

### Windows

```bash
# 1. Clone the repository
git clone https://github.com/KrishT0/hypertype.git
cd hypertype

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt
```

### Linux / macOS

```bash
# 1. Clone the repository
git clone https://github.com/KrishT0/hypertype.git
cd hypertype

# 2. Create a virtual environment
python3 -m venv venv

# 3. Activate the virtual environment
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt
```

> **Linux Note:** If you encounter a permission error with keyboard input, run:
> ```bash
> sudo usermod -aG input your_username
> ```
> Then log out and back in.

---

## 💻 Usage

### Welcome Screen
```bash
hypertype
```

### Start a Typing Test
```bash
# 15 second test
hypertype start 15

# 30 second test
hypertype start 30

# 60 second test
hypertype start 60
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

## 📊 Results & Storage

After every test, your results are saved automatically.

| OS | Storage Location |
|----|-----------------|
| Windows | `C:\Users\YourUsername\.monkeytype_terminal\results.json` |
| Linux / macOS | `/home/yourusername/.monkeytype_terminal/results.json` |

To quickly find your storage folder, you can print the path:
```python
from storage import ResultsStorage
storage = ResultsStorage()
print(storage.results_file)
```

---

## 🏗️ Build From Source

Want to build your own executable? Make sure your venv is activated and run:

```bash
# 1. Install PyInstaller
pip install pyinstaller

# 2. Build using the spec file
pyinstaller hypertype.spec

# 3. Your executable will be in the dist/ folder
dist/hypertype.exe       # Windows
dist/hypertype           # Linux / macOS
```

---

## 🔄 CI/CD — Automated Builds

This project uses **GitHub Actions** to automatically build executables for all platforms when a new release is published.

### How it works

```
You publish a new release on GitHub
        ↓
GitHub Actions triggers automatically
        ↓
Builds run in parallel on 3 OS
        ↓
┌─────────────────────────────────────┐
│  Windows  →  hypertype-windows.exe  │
│  Linux    →  hypertype-linux        │
│  macOS    →  hypertype-mac          │
└─────────────────────────────────────┘
        ↓
All binaries are attached to the release
```

### How to release

```
1. Go to your repo on GitHub
2. Click "Releases" tab
3. Click "New Release"
4. Create a tag (e.g., v1.0.0)
5. Click "Publish Release"
6. Wait a few minutes — binaries are auto-attached ✅
```

The workflow config is in `.github/workflows/build.yml`.

---

## 📁 Project Structure

```
hypertype/
├── .github/
│   └── workflows/
│       └── build.yml            # GitHub Actions CI/CD pipeline
├── .gitignore                   # Ignores build files, venv, etc.
├── main.py                      # CLI entry point (Typer)
├── screen.py                    # Typing screen + live rendering + results
├── storage.py                   # Save/load results from JSON
├── utils.py                     # Word generation utility
├── hypertype.spec               # PyInstaller build config
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

---

## 📋 Requirements.txt

```
rich
typer
pynput
```

---

## 🔧 Deactivating the Virtual Environment

When you're done, deactivate the virtual environment (same on all OS):
```bash
deactivate
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

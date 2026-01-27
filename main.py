import getpass

import typer
from rich import print

from utils import generate_words

username = getpass.getuser()
app = typer.Typer()


@app.callback(invoke_without_command=True)
def main():
    print(f"""Welcome to HyperType!, {username}
    Practice daily • Improve speed • Boost accuracy

    Features:
    - 15s / 30s / 60s typing modes
    - Real-time feedback
    - WPM + accuracy tracking
    - Daily typing exercises

    Start typing. Start improving.
""")


@app.command()
def start(mode: int):
    words = generate_words(mode)
    pass


if __name__ == "__main__":
    app()

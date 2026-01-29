import getpass

import typer

from screen import render_screen, render_stats
from storage import ResultsStorage
from utils import generate_words

username = getpass.getuser()

app = typer.Typer(
    help="HyperType is a CLI app that helps you improve your typing speed and accuracy."
)


def show_welcome():
    """Show welcome message"""
    print(f"""Welcome to HyperType!, {username}
Practice daily • Improve speed • Boost accuracy

Features:
- 15s / 30s / 60s typing modes
- Real-time feedback
- WPM + accuracy tracking
- Daily typing exercises

Start typing. Start improving.

Commands:
    hypertype start <mode>  - Start a typing test (15, 30, or 60 seconds)
    hypertype stats         - View your statistics
    """)


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    HyperType is a CLI app that helps you improve your typing speed and accuracy.
    """
    # Only show welcome if no subcommand was provided
    if ctx.invoked_subcommand is None:
        show_welcome()


@app.command()
def start(mode: int):
    """
    Start the typing game.

    Args:
        mode (int): The typing mode to start (15, 30, or 60 seconds).

    Returns:
        None
    """
    words = generate_words(mode)
    current_session_response = render_screen(words, mode)
    storage = ResultsStorage()
    storage.save_result(current_session_response)


@app.command()
def stats():
    """
    Display user's stats.
    """
    render_stats(username)


if __name__ == "__main__":
    app()

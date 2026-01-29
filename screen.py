import platform
import sys
from time import time

from pynput import keyboard
from rich.align import Align
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.padding import Padding
from rich.text import Text

from storage import ResultsStorage

console = Console()


class TypingScreen:
    def __init__(self, words: str, duration: int = 30):
        self.words = words
        self.duration = duration
        self.typed_text = ""
        self.running = True
        self.old_settings = None
        self.start_time: float = 0.0
        self.end_time: float = 0.0

    def create_display_text(self):
        """Create colored text based on what user has typed"""
        display = Text()

        for i, char in enumerate(self.words):
            if i < len(self.typed_text):
                # User has typed this character
                if self.typed_text[i] == char:
                    # Correct - show in green/normal
                    display.append(char, style="green")
                else:
                    # Incorrect - show in red
                    display.append(char, style="red bold")
            else:
                # Not yet typed - show dimmed
                display.append(char, style="dim")

        return display

    def create_layout(self, remaining: int):
        """Create the layout with current state"""
        layout = Layout()
        layout.split_column(Layout(name="main"), Layout(name="footer", size=1))

        # Create display text with colors
        display_text = self.create_display_text()
        padded_obj = Padding(display_text, (0, 5), expand=False)

        # Footer with timer
        footer_obj = Text(f"Time: {remaining}s", style="dim")

        layout["main"].update(Align.center(padded_obj, vertical="middle"))
        layout["footer"].update(Align.center(footer_obj))

        return layout

    def on_press(self, key):
        """Handle keyboard input"""
        # Handle backspace
        if key == keyboard.Key.backspace:
            if self.typed_text:
                self.typed_text = self.typed_text[:-1]
            return

        # Handle escape
        if key == keyboard.Key.esc:
            self.running = False
            return

        # Handle space
        if key == keyboard.Key.space:
            self.typed_text += " "
            return

        # Handle regular character keys
        try:
            if hasattr(key, "char") and key.char is not None:
                self.typed_text += key.char
        except AttributeError:
            pass

    def calculate_results(self):
        """Calculate WPM and Accuracy"""
        # Calculate time taken
        time_taken = self.end_time - self.start_time
        minutes = time_taken / 60

        # Calculate correct and incorrect characters
        correct_chars = 0
        incorrect_chars = 0

        min_length = min(len(self.typed_text), len(self.words))

        for i in range(min_length):
            if self.typed_text[i] == self.words[i]:
                correct_chars += 1
            else:
                incorrect_chars += 1

        # Extra characters typed (beyond the original text)
        if len(self.typed_text) > len(self.words):
            incorrect_chars += len(self.typed_text) - len(self.words)

        total_chars = len(self.typed_text)

        # Calculate accuracy (percentage of correct characters)
        accuracy = (correct_chars / total_chars * 100) if total_chars > 0 else 0

        # Calculate WPM
        # Standard: 1 word = 5 characters (including spaces)
        words_typed = correct_chars / 5
        wpm = words_typed / minutes if minutes > 0 else 0

        return {
            "wpm": round(wpm, 2),
            "accuracy": round(accuracy, 2),
            "correct_chars": correct_chars,
            "incorrect_chars": incorrect_chars,
            "total_chars": total_chars,
            "time_taken": round(time_taken, 2),
            "duration": self.duration,
        }

    def render(self):
        """Main render loop with timer and typing"""
        # Only use termios on Unix-like systems
        if platform.system() != "Windows":
            try:
                import termios
                import tty

                self.old_settings = termios.tcgetattr(sys.stdin)
                tty.setcbreak(sys.stdin.fileno())
            except:
                pass

        try:
            # Start keyboard listener with suppress=True to prevent echo
            listener = keyboard.Listener(on_press=self.on_press, suppress=True)
            listener.start()

            self.start_time = time()

            # Use Live to update without scrolling
            with Live(
                self.create_layout(self.duration),
                console=console,
                screen=True,
                refresh_per_second=10,
            ) as live:
                while self.running:
                    elapsed = time() - self.start_time
                    remaining = self.duration - int(elapsed)

                    # Check if time is up
                    if remaining <= 0:
                        self.running = False
                        break

                    # Update the live display
                    live.update(self.create_layout(remaining))

            self.end_time = time()

            # Stop listener
            listener.stop()

        finally:
            # Restore terminal settings (only on Unix-like systems)
            if platform.system() != "Windows" and self.old_settings:
                import termios

                termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)

        # Calculate results
        results = self.calculate_results()

        # Show completion message
        console.clear()
        console.print("[bold green]Time's up![/bold green]\n")
        console.print(f"[cyan]WPM:[/cyan] [bold]{results['wpm']}[/bold]")
        console.print(f"[cyan]Accuracy:[/cyan] [bold]{results['accuracy']}%[/bold]")
        console.print(
            f"[cyan]Correct Characters:[/cyan] {results['correct_chars']}/{results['total_chars']}"
        )
        console.print(f"[cyan]Time:[/cyan] {results['time_taken']}s")

        return results


def render_screen(words: str, duration: int = 30):
    """
    Render the typing test screen with timer and typing functionality.

    Args:
        words: The text to display
        duration: How long to run the test in seconds (default: 30)

    Returns:
        dict: Test results containing wpm, accuracy, etc.
    """
    screen = TypingScreen(words, duration)
    results = screen.render()
    return results


def render_stats(username):
    """
    Render the stats screen.

    Args:
        username: The username of the user

    Returns:
        None
    """
    storage = ResultsStorage()
    stats = storage.get_stats()

    if not stats:
        print("No stats found. Start typing to build history 🚀")
        return

    print(f"{username} Stats: ")
    print(f"{'Typing Sessions':<20}: {stats['total_tests']}")
    print(f"{'Average Speed':<20}: {stats['avg_wpm']} WPM")
    print(f"{'Average Accuracy':<20}: {stats['avg_accuracy']}%")
    print(f"{'Top Speed':<20}: {stats['best_wpm']}WPM")
    print(f"{'Best Accuracy':<20}: {stats['best_accuracy']}%")

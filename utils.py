import os
import random


def generate_words(word_count: int):
    """
    Generate a string of random words separated by spaces.

    Args:
        word_count (int): The number of words to generate.
    Returns:
        str: A string of random words.
    """
    random_words = [
        "python",
        "developer",
        "terminal",
        "keyboard",
        "docker",
        "react",
        "cloud",
        "system",
        "performance",
        "latency",
        "database",
        "backend",
        "frontend",
        "typescript",
        "graphql",
        "microservice",
        "distributed",
    ]
    return " ".join(random.choices(random_words, k=(word_count + 20)))


def clear_terminal():
    """
    Clear the terminal screen.
    """
    os.system("cls" if os.name == "nt" else "clear")

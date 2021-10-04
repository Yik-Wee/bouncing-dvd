import os

CLEAR_CMD = 'cls' if os.name == 'nt' else 'clear'


def clear_screen() -> None:
    os.system(CLEAR_CMD)


def make_colour(text, colour: int) -> str:
    """
    `colour: int` - ANSI 256-color extended color set colour code\n
    Returns text coloured using ANSI 256-color extended color set
    """
    return f"\033[38;5;{colour}m{text}\033[0m"

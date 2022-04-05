"""
UI for hmg-client powered by Rich
"""
import random

from rich.console import Console
from rich.columns import Columns
from rich.prompt import Prompt
from rich.panel import Panel

from hmg import __version__
from hmg.hangman import Hangman

console = Console()

random_color = ["#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])]


def draw_panel_word(board: str):
    board_panel = Panel(f"[b]{board}", expand=False)
    console.print(board_panel, justify="center")


def draw_header(**kwargs):
    turn = kwargs.get("turn", False)
    username = kwargs.get("username")
    used_chars = ",".join(kwargs.get("used_chars"))
    board = "  ".join(kwargs.get("board"))

    username_text = f"[b]Username: [{random_color[0]}]{username}"
    used_chars_text = f"[b]Used chars: [red]{used_chars}"
    version_text = f"[b]version: [italic]{__version__}"

    console.clear()
    title = "[b]HMG [red blink] Opponent's Turn"
    if turn:
        title = "[b]HMG [green blink] Your Turn"
    console.rule(title)

    header = Columns(
        [username_text, used_chars_text, version_text],
        expand=True,
        equal=True,
        align="center",
    )

    console.print(header, justify="center")
    for _ in range(3):
        console.print()

    draw_panel_word(board)


def ask_username() -> str:
    default_username = "user_xx"
    while True:
        username = Prompt.ask("[b]Ingresa tu [green]usuario")
        if username:
            return username
        return default_username


def ask_letter_or_word() -> str:
    while True:
        user_input = Prompt.ask(
            "[b]Ingresa una letra o adivina la palabra secreta"
        ).strip()
        user_input_is_valid = Hangman.letter_is_valid(user_input)
        if user_input_is_valid:
            return user_input.lower()


def final_msg(color: str, msg: str):
    console.rule(f"[b {color}]Fin del juego, {msg}")

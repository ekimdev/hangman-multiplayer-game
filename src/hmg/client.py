import pickle
import socket
import argparse

from hmg.hangman import Hangman
from hmg import ui

DEFAULT_BOARD_CHAR = "-"


class Client:
    def __init__(self, host, port, board_char):
        self.host = host
        self.port = port
        self.board_char = board_char
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self):
        self._socket.connect((self.host, self.port))

    def start_game(self):
        ui.console.clear()
        ui.console.rule(title="Hangman Multiplayer")
        username = ui.ask_username()
        ui.console.clear()
        with ui.console.status("Waiting for oponent..."):
            self._socket.send(pickle.dumps({"user": username}))
            payload = pickle.loads(self._socket.recv(1024))
            secret_word = payload["msg"]

        game = Hangman(secret_word, char_board=self.board_char)

        while True:
            with ui.console.status("Waiting for oponent..."):
                msg_server = self._socket.recv(1024)

            payload = pickle.loads(msg_server)
            turn = payload["turn"]
            game.update_dashboard(payload["msg"])
            kwargs = dict(
                turn=turn,
                username=username,
                used_chars=game.letters_used,
                board=game.board,
            )
            ui.draw_header(**kwargs)

            if payload["win"]:
                ui.console.clear()
                ui.draw_panel_word(secret_word.upper())
                ui.final_msg("red", "Perdiste...")
                break
            elif payload["turn"]:
                user_input = ui.ask_letter_or_word()
                if len(user_input) > 1:
                    if user_input == secret_word:
                        ui.console.clear()
                        ui.draw_panel_word(secret_word.upper())
                        ui.final_msg("green", "Ganaste!!")
                        self._socket.send(
                            pickle.dumps({"msg": user_input, "win": True})
                        )
                        break
                    self._socket.send(pickle.dumps({"msg": "", "win": False}))
                else:
                    game.char_is_used(user_input)
                    # FIXME: quizas la funcion debe llamarse de otra manera.
                    # ya no deberia devolver True o False.

                    if game.letter_in_the_word(user_input):
                        game.update_dashboard(user_input)

                        if game.is_completed:
                            ui.console.clear()
                            ui.draw_panel_word(secret_word.upper())
                            ui.final_msg("green", "Ganaste!!")
                            self._socket.send(
                                pickle.dumps(
                                    {"msg": user_input, "win": game.is_completed}
                                )
                            )
                            break

                        self._socket.send(
                            pickle.dumps({"msg": user_input, "win": game.is_completed})
                        )
                    else:
                        self._socket.send(
                            pickle.dumps({"msg": user_input, "win": False})
                        )


def get_cli_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--host", default=socket.gethostname())
    parser.add_argument("-p", "--port", type=int, default=8889)
    parser.add_argument(
        "-c",
        "--board-char",
        default=DEFAULT_BOARD_CHAR,
        help="Char used for fill board",
    )
    return parser


def main():
    args = get_cli_parser().parse_args()
    client = Client(
        host=args.host,
        port=args.port,
        board_char=args.board_char,
    )
    try:
        client.connect_to_server()
        client.start_game()
    except ConnectionRefusedError:
        print("Server is running?")
    except KeyboardInterrupt:
        print("Exiting...")


if __name__ == "__main__":
    main()

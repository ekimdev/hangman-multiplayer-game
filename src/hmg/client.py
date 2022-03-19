import pickle
import socket
import argparse

from hmg.hangman import Hangman
from hmg.display import draw_header


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self):
        self._socket.connect((self.host, self.port))

    def start_game(self):
        username = input("Ingresa tu nombre de usuario: ")
        self._socket.send(pickle.dumps({"user": username}))

        payload = pickle.loads(self._socket.recv(1024))
        secret_word = payload["msg"]
        game = Hangman(secret_word)

        while True:
            print("Waiting for oponent...")

            msg_server = self._socket.recv(1024)
            payload = pickle.loads(msg_server)
            game.actualizar_tablero(payload["msg"])
            draw_header(game.tablero, game.letras_usadas, 5)

            if payload["win"]:
                print("Perdiste")
                break
            elif payload["turn"]:
                user_input = game.pedir_letra()
                if len(user_input) > 1:
                    if user_input == secret_word:
                        print("Ganaste!!")
                        self._socket.send(
                            pickle.dumps({"msg": user_input, "win": True})
                        )
                        break
                    print(f"La palabra: {user_input}, no es correcta...")
                    self._socket.send(pickle.dumps({"msg": "", "win": False}))
                else:
                    game.comprobar_letras_usadas(user_input)

                    if game.letra_esta_en_la_palabra(user_input):
                        game.actualizar_tablero(user_input)
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
    parser.add_argument("-p", "--port", default=8889)
    return parser


def main():
    args = get_cli_parser().parse_args()
    client = Client(host=args.host, port=args.port)
    client.connect_to_server()
    client.start_game()


if __name__ == "__main__":
    main()

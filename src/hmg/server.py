import logging
import socket
import threading
import argparse
import pickle

from rich.console import Console
from rich.logging import RichHandler

from hmg.word_utils import get_word_from_internet


FORMAT_LOGGING = "%(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT_LOGGING, handlers=[RichHandler()])

logger = logging.getLogger("hmg-server")

MAX_PLAYERS = 2

console = Console()


class Server:
    def __init__(self, host, port, secret_word=None):
        self.host = host
        self.port = port
        self.secret_word = secret_word
        self._using_word_arg = secret_word is not None
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._players = {}

    def _update_secret_word(self):
        with console.status("[blue]Searching for word, wait..."):
            self.secret_word = get_word_from_internet()
        logger.info("Secret word=%s", self.secret_word)

    def serve_forever(self):
        self._socket.bind((self.host, self.port))
        self._socket.listen(2)
        logger.info("Server ready and listening on %s:%s", self.host, self.port)
        self._listen_connection()

    def _listen_connection(self):
        is_listening = True
        while is_listening:
            if len(self._players) == MAX_PLAYERS:
                if not self._using_word_arg:
                    self._update_secret_word()

                for _, sock in self._players.items():
                    sock.send(pickle.dumps({"msg": self.secret_word}))

                player1, player2 = self._players.values()
                payload = {"turn": False, "win": False, "msg": ""}
                player1.send(pickle.dumps(payload))
                payload = {"turn": True, "win": False, "msg": ""}
                player2.send(pickle.dumps(payload))

            conn, addr = self._socket.accept()
            incoming_message = conn.recv(1024)
            if not incoming_message:
                continue
            data = pickle.loads(incoming_message)
            username = data["user"]

            if username in self._players.keys():
                username += "_x"

            logger.info("Username=%s with address=%s connected", username, addr)
            self._players[username] = conn

            client_thread = threading.Thread(
                target=self._handle_client, args=(conn, addr, username)
            )
            client_thread.start()

    def _handle_client(self, client, addr, username):
        while True:
            logger.info("Waiting for client message...")
            msg_client = client.recv(1024)
            if not msg_client:
                logger.warning("Client=%s disconnected", username)
                del self._players[username]
                break

            data = pickle.loads(msg_client)
            logger.info("Sending data=%s", data)

            for user, sock in self._players.items():
                if user != username:
                    data["turn"] = True
                else:
                    data["turn"] = False
                sock.send(pickle.dumps(data))


def get_cli_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--host", default=socket.gethostname())
    parser.add_argument("-p", "--port", type=int, default=8889)
    parser.add_argument(
        "-w",
        "--word",
        default=None,
        help="Word to use instead of internet (usefull for testing)",
    )

    return parser


def main():
    args = get_cli_parser().parse_args()

    server = Server(host=args.host, port=args.port, secret_word=args.word)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logger.info("Exiting...")


if __name__ == "__main__":
    main()

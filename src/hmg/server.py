import socket
import threading
import argparse
import pickle


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._players = {}

    def serve_forever(self):
        self._socket.bind((self.host, self.port))
        self._socket.listen(2)
        print(f"[*] Server listening on {self.host}:{self.port}")
        self._listen_connection()

    def _listen_connection(self):
        is_listening = True
        while is_listening:
            if len(self._players) == 2:
                player1, player2 = self._players.values()
                payload = {"turn": False, "win": False, "msg": ""}
                player1.send(pickle.dumps(payload))
                payload = {"turn": True, "win": False, "msg": ""}
                player2.send(pickle.dumps(payload))

            conn, addr = self._socket.accept()
            data = pickle.loads(conn.recv(1024))
            username = data["user"]
            print(f"[*] {username}[{addr}] connected")
            self._players[username] = conn

            client_thread = threading.Thread(
                target=self._handle_client, args=(conn, addr, username)
            )
            client_thread.start()

    def _handle_client(self, client, addr, username):
        client.send(pickle.dumps({"msg": "bandera"}))

        is_online = True
        while is_online:
            print("[*] Waiting for client message...")
            msg_client = client.recv(1024)
            if not msg_client:
                print(f"[*] Client {username} disconnected")
                del self._players[username]
                is_online = False

            data = pickle.loads(msg_client)
            print(f"[*] Sending everyone {data}")

            for user, sock in self._players.items():
                if user != username:
                    data["turn"] = True
                    sock.send(pickle.dumps(data))
                else:
                    data["turn"] = False
                    sock.send(pickle.dumps(data))


def cli_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--host", default=socket.gethostname())
    parser.add_argument("-p", "--port", default=8889)

    return parser

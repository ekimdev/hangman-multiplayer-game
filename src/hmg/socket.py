import socket
import pickle


class Socket:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None

    @property
    def socket(self):
        if self._socket is None:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return self._socket

    def send(self, data):
        self._socket.send(pickle.dumps(data))

    def recv(self):
        return pickle.loads(self._socket.recv(1024))

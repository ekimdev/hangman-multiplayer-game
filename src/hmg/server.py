import socket
import threading

host = ''
port = 8001
BUFFER_SIZE = 1024
HOSTNAME = socket.gethostname()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)


def handle_connection(sock):
    """
        esta funcion maneja las conexiones de los clientes al servidor
    """
    msg = server.recv(BUFFER_SIZE)
    if not msg:
        print('Cliente desconectado')
    else:
        print(f'El cliente a enviado {msg.decode()}')


def main():
    while True:
        print('Esperando conexion...')
        sock_client, addr = server.accept()
        print(f'Cliente {addr} conectado')

        t1 = threading.Thread(target=handle_connection, args=(sock_client,))
        t1.start()


try:
    main()
except KeyboardInterrupt:
    server.shutdown(socket.SHUT_WR)
    server.close()

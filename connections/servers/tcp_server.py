import socket
from _thread import start_new_thread
from connections.servers.server_client import Client
from utils.logger import Logger


logger = Logger()

class TcpServer:
    def __init__(self):
        self.port = None
        self.addr = None
        self.is_ready = False
        self.socket = socket.socket()
        self._clients = []

    def listen(self, port=9000):
        self.port = port
        self.addr = socket.getaddrinfo('0.0.0.0', port)[0][-1]
        self.socket.bind(self.addr)
        self.socket.listen(5)
        start_new_thread(self._listen, ())

    def _listen(self):
        self.is_ready = True
        logger.info(self, f'start listening on port: {self.port}')
        while True:
            cl, addr = self.socket.accept()
            print('client connected from', addr)
            client = Client(cl, addr)
            self.add_client(client)

    def add_client(self, client):

        for i in range(len(self._clients)):
            c = self._clients[i]
            if c.ip == client.ip:
                del self._clients[i]
                break
        self._clients.append(client)

    def send(self, message):
        for i in range(len(self._clients)):
            client = self._clients[i]
            try:
                client.send(message)
            except Exception:
                del self._clients[i]
from utils.logger import Logger
from connections.tcp_connection import TcpConnection


logger = Logger()


class ServerConnection(TcpConnection):

    def send(self, message):
        self._send(message)

from connections.servers.tcp_server import TcpServer
from utils.config import Config

config = Config()


def setup_server():
    PORT = config.get('PORT')
    server = TcpServer()
    server.listen(PORT)

    return server

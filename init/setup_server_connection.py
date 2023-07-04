from connections.server_connection import ServerConnection
from utils.config import Config

config = Config()


def setup_server_connection():
    connection = ServerConnection(config.get('SERVER_IP'), config.get('SERVER_PORT'))

    return connection

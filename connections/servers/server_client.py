class Client:
    def __init__(self, socket, addr):
        self.socket = socket
        self.ip = addr[0]
        self.port = addr[1]
        self.addr = addr

    def send(self, message):
        self.socket.send(message)

    def __del__(self):
        self.socket.close()

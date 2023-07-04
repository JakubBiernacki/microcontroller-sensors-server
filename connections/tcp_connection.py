import socket
import json
from utils.logger import Logger
from utils.event_emitter import EventEmitter

import network
from time import sleep
from _thread import start_new_thread

logger = Logger()


class TcpConnection(EventEmitter):
    def __init__(self, address, port):
        super().__init__()
        self.address = address
        self.port = port
        self._socket = None
        self.is_ready = False

        self.on('connected', self.on_connected)
        self.on('disconnected', self.on_disconnected)
        self.on('data', self.handleIncomingData)

        start_new_thread(self._connect, ())

    def _connect(self):

        wlan = network.WLAN(network.STA_IF)

        while not wlan.isconnected():
            logger.info(self, f'waiting for wifi connection')
            sleep(1)

        while not self.is_ready:
            try:
                self._socket = socket.socket()
                logger.info(self, f'connecting to {self.address}:{self.port} ...')
                self._socket.connect((self.address, self.port))
                self.emit('connected')

            except OSError:
                self.emit('disconnected')
                sleep(1)

    def send(self, message):
        self._send(message)

    def _send(self, data):

        if not self.is_ready:
            return
        try:
            self._socket.send(data)
            logger.info(self, f'sent data: {data}')
        except OSError:
            self.emit('disconnected')

    def on_connected(self):
        self.is_ready = True
        logger.info(self, f'connected to tcp server: {self.address}:{self.port}')
        self.listen()

    def on_disconnected(self):
        self.is_ready = False
        self._connect()

    def listen(self):
        print('wait for data')

        while self.is_ready:
            data = self._socket.recv(500)

            parsed_data = str(data, 'utf8')

            if len(parsed_data) > 0:
                self.emit('data', parsed_data)

    def handleIncomingData(self, data):
        print("new data")
        logger.info(self, data)

    def __del__(self):
        self._socket.close()

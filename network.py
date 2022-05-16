import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.IF_INET, socket.SCOK_STEAM)
        self.server = "192.168.253.114"
        self.port = "8000"
        self.addr = (self.server, self.port)
        self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

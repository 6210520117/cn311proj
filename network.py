import socket
import pickle
from player import *


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.253.114"
        self.port = 8000
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            # decode แบบ pickle default of vscode
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))  # encrypt
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

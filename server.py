import socket
from _thread import *
import sys

server = "192.168.253.114"
port = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

pos = [(0, 0), (100, 100)]


def readPos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def makePos(tup):
    return str(tup[0]) + "," + str(tup[1])


def threaded_client(conn, player):
    conn.send(str.encode(makePos(pos[player])))
    reply = ""
    while True:
        try:
            data = conn.recv(2048).decode()  # amount recv information
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    conn.close()


playerNumber = 0
# wait for connection 2
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, playerNumber))
    playerNumber += 1

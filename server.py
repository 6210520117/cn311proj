import pickle
import socket
from _thread import *
from game import Game

server = "192.168.1.5"
port = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
s.listen()
print("Waiting...")
games = {}  # store game
idCount = 0


def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]  # check game ว่ายังอยู่ในlist หรือป่าว

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    try:
        del games[gameId]
        print(f'Game:{gameId} Player left the game')
    except:
        pass
    idCount -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    idCount += 1
    p = 0
    gameId = (idCount - 1) // 2  # มอบสิ่งระบุตัวตน 0 vs 0 1 vs 1
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Find a suitable opponent...")
    else:
        games[gameId].ready = True
        p = 1

    start_new_thread(threaded_client, (conn, p, gameId))

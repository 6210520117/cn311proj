import pickle
import socket
from _thread import *
from game import Game

server = socket.gethostname()  # IP ของ server
port = 8000             # port ที่จะใช้ในการติดต่อ

# สร้าง socket object
# AF_INET: IPV4, SOCK_STREAM: TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# กำหนดข้อมูลพื้นฐานให้กับ socket object
s.bind((server, port))

# สั่งให้รอการเชื่อมต่อจาก client
s.listen()
print("Waiting...")


games = {}  # store game ที่เปิดห้องอยู่
idCount = 0 # ผู้เล่นใน server


def threaded_client(conn, p, gameId):
    global idCount 

    # ส่งว่าเป็น player ใด ไปที่ client
    conn.send(str.encode(str(p)))

    while True:
        try:
            # รับข้อมูลจาก client
            data = conn.recv(4096).decode()

            if gameId in games: # check game ว่ายังอยู่ในlist หรือป่าว
                game = games[gameId] # เลือกว่า Game object ไหน

                if not data: 
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get": # ตอนแรกมันเป็น get กรณีที่ client เลือกbtnต่างๆ ก็จะไม่ใช่ get 
                        game.play(p, data) # ก็เอาสิ่งที่ player เลือกไปตั้งค่าว่า player เลือกอะไร 

                    conn.sendall(pickle.dumps(game)) # ส่งการอัพเดตไปยังทุก client ที่อยู่ใน connection
            else:
                break
        except:
            break

    try:
        del games[gameId] # ลบห้องกรณีผู้เล่นออกจากห้อง
        print(f'Game:{gameId} Player left the game')
    except:
        pass
    idCount -= 1 # ลดจำนวนผู้เล่นบนserver
    conn.close() # ปิดการเชือมต่อ


while True:
    # รับการเชื่อมต่อจาก client
    conn, addr = s.accept()
    print("Connected to:", addr)

    
    idCount += 1 # เพิ่มจำนวนผู้เล่นบน server
    p = 0 # player 0(default)

    # เอามาจับคู่ แบ่งห้อง
    gameId = (idCount - 1) // 2  # สิ่งระบุ gameID อารมณ์เหมือนหมายเลขห้อง
    if idCount % 2 == 1: # กรณีผู้เล่นยังไม่มีคู่
        games[gameId] = Game(gameId)
        print("Find a suitable opponent...")
    else: # กรณีมีห้องว่าง ก็มาเป็น player ในห้องนั้น
        games[gameId].ready = True # เกมพร้อมเล่นแล้ว
        p = 1 # เปลี่ยนจากค่า default ให้เป็น player 1

    # สร้าง thread เอาไว้รันแต่ละ client 
    start_new_thread(threaded_client, (conn, p, gameId))

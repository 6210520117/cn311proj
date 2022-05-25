class Game:
    # ตั้งค่าเริ่มต้น
    def __init__(self, id):
        # ตัวแปรที่คอยบอกว่า player 1,2 เลือกหรือยังว่าออกอะไร เลือกแล้วจะเป็น True
        self.p1Went = False
        self.p2Went = False
        # player เข้าเกมครบ 2คนหรือยัง ครบแล้วจะ True 
        self.ready = False
        # รับ id ห้อง
        self.id = id
        # player ทั้ง 2 ฝ่ายเลือกอะไร
        self.moves = [None, None]

    # คอยบอกว่า player ออกอะไร
    def get_player_move(self, p):
        return self.moves[p]

    # ตั้งค่าว่า player เลือกอะไร
    def play(self, player, move):
        self.moves[player] = move # player เลือกอะไร
        if player == 0:
            self.p1Went = True # player0 เลือกแล้ว
        else:
            self.p2Went = True # player1 เลือกแล้ว

    def connected(self): # 76 client
        return self.ready  # ตรวจสอบ connection จาก server

    def bothWent(self): # 99 client
        return self.p1Went and self.p2Went # player ทั้ง 2 เลือกหรือยัง

    def winner(self):
        # ตรวจสอบว่า player เลือกอะไร
        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]  # เอาตัวอักษรแรกมาเป็นตัวเปรียบเทียบ
        imgP1 = ''
        imgP2 = '' # รูปภาพที่จะเอาไปใช้เป็น background ของจอฝั่ง player นั้น

        if p1 == "R" and p2 == "S":
            winner = 0  # player 1 win
            imgP1 = 'r-s.jpg'
            imgP2 = 's-r.jpg'
        elif p1 == "S" and p2 == "R":
            winner = 1  # player 2 win
            imgP1 = 's-r.jpg'
            imgP2 = 'r-s.jpg'
        elif p1 == "P" and p2 == "R":
            winner = 0
            imgP1 = 'p-r.jpg'
            imgP2 = 'r-p.jpg'
        elif p1 == "R" and p2 == "P":
            winner = 1
            imgP1 = 'r-p.jpg'
            imgP2 = 'p-r.jpg'
        elif p1 == "S" and p2 == "P":
            winner = 0
            imgP1 = 's-p.jpg'
            imgP2 = 'p-s.jpg'
        elif p1 == "P" and p2 == "S":
            winner = 1
            imgP1 = 'p-s.jpg'
            imgP2 = 's-p.jpg'
        elif p1 == "S" and p2 == "S":
            winner = -1 # tie
            imgP1 = 's-s.jpg'
            imgP2 = 's-s.jpg'
        elif p1 == "R" and p2 == "R":
            winner = -1
            imgP1 = 'r-r.jpg'
            imgP2 = 'r-r.jpg'
        elif p1 == "P" and p2 == "P":
            winner = -1
            imgP1 = 'p-p.jpg'
            imgP2 = 'p-p.jpg'

        return winner, imgP1, imgP2 # ส่งผลการเล่น, รูป background ที่ใช้แต่ละฝ่าย

    def resetWent(self): # หลังจาก bothWent(ตอบมาทั้งคู่) ก็ reset
        self.p1Went = False
        self.p2Went = False

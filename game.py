class Game:
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0, 0]
        self.ties = 0

    def get_player_move(self, p):
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready  # ตรวจสอบ connection จาก server

    def bothWent(self):
        return self.p1Went and self.p2Went

    def winner(self):

        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]  # เอาตัวอักษรแรก
        imgP1 = ''
        imgP2 = ''

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
            winner = -1
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

        return winner, imgP1, imgP2

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False

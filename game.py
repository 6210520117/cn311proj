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
        img = ""
        winner = -1  # ties
        if p1 == "R" and p2 == "S":
            winner = 0  # player 1 win
            img = "lol1"
        elif p1 == "S" and p2 == "R":
            winner = 1  # player 2 win
            img = "lol2"
        elif p1 == "P" and p2 == "R":
            winner = 0
            img = "lol3"
        elif p1 == "R" and p2 == "P":
            winner = 1
            img = "lol4"
        elif p1 == "S" and p2 == "P":
            winner = 0
            img = "lol5"
        elif p1 == "P" and p2 == "S":
            winner = 1
            img = "lol6"

        return winner, img

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False

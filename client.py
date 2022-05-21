import pygame
import socket
import pickle
pygame.font.init()


# NETWORK


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostname()
        self.port = 8000
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)


class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 30)
        text = font.render(self.text, 1, (0, 0, 0))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2),
                 self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


width = 1200
height = 375
win = pygame.display.set_mode((width, height))
picture = pygame.image.load('bg.jpg')
picture = pygame.transform.scale(picture, (width, height))
pygame.display.set_caption("ROCK PAPER SCISSORS - Client")


def redrawWindow(win, game, p):
    win.fill((255, 255, 255))
    win.blit(picture, (0, 0))
    if not(game.connected()):
        font = pygame.font.SysFont("consolas", 60)
        # text = font.render("Waiting for Player...", 1, (255, 0, 0), True)
        text = font.render("Waiting for Player...", True, (255, 255, 255))
        text.set_alpha(200)
        win.blit(text, (width/2 - text.get_width() /
                 2, height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("consolas", 50, bold=True)
        text = font.render("Multiplayer Game", 1, (255, 255, 255))
        win.blit(text, (width/2 - text.get_width() /
                 2, 50))

        font = pygame.font.SysFont("candara", 48)
        text = font.render("Your Move", 1, (255, 255, 255))
        win.blit(text, (width/2 - width/4 - text.get_width()/2, 120))

        text = font.render("Opponents", 1, (255, 255, 255))
        win.blit(text, (width/2 + width/4 - text.get_width()/2, 120))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)

        font = pygame.font.SysFont("candara", 40)
        if game.bothWent():
            text1 = font.render(move1, 1, (255, 255, 255))
            text2 = font.render(move2, 1, (255, 255, 255))
        else:
            if game.p1Went and p == 0:
                text1 = font.render(move1, 1, (255, 255, 255))
            elif game.p1Went:
                text1 = font.render("Selected", 1, (255, 255, 255))
            else:
                text1 = font.render("Waiting...", 1, (255, 255, 255))

            if game.p2Went and p == 1:
                text2 = font.render(move2, 1, (255, 255, 255))
            elif game.p2Went:
                text2 = font.render("Selected", 1, (255, 255, 255))
            else:
                text2 = font.render("Waiting...", 1, (255, 255, 255))

        if p == 1:
            win.blit(text2, (width/2 - width/4 - text1.get_width()/2, 180))
            win.blit(text1, (width/2 + width/4 - text2.get_width()/2, 180))
        else:
            win.blit(text1, (width/2 - width/4 - text1.get_width()/2, 180))
            win.blit(text2, (width/2 + width/4 - text2.get_width()/2, 180))

        for btn in btns:
            btn.draw(win)

    pygame.display.update()


btns = [Button("Rock", width/2 - width/4 - 75, 250, (255, 255, 255)), Button(
    "Scissors", width/2 - 75, 250, (255, 255, 255)), Button("Paper", width/2 + width/4 - 75, 250, (255, 255, 255))]


def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print("You are player", player)

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.bothWent():
            redrawWindow(win, game, player)
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

            check, imgP1, imgP2 = game.winner()

            font = pygame.font.SysFont("comicsans", 90)
            if (check == 1 and player == 1) or (check == 0 and player == 0):
                text = font.render("You Won!", 1, (63, 171, 187))
                # text.set_alpha(200)
                if (player == 0):
                    picmain = pygame.image.load(imgP1)
                    picmain = pygame.transform.scale(picmain, (width, height))
                    win.blit(picmain, (0, 0))
                else:
                    picmain = pygame.image.load(imgP2)
                    picmain = pygame.transform.scale(picmain, (width, height))
                    win.blit(picmain, (0, 0))

            elif check == -1:
                text = font.render("Tie Game!", 1, (145, 165, 224))
                # text.set_alpha(200)
                if (player == 0):
                    picmain = pygame.image.load(imgP1)
                    picmain = pygame.transform.scale(picmain, (width, height))
                    win.blit(picmain, (0, 0))
                else:
                    picmain = pygame.image.load(imgP2)
                    picmain = pygame.transform.scale(picmain, (width, height))
                    win.blit(picmain, (0, 0))
            else:
                text = font.render("You Lost!", 1, (217, 76, 73))
                # text.set_alpha(200)
                if (player == 0):
                    picmain = pygame.image.load(imgP1)
                    picmain = pygame.transform.scale(picmain, (width, height))
                    win.blit(picmain, (0, 0))
                else:
                    picmain = pygame.image.load(imgP2)
                    picmain = pygame.transform.scale(picmain, (width, height))
                    win.blit(picmain, (0, 0))

            win.blit(text, (width/2 - text.get_width() /
                     2, height/2 - text.get_height()/2))

            # if (player == 0):
            #     picmain = pygame.image.load(imgP1)
            #     picmain = pygame.transform.scale(picmain, (width, height))
            #     win.blit(picmain, (0, 0))
            # else:
            #     picmain = pygame.image.load(imgP2)
            #     picmain = pygame.transform.scale(picmain, (width, height))
            #     win.blit(picmain, (0, 0))

            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and game.connected():
                        if player == 0:
                            if not game.p1Went:
                                n.send(btn.text)
                        else:
                            if not game.p2Went:
                                n.send(btn.text)

        redrawWindow(win, game, player)


# MenuScreen
pic = pygame.image.load('menu.jpg')
pic = pygame.transform.scale(pic, (width, height))


def menu_screen():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        win.fill((0, 0, 0))
        win.blit(pic, (0, 0))
        # font = pygame.font.SysFont("comicsans", 108)
        # text = font.render("CLICK TO PLAY", 1, (255, 0, 0))
        # win.blit(text, (500, 300))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()


while True:
    menu_screen()

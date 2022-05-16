import pygame
from network import *

# window
width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0


class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.pos = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.pos
        if keys[pygame.K_RIGHT]:
            self.x += self.pos
        if keys[pygame.K_UP]:
            self.y -= self.pos
        if keys[pygame.K_DOWN]:
            self.y += self.pos

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def newWindow(win, player1, player2):
    win.fill((255, 255, 255))
    player1.draw(win)
    player2.draw(win)
    pygame.display.update()


def readPos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def makePos(tup):
    return str(tup[0]) + "," + str(tup[1])


def main():
    run = True

    n = Network()
    startPos = readPos(n.getPos())   # str from server need to adapter
    p1 = Player(startPos[0], startPos[1], 100, 100, (0, 255, 0))
    p2 = Player(0, 0, 100, 100, (0, 255, 0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)  # check run
        p2Pos = readPos(n.send(makePos((p1.x, p1.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p1.move()
        newWindow(win, p1, p2)


main()

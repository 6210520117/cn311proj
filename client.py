import pygame
from network import Network
from player import Player


# window
width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def newWindow(win, player1, player2):
    win.fill((255, 255, 255))
    player1.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)  # check run
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        newWindow(win, p, p2)


main()

import pygame

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
from direction import Direction 
from color import RED

import pygame


class Player:
    def __init__(self) -> None:
        self.speed = 10
        self.x = 50
        self.y = 50
        self.width = 50
        self.height = 50
        self.direction = Direction.RIGHT

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.y -= self.speed
            self.direction = Direction.UP
        elif keys[pygame.K_DOWN]:
            self.y += self.speed
            self.direction = Direction.DOWN

        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.direction = Direction.LEFT
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.direction = Direction.RIGHT

    def get_direction(self):
        return self.direction

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
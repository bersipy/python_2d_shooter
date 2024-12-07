from direction import Direction 
from color import RED

import pygame


class Player:
    def __init__(self) -> None:
        self.speed = 10 * 100
        self.x = 50
        self.y = 50
        self.width = 50
        self.height = 50
        self.direction = Direction.RIGHT

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.y -= self.speed * dt
            self.direction = Direction.UP
        elif keys[pygame.K_DOWN]:
            self.y += self.speed * dt
            self.direction = Direction.DOWN

        if keys[pygame.K_LEFT]:
            self.x -= self.speed * dt
            self.direction = Direction.LEFT
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed * dt
            self.direction = Direction.RIGHT

        # diagonal movement
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            self.direction = Direction.UP_LEFT
        elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]: 
            self.direction = Direction.UP_RIGHT
        elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            self.direction = Direction.DOWN_LEFT
        elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            self.direction = Direction.DOWN_RIGHT

    def get_direction(self):
        return self.direction

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
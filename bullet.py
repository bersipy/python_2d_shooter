from color import BLUE

import pygame


class Bullet:
    radius = 15

    def __init__(self, starting_pos: tuple, direction: tuple) -> None:
        self.speed = 10 * 100
        self.x, self.y = starting_pos
        self.dir_x, self.dir_y = direction
        self.counter = 0

    def move(self, dt):
        self.x += self.speed * self.dir_x * dt
        self.y += self.speed * self.dir_y * dt

    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), self.radius)

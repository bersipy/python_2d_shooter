from direction import Direction
from color import BLUE

import pygame


class Bullet:
    radius = 15
    ttl = 

    def __init__(self, starting_pos: tuple, direction: tuple) -> None:
        self.speed = 20
        self.x, self.y = starting_pos
        self.dir_x, self.dir_y = direction

    def move(self):
        self.x += self.speed * self.dir_x
        self.y += self.speed * self.dir_y

    def draw(self, screen, dt):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), self.radius)

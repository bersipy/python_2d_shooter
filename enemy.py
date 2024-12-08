import random
import math

from color import RED
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

import pygame


class Enemy:
    def __init__(self, speed: int = 5):
        self.speed = speed * 100
        self.width = 25
        self.height = 25
        self.__destination_reached = False
        self.__position = self.__get_random_vector2(range(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.__destination = self.__get_random_vector2(range(0, 0))

    def update(self, dt):
        if self.__destination_reached:
            self.__destination = self.__get_random_vector2(range(SCREEN_WIDTH, SCREEN_HEIGHT))
        
        self.__move(dt)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.__position.x, self.__position.y, self.width, self.height))

    def __move(self, dt):
        x = pow(self.__position.x - self.__destination.x)
        y = pow(self.__position.y - self.__destination.y)
        distance = math.sqrt(x + y, 2)



    def __get_random_vector2(self, range: range):
        x, y = random.randint(0, range.start), random.randint(0, range.stop)
        return pygame.math.Vector2(x, y)


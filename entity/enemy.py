import random
import math

from utils.color import RED
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

import pygame


class Enemy:
    def __init__(self, speed):
        self.speed = speed * 100
        self.size = 25
        self.__position = self.__get_random_vector2(range(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.__destination = self.__get_random_vector2(range(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.collision_rect = pygame.Rect(self.__position.x, self.__position.y, self.size, self.size)

    def update(self, dt):
        if self.__destination == self.__position:
            self.__destination = self.__get_random_vector2(range(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.__move(dt)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.collision_rect)

    def __move(self, dt):
        distance = self.__destination.distance_to(self.__position)
        distance_to_move = self.speed * dt

        dx = self.__destination.x - self.__position.x
        dy = self.__destination.y - self.__position.y

        if distance <= distance_to_move:
            self.__position = self.__destination
        else:   
            x = dx * distance_to_move / distance
            y = dy * distance_to_move / distance
            self.__position += pygame.math.Vector2(x, y)

        self.collision_rect.x = self.__position.x
        self.collision_rect.y = self.__position.y

    def __get_random_vector2(self, range: range):
        x, y = random.randint(0, range.start), random.randint(0, range.stop)
        return pygame.math.Vector2(x, y)



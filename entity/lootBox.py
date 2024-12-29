import random

from utils.color import ORANGE
from manager.inventory_manager import InventoryManager
from items import Items

import pygame


class LootBox:
    def __init__(self, starting_pos: tuple):
        self.size = 20
        self.inventory = InventoryManager()
        self.inventory.add(Items.BULLET, random.randint(1, 3))
        self.collision_rect = pygame.Rect(starting_pos[0], starting_pos[1], self.size, self.size)
        self.is_looted = False

    def draw(self, screen):
        pygame.draw.rect(screen, ORANGE, self.collision_rect)
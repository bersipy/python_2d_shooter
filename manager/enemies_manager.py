import time
from typing import Dict, Tuple

from entity.enemy import Enemy
from utils.id_generator import IdGenerator


class EnemiesManager:
    def __init__(self):
        self.__enemies : Dict[int, Tuple[Enemy, float, float]] = {}
        self.id_generator = IdGenerator()

    @property
    def enemies(self):
        return self.__enemies.values()

    def spawn(self):
        _id = self.id_generator.generate()
        enemy = Enemy(3)
        self.__enemies[_id] = enemy

    def draw(self, screen):
        for enemy in self.__enemies.values():
            enemy.draw(screen)

    def update(self, dt: int):
        self.__clean_killed_enemies()
        for enemy in self.__enemies.values():
            enemy.update(dt)

    def __clean_killed_enemies(self):
        self.__enemies = { k: v for k, v in self.__enemies.items() if not v.is_dead }
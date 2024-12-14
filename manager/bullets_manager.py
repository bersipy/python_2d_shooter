import time
from typing import Dict, Tuple

from entity.bullet import Bullet
from utils.id_generator import IdGenerator


class BulletsManager:
    def __init__(self):
        self.__bullets : Dict[int, Tuple[Bullet, float, float]] = {}
        self.id_generator = IdGenerator()

    @property
    def bullets(self):
        return [t[0] for t in self.__bullets.values()]

    def spawn(self, starting_pos: tuple, direction: tuple, ttl: float = 0.5):
        _id = self.id_generator.generate()
        bullet = Bullet(starting_pos, direction)
        self.__bullets[_id] = (bullet, ttl, time.time()) 

    def draw(self, screen):
        for bullet, _, _ in self.__bullets.values():
            bullet.draw(screen)

    def update(self, dt: int):
        self.__clean_old_bullets()
        for (bullet, _, _) in self.__bullets.values():
            bullet.update(dt)

    def __clean_old_bullets(self):
        current_time = time.time()
        self.__bullets = {
            bullet_id: (data, ttl, creation_time)
            for bullet_id, (data, ttl, creation_time) in self.__bullets.items()
            if current_time - creation_time < ttl
        }
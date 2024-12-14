import time
from typing import Dict

from entity.bullet import Bullet
from utils.id_generator import IdGenerator
from manager.collision_manager import CollisionManager


class BulletsManager:
    def __init__(self):
        self.__bullets : Dict[Bullet] = {}
        self.id_generator = IdGenerator()

    @property
    def bullets(self):
        return self.__bullets

    def spawn(self, starting_pos: tuple, direction: tuple, ttl: int = 0.5):
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
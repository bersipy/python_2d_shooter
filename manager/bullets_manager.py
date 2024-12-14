import time
from typing import Dict

from entity.bullet import Bullet
from id_generator import IdGenerator


class BulletsManager:
    def __init__(self):
        self.bullets : Dict[Bullet] = {}
        self.id_generator = IdGenerator()

    def spawn(self, starting_pos: tuple, direction: tuple, ttl: int = 0.5):
        _id = self.id_generator.generate()
        bullet = Bullet(starting_pos, direction)
        self.bullets[_id] = (bullet, ttl, time.time()) 

    def draw(self, screen):
        for bullet, _, _ in self.bullets.values():
            bullet.draw(screen)

    def update(self, dt: int):
        self.__clean_old_bullets()
        for (bullet, _, _) in self.bullets.values():
            bullet.update(dt)

    def __clean_old_bullets(self):
        current_time = time.time()
        self.bullets = {
            bullet_id: (data, ttl, creation_time)
            for bullet_id, (data, ttl, creation_time) in self.bullets.items()
            if current_time - creation_time < ttl
        }
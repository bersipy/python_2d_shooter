import time

from game_state import GameState
from entity.player import Player
from manager.bullets_manager import BulletsManager
from manager.enemies_manager import EnemiesManager
from utils.color import WHITE
from manager.collision_manager import CollisionManager

import pygame

class TestLevel:
    def __init__(self, screen: pygame.Surface, fps: int):
        self.screen = screen
        self.fps = fps

    def run(self):
        player = Player()
        bullets_manager = BulletsManager()
        enemies_manager = EnemiesManager()
        enemies_manager.spawn()

        clock = pygame.time.Clock()
        last_frame = time.time()

        while(True):
            now = time.time()
            dt = now - last_frame
            last_frame = now

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return GameState.QUIT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullets_manager.spawn((player.x + player.width / 2, player.y + player.height / 2), player.get_direction())

            # update
            player.update(dt)
            bullets_manager.update(dt)
            enemies_manager.update(dt)

            for enemy in enemies_manager.enemies:
                if CollisionManager.collideAny(enemy.collision_rect, [bullet.collision_rect for bullet in bullets_manager.bullets]):
                    enemy.is_dead = True

            self.screen.fill(WHITE)

            # draw
            player.draw(self.screen)
            bullets_manager.draw(self.screen)
            enemies_manager.draw(self.screen)            

            pygame.display.flip()
            clock.tick(self.fps)

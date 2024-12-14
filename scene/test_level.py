import time

from game_state import GameState
from entity.player import Player
from entity.enemy import Enemy
from manager.bullets_manager import BulletsManager
from utils.color import WHITE

import pygame

class TestLevel:
    def __init__(self, screen: pygame.Surface, fps: int):
        self.screen = screen
        self.fps = fps

    def run(self):
        player = Player()
        enemy = Enemy(4)
        bullets_manager = BulletsManager()

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
            enemy.update(dt)
            bullets_manager.update(dt)

            self.screen.fill(WHITE)

            # draw
            player.draw(self.screen)
            bullets_manager.draw(self.screen)
            enemy.draw(self.screen)

            pygame.display.flip()
            clock.tick(self.fps)

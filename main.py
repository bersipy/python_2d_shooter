import time

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from enemy import Enemy
from bullets_manager import BulletsManager
from color import WHITE

import pygame

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Minecraft")
    player = Player()
    enemy = Enemy()
    bullets_manager = BulletsManager()

    clock = pygame.time.Clock()
    last_frame = time.time()

    while(True):
        now = time.time()
        dt = now - last_frame
        last_frame = now

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets_manager.spawn((player.x + player.width / 2, player.y + player.height / 2), player.get_direction())

        # update
        player.update(dt)
        bullets_manager.update(dt)

        screen.fill(WHITE)

        # draw
        player.draw(screen)
        bullets_manager.draw(screen)
        enemy.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()

import time

from player import Player
from bullet import Bullet
from color import WHITE

import pygame

def main():
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Minecraft")
    player = Player()
    bullets = []

    clock = pygame.time.Clock()
    last_frame = time.time()

    while(True):
        now = time.time()
        dt = last_frame - now
        last_frame = now

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet((player.x + player.width / 2, player.y + player.height / 2), player.get_direction())
                    bullets.append(bullet)                    

        player.move()
        for bullet in bullets:
            bullet.move()

        screen.fill(WHITE)

        player.draw(screen)

        for bullet in bullets:
            bullet.draw(screen, dt)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()

import time
import random

from game_state import GameState
from entity.player import Player
from entity.lootBox import LootBox
from manager.bullets_manager import BulletsManager
from manager.enemies_manager import EnemiesManager
from manager.collision_manager import CollisionManager
from manager.lotboxes_manager import LootboxesManager
from utils.color import WHITE
from items import Items
from ui.label import Label

import pygame

class TestLevel:
    def __init__(self, screen: pygame.Surface, fps: int):
        self.screen = screen
        self.fps = fps

    def run(self):
        bullet_counter = Label(text="Bullets:")
        player = Player()
        bullets_manager = BulletsManager()
        enemies_manager = EnemiesManager()
        lootboxes_manager = LootboxesManager()
        enemies_manager.spawn(3)

        # lootbox = LootBox((random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)))

        clock = pygame.time.Clock()
        last_frame = time.time()

        while(True):
            bullet_counter.update_text(f"Bullets: {player.inventory.get(Items.BULLET)}")

            now = time.time()
            dt = now - last_frame
            last_frame = now

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return GameState.QUIT

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return GameState.QUIT

                    if event.key == pygame.K_SPACE:
                        if player.inventory.get(Items.BULLET) == 0:
                            return GameState.MAIN_MENU
                        
                        bullets_manager.spawn((player.x + player.size / 2, player.y + player.size / 2), player.get_direction())
                        player.inventory.remove(Items.BULLET, 1)

            # update
            player.update(dt)
            bullets_manager.update(dt)
            enemies_manager.update(dt)
            lootboxes_manager.update()

            someone_has_died = False
            for enemy in enemies_manager.enemies:
                if CollisionManager.collideAny(enemy.collision_rect, [bullet.collision_rect for bullet in bullets_manager.bullets]):
                    enemy.is_dead = True
                    someone_has_died = True
                    
                    # we spawn a lootbox in place of the enemy
                    lootboxes_manager.spawn(enemy.position)

            if someone_has_died:
                probability = 0.5
                for _ in range(5):
                    if random.random() < probability:
                        enemies_manager.spawn(1)

            for lootbox in lootboxes_manager.lootboxes:
                if CollisionManager.collide(player.collision_rect, lootbox.collision_rect):
                    lootbox.is_looted = True
                    bullets = lootbox.inventory.get(Items.BULLET)

                    print(f"We added {bullets} to the player")
                    player.inventory.add(Items.BULLET, bullets)

            self.screen.fill(WHITE)

            # draw
            player.draw(self.screen)
            bullets_manager.draw(self.screen)
            lootboxes_manager.draw(self.screen)
            enemies_manager.draw(self.screen)    
            bullet_counter.draw(self.screen)       

            # utility
            pygame.display.flip()
            clock.tick(self.fps)

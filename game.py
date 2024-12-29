from game_state import GameState
from scene.test_level import TestLevel
from scene.main_menu import MainMenu
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Minecraft")
        self.state = GameState.TEST_LEVEL

    def run(self):
        while True:
            if self.state == GameState.TEST_LEVEL:
                print("Test level is running")
                self.state = TestLevel(self.screen, FPS).run()
            elif self.state == GameState.MAIN_MENU:
                print("Main menu")
                self.state = MainMenu(self.screen, FPS).run()

            elif self.state == GameState.QUIT:
                print("Quitting the game...")
                pygame.quit()
                exit(0)
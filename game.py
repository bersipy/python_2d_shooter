from game_state import GameState
from scene.test_level import TestLevel
from scene.main_menu import MainMenu
from scene.particle_test import ParticleTest
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from utils.color import WHITE, rgb_to_gl_color

import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)
        pygame.display.set_caption("Minecraft")
        self.state = GameState.MAIN_MENU

        self.init_opengl()

    def init_opengl(self):
        # Set up OpenGL for 2D rendering
        glClearColor(*rgb_to_gl_color(WHITE))  # Set background color (black)
        glEnable(GL_BLEND)  # Enable transparency (if needed for particles)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        # Set up projection matrix (orthographic for 2D rendering)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()  # Reset the projection matrix
        gluOrtho2D(0, SCREEN_WIDTH, SCREEN_HEIGHT, 0)  # Set 2D orthographic projection
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()  # Reset the model-view matrix

        # Other potential OpenGL settings
        glViewport(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)  # Set the viewport size

    def run(self):
        while True:
            if self.state == GameState.TEST_LEVEL:
                print("Test level is running")
                self.state = TestLevel(FPS).run()
            elif self.state == GameState.MAIN_MENU:
                print("Main menu")
                self.state = MainMenu(FPS).run()
            elif self.state == GameState.PARTICLE_TEST:
                print("Particle test is running")
                self.state = ParticleTest(FPS).run()
            elif self.state == GameState.QUIT:
                print("Quitting the game...")
                pygame.quit()
                exit(0)
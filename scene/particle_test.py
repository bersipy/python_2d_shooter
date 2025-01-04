import time

from particle.particle_system import ParticleSystem
from game_state import GameState

from OpenGL.GL import *
from OpenGL.GL.shaders import compileShader, compileProgram
import pygame
import numpy as np


class ParticleTest:
    def __init__(self, fps: int):
        self.fps = fps

    def __clear_openGL(self):
        # Clear the color buffer (reset the screen)
        glClear(GL_COLOR_BUFFER_BIT)
        # Reset other OpenGL states if necessary
        glLoadIdentity()  # Reset any transformations
        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        particle_system = ParticleSystem()

        # Load shaders
        vertex_shader_code = open('shaders/particle_vertex_shader.glsl', 'r').read()
        fragment_shader_code = open('shaders/particle_fragment_shader.glsl', 'r').read()

        vertex_shader = compileShader(vertex_shader_code, GL_VERTEX_SHADER)
        fragment_shader = compileShader(fragment_shader_code, GL_FRAGMENT_SHADER)
        shader_program = compileProgram(vertex_shader, fragment_shader)

        # Create VAO and VBO for particles (as points)
        VAO = glGenVertexArrays(1)
        VBO = glGenBuffers(1)
        glBindVertexArray(VAO)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)

        # Set up a single particle point (this could be expanded if you want textured particles)
        particle_vertices = np.array([0.0, 0.0], dtype=np.float32)
        glBufferData(GL_ARRAY_BUFFER, particle_vertices.nbytes, particle_vertices, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * particle_vertices.itemsize, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        # Set the particle emitter's properties
        emission_rate = 50  # particles per second
        last_emit_time = time.time()
        last_time = time.time()

        # Game loop
        while True:
            delta_time = time.time() - last_time
            last_time = time.time()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__clear_openGL()
                    return GameState.QUIT

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.__clear_openGL()
                        return GameState.MAIN_MENU

            # Emit new particles at regular intervals
            if time.time() - last_emit_time > 1.0 / emission_rate:
                position = np.random.uniform(-0.5, 0.5, 2)  # Random position within a certain range
                velocity = np.random.uniform(-0.1, 0.1, 2)  # Random velocity
                color = np.array([1.0, 0.5, 0.2, 1.0], dtype=np.float32)  # Color (red-orange)
                size = 0.05  # Particle size
                lifespan = 2.0  # Lifespan in seconds
                particle_system.emit_particle(position, velocity, color, size, lifespan)
                last_emit_time = time.time()
            
            # Update particle system
            particle_system.update(delta_time)

            # Clear screen and render particles
            glClear(GL_COLOR_BUFFER_BIT)
            particle_system.draw(shader_program, VAO)
            
            pygame.display.flip()
            clock.tick(self.fps)

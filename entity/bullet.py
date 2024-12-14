from utils.color import BLUE, RED
import pygame


class Bullet:
    radius = 15

    def __init__(self, starting_pos: tuple, direction: tuple) -> None:
        self.speed = 12 * 100
        self.position = pygame.math.Vector2(starting_pos)
        self.direction = pygame.math.Vector2(direction)
        self.direction.normalize_ip()
        self.counter = 0

        size = 2 * self.radius
        self.collision_rect = pygame.Rect(self.position.x - self.radius, self.position.y - self.radius, size, size)
        self.is_dead = False

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        # Use the normalized direction vector for movement
        movement : pygame.Vector2 = self.direction * self.speed * dt
        self.position += movement

        self.collision_rect.x = self.position.x
        self.collision_rect.y = self.position.y


    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, (self.position.x, self.position.y), self.radius)

import pygame


class CollisionManager:
    @staticmethod
    def collide(rectA: pygame.Rect, rectB: pygame.Rect):
        return rectA.colliderect(rectB)
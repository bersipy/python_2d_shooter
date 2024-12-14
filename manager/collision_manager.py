from typing import List

import pygame


class CollisionManager:
    @staticmethod
    def collide(rectA: pygame.Rect, rectB: pygame.Rect):
        return rectA.colliderect(rectB)
    
    @staticmethod
    def collideAny(rect: pygame.Rect, listOfRects: List[pygame.Rect]):
        return any(map(rect.colliderect, listOfRects))
    
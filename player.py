# player.py
# Player class and logic
import pygame
from settings import PLAYER_SIZE, PLAYER_COLOR

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.name = ""

    def update(self, platforms):
        # Apply gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        # Horizontal movement
        self.rect.x += self.vel_x
        # Check horizontal collisions
        for plat in platforms:
            if self.rect.colliderect(plat):
                if self.vel_x > 0:
                    self.rect.right = plat.left
                elif self.vel_x < 0:
                    self.rect.left = plat.right
        # Vertical movement
        self.rect.y += self.vel_y
        self.on_ground = False
        for plat in platforms:
            if self.rect.colliderect(plat):
                if self.vel_y > 0:
                    self.rect.bottom = plat.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.rect.top = plat.bottom
                    self.vel_y = 0

    def draw(self, surface):
        pygame.draw.rect(surface, PLAYER_COLOR, self.rect)

import pygame
from pygame.locals import *
import math


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.color = (255, 0, 0)  # Red color
        self.speed = 2
        self.health = 30

    def move_towards_player(self, player_x, player_y):
        # Calculate direction to player
        dx = player_x - self.x
        dy = player_y - self.y

        # Calculate distance to player
        distance = math.sqrt(dx ** 2 + dy ** 2)

        # Normalize and scale by speed
        if distance != 0:  # Prevent division by zero
            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color,
                         (self.x, self.y, self.width, self.height))

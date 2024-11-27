import pygame
from pygame.locals import *


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_y = 0
        self.vel_x = 0
        self.speed = 0.5
        self.max_speed = 3
        self.friction = 0.1
        self.width = 50
        self.height = 50
        self.color = (0, 0, 255) # blue

    def move(self, screen_width, screen_height):
            self.x += self.vel_x
            self.y += self.vel_y

            # apply friction
            self.vel_x *= (1 - self.friction)
            self.vel_y *= (1 - self.friction)

            # keep player within screen boundaries
            self.x = max(0, min(self.x, screen_width - self.width))
            self.y = max(0, min(self.y, screen_height - self.height))

    def handle_input(self, pressed):

        if pressed[K_d]:
            self.vel_x = min(self.vel_x + self.speed, self.max_speed)
        if pressed[K_a]:
            self.vel_x = max(self.vel_x - self.speed, -self.max_speed)
        if pressed[K_s]:
            self.vel_y = min(self.vel_y + self.speed, self.max_speed)
        if pressed[K_w]:
            self.vel_y = max(self.vel_y - self.speed, -self.max_speed)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))



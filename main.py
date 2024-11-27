import pygame
from pygame.locals import *
from player import Player
from enemy import Enemy

# Initialize Pygame
pygame.init()

# Display setup
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Crawler")

# Colors
BACKGROUND = (255, 255, 255)  # White

# Create player in center of screen
player = Player(WIDTH // 2, HEIGHT // 2)

# Create an enemy
enemy = Enemy(100, 100)  # Start enemy at position (100, 100)

# Game loop
clock = pygame.time.Clock()
FPS = 60
running = True

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    # Handle input and movement
    pressed = pygame.key.get_pressed()
    player.handle_input(pressed)
    player.move(WIDTH, HEIGHT)

    # Update enemy
    enemy.move_towards_player(player.x, player.y)

    # Draw
    screen.fill(BACKGROUND)
    player.draw(screen)
    enemy.draw(screen)
    pygame.display.flip()

    # Control frame rate
    clock.tick(FPS)

pygame.quit()

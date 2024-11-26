import pygame

# Initialize Pygame
pygame.init()

# COLORS
BACKGROUND = (255, 255, 255)  # White

# Clock
FPS = 60
clock = pygame.time.Clock()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Neat Collab")
running = True

# Game loop
while running:
    # 1. Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if window close button is clicked
            running = False
        # Fixed escape key check - it should be a keyboard event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # 2. Clear the screen
    screen.fill(BACKGROUND)  # Fill with background color

    # 3. Draw/render game elements

    pygame.draw.rect(screen, (0, 0, 0), (100, 100, 50, 50))  # Draw a black rectangle

    # 4. Update the display
    pygame.display.flip()

    # 5. Control the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
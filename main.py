import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1280, 720))  # Width: 1280, Height: 720
clock = pygame.time.Clock()
running = True

# Game loop
while running:
    # 1. Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if window close button is clicked
            running = False

    # 2. Clear the screen
    screen.fill("purple")  # Fill with background color

    # 3. Draw/render game elements
    # Your game drawing code would go here

    # 4. Update the display
    pygame.display.flip()

    # 5. Control the frame rate
    clock.tick(60)  # Limit to 60 FPS

# Quit Pygame
pygame.quit()

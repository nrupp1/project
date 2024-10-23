import pygame
import math

# Initialize pygame
pygame.init()

# Set up the display
SCREEN_WIDTH, SCREEN_HEIGHT = 320, 240
Screem_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(Screem_size, pygame.SCALED)
pygame.display.set_caption("Don't Crash!!")

# Load road textures
road_texture = pygame.image.load("road3.png")

# Clock for managing time and speed
clock = pygame.time.Clock()

car_x = 0  # Starting car x-position
running = True

while running:
    delta = clock.tick() / 1000 + 0.00001  # Calculate delta time
    car_x += delta * 200  # Speed up the car a bit for testing purposes

    # Handle quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background with sky color
    screen.fill((100, 150, 250))
    # Draw the road in the main loop
    for i in range(130):  # 120 rows of road slices
        scale = (139 - i) / 320
        x = car_x + i / scale  # Update road position based on car_x and current row

        # Correctly using math.sin instead of sin
        y_pos = 200 * math.sin(x / 1170) + 170 * math.sin(x / 580)  # Calculate y position to simulate depth effect
        horizontal = 200 - (200 - y_pos) * scale

        # Extract a road slice from the texture
        road_slice = road_texture.subsurface(0, int(x % road_texture.get_height()), road_texture.get_width(), 1)

        # Scale the road slice to create a sense of perspective (smaller at the top)
        scale_factor = (140 - i) / 300
        scaled_slice = pygame.transform.scale(road_slice, (int(road_texture.get_width() * scale_factor), 1))

        # Color the road based on depth
        color = (int(50 - i / 3), int(130 - i), int(50 + 30 * math.sin(x)))
        pygame.draw.rect(screen, color, (0, 239 - i, 320, 1))

        # Center the scaled road slice horizontally
        slice_x = (SCREEN_WIDTH - scaled_slice.get_width()) // 2

        # Blit the scaled road slice onto the screen
        screen.blit(scaled_slice, (horizontal, 239 - i))

    # Update the display with the road drawn
    pygame.display.update()

# Quit pygame
pygame.quit()

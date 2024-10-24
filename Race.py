import pygame
import math

# Initialize pygame
pygame.init()

# Set up the display
SCREEN_WIDTH, SCREEN_HEIGHT = 320, 240
screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(screen_size, pygame.SCALED)
pygame.display.set_caption("Don't Crash!!")

# Load road textures
road_texture = pygame.image.load("road3.png")

# Clock for managing time and speed
clock = pygame.time.Clock()

car_x = 0  # Starting car x-position
running = True

while running:
    delta = clock.tick() / 1000 + 0.00001  # Calculate delta time
    car_x += delta * 10  # Updated speed to match the provided ideas

    # Handle quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background with sky color
    screen.fill((100, 150, 250))

    # Initialize vertical position and draw distance
    vertical, draw_distance = 180, 1
    z_buffer = [999 for _ in range(SCREEN_HEIGHT)]  # Adjusted to match screen height

    while draw_distance < 115:
        last_vertical = vertical

        # Keep drawing the road while vertical is greater than or equal to the last position
        while vertical >= last_vertical and draw_distance < 120:
            draw_distance += draw_distance / 600  # Increment draw distance

            x = car_x + draw_distance  # Update x position based on draw distance
            scale = 1 / draw_distance  # Calculate scale for perspective

            # Simulate the z-axis (depth effect) with sine waves
            z = 200 + 80 * math.sin(x / 17) - 140 * math.sin(x / 8)

            # Update vertical position based on scale
            vertical = int(80 + 180 * scale + z * scale)

            if draw_distance < 115:
                # Clamp vertical to be within screen height (z_buffer size)
                vertical_clamped = max(0, min(SCREEN_HEIGHT - 1, int(vertical)))

                # Ensure z_buffer remains in bounds
                z_buffer[vertical_clamped] = draw_distance

                # Calculate the horizontal position based on the perspective scale
                # Drastic hills: modifying y to create larger vertical shifts
                y = 200 * math.sin(x / 15) + 250 * math.sin(x / 7)

                # Horizontal positioning based on perspective scaling
                horizontal = int(160 - (120 - y) * scale)

                road_slice = road_texture.subsurface((0, int(10 * x % 170), 320, 1))

                # Clamp color values to avoid invalid arguments
                color = (
                    max(0, min(255, int(50 - draw_distance / 3))),  # Red value
                    max(0, min(255, int(130 - draw_distance))),     # Green value
                    max(0, min(255, int(50 - z / 20 + 30 * math.sin(x))))  # Blue value
                )

                # Draw a rectangle for the road slice with the calculated color
                pygame.draw.rect(screen, color, (0, vertical_clamped, 320, 1))

                # Extract a road slice from the texture
                road_slice = road_texture.subsurface(0, int(x % road_texture.get_height()), road_texture.get_width(), 1)

                # Scale the road slice based on the perspective scale
                scaled_slice = pygame.transform.scale(road_slice, (int(500 * scale), 1))

                # Blit the scaled road slice onto the screen at the calculated horizontal position
                screen.blit(scaled_slice, (horizontal, vertical_clamped))

        # Adjust vertical for the next slice
        vertical += 1

    # Update the display with the road drawn
    pygame.display.update()

# Quit pygame
pygame.quit()

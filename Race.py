import os
import pygame
from PIL import Image
from math import tan, radians, degrees, pi
from pygame.locals import *

import os
import pygame
from pygame.locals import *
from math import tan, radians

# Set the screen dimensions
SCREEN_HEIGHT = 640
SCREEN_WIDTH = 480
HALF_HEIGHT = SCREEN_HEIGHT // 2
HALF_WIDTH = SCREEN_WIDTH // 2

def load_images():
    """Load images and handle loading errors."""
    try:
        background = pygame.image.load("nolines.png").convert()
        stripes_image = pygame.image.load("stripes.png").convert()
        road_image = pygame.image.load("road3.png").convert()
        return background, stripes_image, road_image
    except Exception as e:
        print(f"Error loading images: {e}")
        return None, None, None

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Road Raster Effect")

    # Load images
    background, stripes_image, road_image = load_images()
    if background is None:
        return  # Exit if images failed to load

    # Resize the background to fit the screen
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set camera parameters
    camera_y = 15
    camera_z = 0.1
    fov_angle = 60
    scaling = (HALF_WIDTH) / tan(radians(fov_angle / 2))

    # Game loop
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        # Clear the screen and display the background
        screen.blit(background, (0, 0))

        # Apply raster effect by progressively scaling road and stripes images
        for y in range(HALF_HEIGHT, SCREEN_HEIGHT):
            z_world = (y - HALF_HEIGHT) + camera_y  # Distance to the screen based on y position
            if z_world <= 0:
                continue  # Skip if z_world is zero or negative to avoid division by zero

            perspective_scale = scaling / z_world

            # Set widths based on perspective
            road_width = int(SCREEN_WIDTH * 0.4 * perspective_scale)  # Road should be about 40% of screen width
            stripe_width = int(SCREEN_WIDTH * 0.2 * perspective_scale)  # Stripes should take up about 20% on either side
            road_height = int(SCREEN_HEIGHT / 10)  # Keep height fixed for horizontal strips

            # Scale the road and stripes for perspective effect
            scaled_road_image = pygame.transform.scale(road_image, (road_width, road_height))
            scaled_stripes_image = pygame.transform.scale(stripes_image, (stripe_width, road_height))

            # Calculate positions to center road and put stripes on either side
            road_x_position = (HALF_WIDTH - (road_width // 2))
            left_stripe_x_position = road_x_position - stripe_width
            right_stripe_x_position = road_x_position + road_width

            # Blit the road and stripes onto the screen
            screen.blit(scaled_road_image, (road_x_position, y))
            screen.blit(scaled_stripes_image, (left_stripe_x_position, y))
            screen.blit(scaled_stripes_image, (right_stripe_x_position, y))

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()

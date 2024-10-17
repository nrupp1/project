import pygame
import math
from pygame.locals import *

# Set the screen dimensions
SCREEN_HEIGHT = 480
SCREEN_WIDTH = 640
HORIZON_Y = 220  # Horizon starting point
MIN_ROAD_WIDTH = 28  # Narrow road width at the horizon
MAX_ROAD_WIDTH = 640  # Wide road width at the base
STRIPE_HEIGHT = 10  # Height of each stripe section
STRIPE_SPEED = 3  # Speed for stripe movement


def load_images():
    """Load images and handle loading errors."""
    try:
        # Removed the background image as it's no longer needed
        road_image = pygame.image.load("road3.png").convert()
        road_image2 = pygame.image.load("road2.png").convert()
        return road_image, road_image2
    except Exception as e:
        print(f"Error loading images: {e}")
        return None, None


def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Road Stretching Effect")

    # Load images
    road_image, road_image2 = load_images()
    if road_image is None or road_image2 is None:
        return  # Exit if images failed to load

    clock = pygame.time.Clock()

    # Initialize stripe positions below the horizon
    stripe_positions = list(range(HORIZON_Y, SCREEN_HEIGHT, STRIPE_HEIGHT * 2))

    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

                # Fill the screen with the blue background color
            screen.fill((100, 150, 250))

            # Fill the area below the horizon with the specified light green color
            pygame.draw.rect(screen, (180, 230, 28), (0, HORIZON_Y, SCREEN_WIDTH, SCREEN_HEIGHT - HORIZON_Y))

        # Draw dark green stripes and empty rows
        for i in range(len(stripe_positions)):
            position = stripe_positions[i]

            # Draw the green stripe
            pygame.draw.rect(screen, (0, 198, 0), (0, position, SCREEN_WIDTH, STRIPE_HEIGHT))  # Green row

            # Draw empty row (light green)
            empty_row_position = position + STRIPE_HEIGHT
            if empty_row_position < SCREEN_HEIGHT:
                pygame.draw.rect(screen, (180, 230, 28),
                                 (0, empty_row_position, SCREEN_WIDTH, STRIPE_HEIGHT))  # Light green row

            # Update stripe position for movement
            stripe_positions[i] += STRIPE_SPEED  # Move downwards

            # Reset stripe position if it goes off-screen
            if stripe_positions[i] > SCREEN_HEIGHT:
                stripe_positions[i] = HORIZON_Y  # Reset back to below the horizon

        # Draw the road with stretching effect
        for i in range(HORIZON_Y, SCREEN_HEIGHT):
            # Calculate the scaling factor for perspective effect
            scale = (i - HORIZON_Y) / (SCREEN_HEIGHT - HORIZON_Y)  # Scale from 0 to 1

            # Calculate road width based on scaling factor
            road_width = int(MIN_ROAD_WIDTH + (scale * (MAX_ROAD_WIDTH - MIN_ROAD_WIDTH)))

            # Calculate the position to center the road
            road_x_position = (SCREEN_WIDTH - road_width) // 2

            # Alternate between road images
            if count % 3 == 0:
                road_slice = road_image.subsurface((0, 0, road_image.get_width(), 1))
            else:
                road_slice = road_image2.subsurface((0, 0, road_image2.get_width(), 1))
            count += 1

            # Scale the road slice to the correct width
            scaled_slice = pygame.transform.scale(road_slice, (road_width, 1))

            # Draw the scaled road slice
            screen.blit(scaled_slice, (road_x_position, i))

        # Update the display
        pygame.display.flip()
        clock.tick(60)

    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()

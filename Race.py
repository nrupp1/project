import os
import pygame
from PIL import Image
from math import tan, radians, degrees, pi
from pygame.locals import *

# Define colors
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
RED = pygame.Color('red')
GREEN = pygame.Color('green')
BLUE = pygame.Color('blue')
LIGHT_GREEN = pygame.Color('lightgreen')
LIGHT_GRAY = pygame.Color('lightgray')
DARK_GRAY = pygame.Color('darkgray')
DARK_GREEN = pygame.Color('darkgreen')

# Set the screen dimensions
h = 640
w = 480
Hh = h // 2
Hw = w // 2
def find_segment(z,segments):
    return segments[int(z/segmentLength) % segments_List_Length]
class Segment:
    def __init__(self):
        self.point_1_x = 0
        self.point_1_y = 0
        self.point_1_screen_x = 0
        self.point_1_screen_y = 0
        self.point_1_screen_scale_x = 0
        self.point_2_x = 0
        self.point_2_y = 0
        self.point_2_z = 0
        self.point_2_screen_x = 0
        self.point_2_screen_y = 0
        self.point_2_screen_scale = 0
        self.road_half_width_1 = 0
        self.road_half_width_2 = 0
        self.edge_width_1 = 0
        self.edge_width_2 = 0
        self.line_half_width_1 = 0
        self.line_half_width_2 = 0
        self.color = 0
        self.sprites=[]
    def project(self):
        f = viewing_distance
def main():
    # Initialize Pygame
    pygame.init()
    r_tree = pygame.image.load("tree.jpg").convert()
    l_tree = pygame.transform.flip(r_tree, True, False)
    car = pygame.image.load().convert()
    car.set_colorkey(car.get_at(0,0))
    car = car.subsurface(0,0,33,74)
    # Set up the display

    screen = pygame.display.set_mode((h, w))
    pygame.display.set_caption("Image Display")
    camera_x = 0
    camera_y = 15
    camera_z = .1
    fov = 60
    viewing_distance = Hw/tan(radians(fov/2))
    # Load and convert an image using PIL to strip ICC profile
    try:
        image_path = "nolines.png"
        pil_image = Image.open(image_path)
        pil_image.save(image_path)  # This removes the ICC profile
    except Exception as e:
        print(f"Error loading image: {e}")
        return

    # Now load the image using Pygame after PIL has stripped the ICC profile
    try:
        image_surface = pygame.image.load(image_path).convert()
    except Exception as e:
        print(f"Error loading image in Pygame: {e}")
        return

    # Scale image to fit the window
    image_surface = pygame.transform.scale(image_surface, (h, w))

    # Game loop
    game_running = True
    event_count = 1  # Track event count to exit after collision

    while game_running and event_count > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        # Clear the screen and display the image
        screen.fill((0, 0, 0))
        screen.blit(image_surface, (0, 0))

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()

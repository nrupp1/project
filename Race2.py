import os
import pygame
import math

# Global variables for current song and car
current_song_index = 0
current_car_index = 0

# Define songs and car images
songs = [
    "68. Rainbow Road.mp3",
    "Magical Sound Shower.mp3",
    "28. Coconut Mall.mp3",
    "85. N64 Sherbet Land.mp3",
    "1-109. Bowser's Castle_.mp3"
]
current_car = [
    "car1.png",
    "car2.png",
    "car1.png",
    "car1.png",
    "car1.png"
]

# Button display flags
buttons_visible = False
music_screen = False
car_screen = False
music_playing = False

def load_image(path, is_car=False):
    """Load and preprocess images."""
    try:
        image = pygame.image.load(path).convert_alpha() if is_car else pygame.image.load(path).convert()
        return image
    except Exception as e:
        print(f"Error loading image {path}: {e}")
        return None

def play_music(song_index):
    """Play the specified song based on the index."""
    pygame.mixer.music.load(songs[song_index])
    pygame.mixer.music.play(-1)  # Play music indefinitely

def main():
    global current_car_index, current_song_index, music_playing, buttons_visible, music_screen, car_screen
    pygame.init()
    screen = pygame.display.set_mode((320, 240))
    pygame.display.set_caption("Don't Crash!!")

    # Load initial car image
    car = load_image(current_car[current_car_index], is_car=True)

    # Button dimensions and positions
    button_width, button_height = 150, 50
    button_start_y = 100
    screen_center_x = screen.get_width() // 2

    # Button rectangles
    start_button = pygame.Rect(screen_center_x - button_width // 2, button_start_y, button_width, button_height)
    music_button = pygame.Rect(screen_center_x - button_width // 2, button_start_y + 60, button_width, button_height)
    cars_button = pygame.Rect(screen_center_x - button_width // 2, button_start_y + 120, button_width, button_height)
    back_button = pygame.Rect(10, 10, 60, 30)

    running = True
    while running:
        screen.fill((100, 150, 250))  # Sky color
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if music_screen or car_screen:
                        if back_button.collidepoint(mouse_pos):
                            music_screen = False
                            car_screen = False
                            buttons_visible = False
                            if music_playing:
                                pygame.mixer.music.stop()
                                music_playing = False
                    elif music_screen:
                        # Switch songs
                        if button1.collidepoint(mouse_pos):
                            current_song_index = (current_song_index - 1) % len(songs)
                            play_music(current_song_index)
                        elif button2.collidepoint(mouse_pos):
                            current_song_index = (current_song_index + 1) % len(songs)
                            play_music(current_song_index)
                    elif car_screen:
                        # Switch cars
                        if button1.collidepoint(mouse_pos):
                            current_car_index = (current_car_index - 1) % len(current_car)
                            car = load_image(current_car[current_car_index], True)
                        elif button2.collidepoint(mouse_pos):
                            current_car_index = (current_car_index + 1) % len(current_car)
                            car = load_image(current_car[current_car_index], True)
                    else:
                        # Main menu buttons
                        if start_button.collidepoint(mouse_pos):
                            # Start the game logic here
                            pass
                        elif music_button.collidepoint(mouse_pos):
                            music_screen = True
                            buttons_visible = True
                            play_music(current_song_index)
                        elif cars_button.collidepoint(mouse_pos):
                            car_screen = True
                            buttons_visible = True

        # Draw buttons
        if not music_screen and not car_screen:
            pygame.draw.rect(screen, (0, 255, 0), start_button)
            pygame.draw.rect(screen, (0, 255, 255), music_button)
            pygame.draw.rect(screen, (255, 0, 0), cars_button)
        else:
            pygame.draw.rect(screen, (200, 200, 200), back_button)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
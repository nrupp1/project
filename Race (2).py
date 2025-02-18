import asyncio
from itertools import count

import pygame
import sys, platform, math, random

async def main ():
    screen_size = [320, 180]
    if sys.platform == "emscripten":
        platform.window.canvas.style.imageRendering = "pixelated"
        screen = pygame.display.set_mode (screen_size)
    else:
        screen = pygame.display.set_mode (screen_size, pygame.SCALED)

    clock = pygame.time.Clock ()
    clock.tick ();
    pygame.time.wait (16)
    road_texture = pygame.image.load ("road.png").convert ()
    car_sprite = pygame.image.load ("car1.png")

    car_sprite2 = pygame.image.load ("facingcartest.png")
    car_sprite2_rect = car_sprite2.get_rect()
    car_sprite2_mask = pygame.mask.from_surface(car_sprite2)
    mask_image = car_sprite2_mask.to_surface()
    car_sprite2.set_colorkey((0,0,0))

    tree_sprite = pygame.image.load ("tree.png")

    car = Player ()
    cars = [Car (-50), Car (-23), Car (7)]
    trees = [Tree (-67), Tree (-55), Tree (-43), Tree (-33), Tree (-25), Tree (-13), Tree (-3)]

    running = 1
    total_time = 0

    while running:  # game loop
        global count
        delta = clock.tick () / 1000 + 0.00001
        total_time += delta
        car.controls (delta)

        for event in pygame.event.get ():
            if event.type == pygame.QUIT: running = 0

        screen.fill((100,180,250))
        vertical, draw_distance = 180, 1
        car.z = calc_z (car.x)
        z_buffer = [999 for element in range (180)]
        while draw_distance < 120:
            last_vertical = vertical
            while vertical >= last_vertical and draw_distance < 120:
                draw_distance += draw_distance / 150
                x = car.x + draw_distance
                scale = 1 / draw_distance
                z = calc_z (x) - car.z
                vertical = int (60 + 160 * scale + z * scale)

            if draw_distance < 115:
                z_buffer[int (vertical)] = draw_distance
                road_slice = road_texture.subsurface ((0, 10 * x % 170, 320, 1))
                color = (int (70 - draw_distance / 3), int (160 - draw_distance), int (70 - z / 20 + 30 * math.sin (x)))
                pygame.draw.rect (screen, color, (0, vertical, 320, 1))
                render_element (screen, road_slice, 500 * scale, 1, scale, x, car, 70 + car.y, z_buffer)

                """# Making collision on the player car
                player_car_rect = car_sprite.get_rect(topleft=(car.x, car.y))
                player_car_rect.topleft = (car.x, car.y)
                # Making collision on the enemy car
                car_sprite2_rect = car_sprite2.get_rect(topleft=(150, 100))
                car_sprite2_rect.topleft = (150, 100)

                if player_car_rect.colliderect(car_sprite2_rect):
                    print("Collision detected with car_sprite2!")
                    collision_sound.play()"""

        for index in reversed (range (len (trees) - 1)):
            scale = max (0.0001, 1 / (trees[index].x - car.x))
            render_element (screen, tree_sprite, 200 * scale, 300 * scale, scale, trees[index].x, car,
                            trees[index].y + car.y, z_buffer)

        if trees[0].x < car.x + 1:
            trees.pop (0)
            trees.append (Tree (trees[-1].x))
            count = 0
        for index in reversed (range (len (cars) - 1)):
            scale = max (0.0001, 1 / (cars[index].x - car.x))
            render_element (screen, car_sprite2, 100 * scale, 80 * scale, scale, cars[index].x, car, (-140 + car.y) * 1.7,
                            z_buffer)

            cars[index].x -= 10 * delta

        if cars[0].x < car.x + 1:
            cars.pop (0)
            cars.append (Car (car.x))

        #Bliting everything
        screen.blit(mask_image, (0, 0))
        screen.blit (car_sprite, (120, 120 + math.sin (total_time * car.velocity)))


        if abs (car.y - calc_y (car.x + 2) - 100) > 280 and car.velocity > 5:
            car.velocity += -car.velocity * delta
            car.acceleration += -car.acceleration * delta
            pygame.draw.circle (screen, (255, 0, 0), (300, 170), 3)
        pygame.display.update ()

        await asyncio.sleep (0)


class Tree ():
    def __init__ (self, distance):
        self.x = distance + random.randint (10, 20) + 0.5
        self.y = random.randint (500, 1500) * random.choice ([-1, 1])


def calc_y (x):
    return 200 * math.sin (x / 15) + 250 * math.sin (x / 7)


def calc_z (x):
    return 200 + 80 * math.sin (x / 17) - 140 * math.sin (x / 8)

def render_element (screen, sprite, width, height, scale, x, car, y, z_buffer):
    y = calc_y (x) - y
    z = calc_z (x) - car.z

    vertical = int (60 + 160 * scale + z * scale)
    if vertical >= 1 and vertical < 180 and z_buffer[vertical - 1] > 1 / scale - 10:
        horizontal = int (160 - (65 - y) * scale) + car.angle * (vertical - 150)

        scaled_sprite = pygame.transform.scale (sprite, (width, height))
        screen.blit (scaled_sprite, (horizontal, vertical - height + 1))


class Car ():
    def __init__ (self, distance):
        self.x = distance + random.randint (90, 110)


class Player ():
    def __init__ (self):
        self.x = 0
        self.y = 300
        self.z = 0
        self.angle = 0
        self.velocity = 0
        self.acceleration = 0

    def controls (self, delta):
        pressed_keys = pygame.key.get_pressed ()
        self.acceleration += -0.5 * self.acceleration * delta
        self.velocity += -0.5 * self.velocity * delta

        #Sounds for the player car
        driving_sound = pygame.mixer.Sound("GT2_13201_2.wav")
        driving_sound.set_volume(0.2)
        brake_sound = pygame.mixer.Sound("brake-101soundboards.mp3")
        brake_sound.set_volume(0.2)

        if not hasattr(self, 'brake_sound_played'):
            self.brake_sound_played = False

        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            if self.velocity > -1:
                self.acceleration += 4 * delta
                if not pygame.mixer.get_busy():
                    driving_sound.play()
            else:
                self.acceleration = 0
                self.velocity += -self.velocity * delta

        elif pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
            if self.velocity < 1:
                self.acceleration -= delta
                if not self.brake_sound_played:
                    brake_sound.play()
                    self.brake_sound_played = True
            else:
                self.acceleration = 0
                self.velocity += -self.velocity * delta
                self.brake_sound_played = False

        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            self.angle -= delta * self.velocity / 10
        elif pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            self.angle += delta * self.velocity / 10
        self.velocity = max (-10, min (self.velocity, 20))
        self.angle = max (-0.8, (min (0.8, self.angle)))
        self.velocity += self.acceleration * delta
        self.x += self.velocity * delta * math.cos (self.angle)
        self.y += self.velocity * math.sin (self.angle) * delta * 100


if __name__ == "__main__":
    pygame.init ()
    asyncio.run (main ())
    pygame.quit ()
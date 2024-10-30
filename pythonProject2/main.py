import pygame
from pygame import mixer

# initialize pygame
pygame.init()

# create game window
window = pygame.display.set_mode((1200, 400))

# background music
mixer.music.load('background.wav')
mixer.music.play(-1)

# set caption and icon
pygame.display.set_caption("My Self-Driving Car :)")
icon = pygame.image.load('tesla.png')
pygame.display.set_icon(icon)

# game specific variables
track = pygame.image.load('track6.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30, 60))
car_x = 150
car_y = 300
focal_dist = 25
cam_x_offset = 0
cam_y_offset = 0
drive = True
direction = 'up'

# game loop
clock = pygame.time.Clock()
while drive:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False

    # detect road
    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + cam_y_offset + 15
    up_px = window.get_at((cam_x, cam_y - focal_dist))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dist))[0]
    right_px = window.get_at((cam_x + focal_dist, cam_y))[0]

    # change direction
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        cam_x_offset = 0
        cam_y_offset = 30
        car_x += 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        cam_x_offset = 30
        cam_y_offset = 0
        car_y += 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        cam_x_offset = 0
        cam_y_offset = 0
        car_x += 30
        car_y -= 30
        car = pygame.transform.rotate(car, 90)

    # drive
    if direction == 'up' and up_px == 255:
        car_y -= 2
    elif direction == 'right' and right_px == 255:
        car_x += 2
    elif direction == 'down' and down_px == 255:
        car_y += 2
    elif direction == 'right' and right_px == 255:
        car_x += 2

    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))
    pygame.draw.circle(window, (0, 0, 255), (cam_x, cam_y), 5, 5)
    pygame.display.update()

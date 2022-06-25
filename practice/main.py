import pygame
import random
from pygame.locals import *

pygame.init()

screen_width = 700
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('THE DINO GAME')

# Game variables
tile_size = 100
bg_x = [0, 700]
bg_y = [0, 0]
bg_vel = -5  # originally, -5
cact_vel = [-1, -1]   # originally, [-1, -1]
cactus_img = pygame.image.load('Dino Game/Dino_1/cactus.png')
img = []
img_rect = []

img.append(pygame.transform.scale(cactus_img, (tile_size, tile_size)))
img.append(pygame.transform.scale(cactus_img, (tile_size, tile_size)))
img_rect.append(img[0].get_rect())
img_rect.append(img[1].get_rect())
img_rect[0].x = 300
img_rect[1].x = 700

# specify frame rate
clock = pygame.time.Clock()
fps = 60

# define colors
white = (255, 255, 255)

# load images
bg_img = pygame.transform.scale(pygame.image.load('Dino Game/Dino_1/background.jpg'), (screen_width, screen_height))


def draw_bg():
    screen.blit(bg_img, (bg_x[0], bg_y[0]))
    screen.blit(bg_img, (bg_x[1], bg_y[1]))

    bg_x[0] += bg_vel
    bg_x[1] += bg_vel
    if bg_x[0] < 0:
        bg_x[1] = bg_x[0] + screen_width
    if bg_x[1] < 0:
        bg_x[0] = bg_x[1] + screen_width
    # print("bg_x[0] = ; bg_x[1] = ", bg_x[0], bg_x[1])


class Player():
    def __init__(self, x, y):
        self.images_stand = []
        self.images_run = []
        self.images_jump = []
        self.stand_counter = 0
        self.run_counter = 0
        self.stand_cooldown = 15
        self.run_cooldown = 15
        self.stand_index = 0
        self.run_index = 0

        for num in range(1, 6):
            image_stand = pygame.image.load(f'Dino Game/Dino_1/stand_{num}.png')
            self.images_stand.append(image_stand)
        for num in range(1, 6):
            image_run = pygame.image.load(f'Dino Game/Dino_1/run_{num}.png')
            self.images_run.append(image_run)

        self.image = self.images_stand[self.stand_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        dx = 0
        dy = 0
        state = 0

        for event in pygame.event.get():
            if state == 0 and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    dx += 10
                    self.run_counter += 1
                    state = 1
            if state == 1 and event.type == pygame.KEYUP:
                dx = 0
                self.stand_index = 0
                self.run_index = 0
                self.stand_counter = 0
                self.run_counter = 0
                self.image = self.images_stand[self.stand_index]
                state = 0

        if state == 0:
            # standing animation
            self.stand_counter += 1
            if self.stand_counter > self.stand_cooldown:
                self.stand_counter = 0
                self.stand_index += 1
            if self.stand_index >= len(self.images_stand):
                self.stand_index = 0
            self.image = self.images_stand[self.stand_index]
        elif state == 1:
            # running animation
            if self.run_counter > self.run_cooldown:
                self.run_counter = 0
                self.run_index += 1
            if self.run_index >= len(self.images_run):
                self.run_index = 0
            self.image = self.images_run[self.run_index]

        self.rect.x += dx
        screen.blit(self.image, self.rect)


def create_world():
    for i in range(2):
        img_rect[i].y = screen_height - tile_size
        screen.blit(img[i], (img_rect[i].x, img_rect[i].y))
        img_rect[i].x += cact_vel[i]
        if img_rect[0].x < 0:
            img_rect[0].x += img_rect[1].x + random.randint(3, 5) * tile_size
        if img_rect[1].x < 0:
            img_rect[1].x += img_rect[0].x + random.randint(3, 5) * tile_size


player = Player(0, screen_height - tile_size)
# Game Loop
run = True
while run:
    clock.tick(fps)

    draw_bg()
    create_world()
    player.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()

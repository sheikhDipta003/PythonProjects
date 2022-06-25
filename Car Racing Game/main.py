import pygame
import random
import time
from pygame import mixer

# initialize pygame
pygame.init()

# background music
mixer.music.load('background.mp3')
mixer.music.play(-1)

# create game window
screen = pygame.display.set_mode((1200, 600))

# set caption and icon
pygame.display.set_caption("Bogus")
icon = pygame.image.load('car_1.png')
pygame.display.set_icon(icon)
pygame.display.update()

# player
playerImg = pygame.image.load('player.png')

# enemy cars
enemyImg = []
enemyImg.append(pygame.image.load('car_1.png'))
enemyImg.append(pygame.image.load('car_3.png'))
# enemyImg.append(pygame.image.load('car_3.bmp'))

# road
temp = pygame.image.load('road.png')
temp = pygame.transform.scale(temp, (500, 600))
roadImg = []
for i in range(2):
    roadImg.append(temp)

# score
score_value = 0
textX = 10
textY = 10
font = pygame.font.Font('Bubblegum.ttf', 32)

# game over
game_over_font = pygame.font.Font('Bubblegum.ttf', 64)


def show_score(x, y):
    score = font.render("SCORE : " + str(score_value), True, (255, 0, 0))
    screen.blit(score, (x, y))


def welc_text():
    text_font_1 = pygame.font.Font('moonstar.ttf', 64)
    text_1 = text_font_1.render("CAR GAME", True, (255, 50, 0))
    screen.blit(text_1, (400, 100))
    text_font_2 = pygame.font.Font('daily hours.ttf', 64)
    text_2 = text_font_2.render("CREATED BY: " + "DIPTA003", True, (0, 50, 255))
    screen.blit(text_2, (350, 170))
    text_font_3 = pygame.font.Font('Bubblegum.ttf', 36)
    text_3 = text_font_3.render("PRESS ENTER TO CONTINUE...", True, (0, 50, 255))
    screen.blit(text_3, (350, 490))


def welcome():
    exit_game = False

    while not exit_game:
        screen.fill((0, 255, 100))
        welc_text()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
        pygame.display.update()


def game_over_text():
    game_over_txt = game_over_font.render("GAME OVER", True, (200, 100, 255))
    screen.blit(game_over_txt, (500, 250))


def gameloop():
    # game specific variables
    exit_game = False
    game_over = False

    # player position and velocity
    player_x = 600
    player_y = 400
    player_vx = 0

    # enemy position and velocity
    enemy_x = [525, 675]
    enemy_y = [50 + 74, 50 + 74]
    enemy_vy = [0.2, 0.3]
    enemy_vy_change = 0

    # road position and velocity
    road_x = []
    road_y = []
    road_x.append(400)
    road_x.append(400)
    road_y.append(0)
    road_y.append(-600)
    road_vy = 0

    # score
    global score_value

    # game loop
    while not exit_game:
        if game_over:
            score_value = 0
            game_over_text()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            welcome()
                pygame.display.update()
        else:
            screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        player_vx = 0.5
                    if event.key == pygame.K_LEFT:
                        player_vx = -0.5
                    if event.key == pygame.K_UP:
                        player_vx = 0
                        road_vy += 2
                        enemy_vy_change += 2
                        score_value += 10 * road_vy
                if event.type == pygame.KEYUP:
                    player_vx = 0
                    road_vy = 0
                    enemy_vy_change = 0

            screen.fill((255, 255, 255))

            for i in range(2):
                screen.blit(roadImg[i], (road_x[i], road_y[i]))

            if not game_over:
                road_y[0] += 2 + road_vy
                road_y[1] += 2 + road_vy

                if road_y[0] > 0:
                    road_y[1] = road_y[0] - 600
                if road_y[1] > 0:
                    road_y[0] = road_y[0] - 600

            # draw the player
            player_x += player_vx
            if player_x > (900 - 74 - 125):
                player_x = 900 - 74 - 125
            elif player_x < (400 + 125):
                player_x = 400 + 125

            screen.blit(playerImg, (player_x, player_y))
            score_value += 1

            # draw enemy
            for i in range(2):
                enemy_y[i] += enemy_vy[i] + enemy_vy_change

            for i in range(2):
                if enemy_y[i] > (600 - 10):
                    enemy_x[i] = random.randint(400 + 125, 900 - 74 - 125)
                    enemy_y[i] = random.randint(0, 200)
                screen.blit(enemyImg[i], (enemy_x[i], enemy_y[i]))

            for i in range(2):
                if abs(player_x - enemy_x[i]) < (74 - 40) and abs(player_y - enemy_y[i]) < (74 - 10):
                    crash_sound = mixer.Sound('crash.wav')
                    crash_sound.play()
                    game_over = True
                    break

            show_score(textX, textY)
            pygame.display.update()


welcome()

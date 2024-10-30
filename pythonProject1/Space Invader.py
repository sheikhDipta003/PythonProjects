import pygame
import random
import math
from pygame import mixer

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (800, 600)).convert_alpha()

# background music
mixer.music.load('background.wav')
mixer.music.play(-1)

# title and icon
pygame.display.set_caption("SPACE INVADERS :)")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
pygame.display.update()

# player image
playerImg = pygame.image.load('player.png')

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemy_vx = []
enemy_vy = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 800 - 64))
    enemyY.append(random.randint(50, 150))
    enemy_vx.append(0.3)
    enemy_vy.append(40)

# bullet image and state
# ready ---> you can't see the bullet on the screen
# fire ---> the bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bullet_state = "ready"

# score
score_value = 0
textX = 10
textY = 10
font = pygame.font.Font('Bubblegum.ttf', 32)

# game over
game_over_font = pygame.font.Font('Bubblegum.ttf', 64)


def show_score(x, y):
    score = font.render("SCORE : " + str(score_value), True, (255, 255, 0))
    screen.blit(score, (x, y))


def game_over_text():
    game_over_txt = game_over_font.render("GAME OVER", True, (0, 255, 0))
    screen.blit(game_over_txt, (200, 250))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


def welc_text():
    text_font_1 = pygame.font.Font('moonstar.ttf', 64)
    text_1 = text_font_1.render("SPACE INVADERS", True, (255, 50, 0))
    screen.blit(text_1, (80, 100))
    text_font_2 = pygame.font.Font('daily hours.ttf', 64)
    text_2 = text_font_2.render("CREATED BY: " + "DIPTA003", True, (0, 50, 255))
    screen.blit(text_2, (130, 170))
    text_3 = font.render("PRESS ENTER TO CONTINUE...", True, (0, 50, 255))
    screen.blit(text_3, (180, 490))


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


def gameloop():
    game_over = False

    # player

    playerX = 370
    playerY = 500
    player_vx = 0

    # bullet initial condition
    bulletX = 0
    bulletY = 480
    bullet_vy = 1
    global bullet_state

    global score_value

    exit_game = False
    while not exit_game:
        if game_over:
            game_over_text()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_HOME:
                        welcome()
        else:
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        player_vx = 0.5
                    if event.key == pygame.K_LEFT:
                        player_vx = -0.5
                    if event.key == pygame.K_SPACE:
                        if bullet_state == "ready":
                            bullet_sound = mixer.Sound('laser.wav')
                            bullet_sound.play()
                            bulletX = playerX
                            fire_bullet(bulletX, bulletY)

                if event.type == pygame.KEYUP:
                    player_vx = 0

            playerX += player_vx

            if playerX <= 0:
                playerX = 0
            elif playerX >= (800 - 64):
                playerX = 800 - 64

            for i in range(num_of_enemies):

                if enemyY[i] > 440:
                    for j in range(num_of_enemies):
                        enemyY[i] = 2000
                    game_over = True
                    break
                enemyX[i] += enemy_vx[i]
                if enemyX[i] <= 0:
                    enemy_vx[i] = 0.3
                    enemyY[i] += enemy_vy[i]
                elif enemyX[i] >= (800 - 64):
                    enemy_vx[i] = -0.3
                    enemyY[i] += enemy_vy[i]

                # collision
                collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
                if collision:
                    explosion_sound = mixer.Sound('explosion.wav')
                    explosion_sound.play()
                    bulletY = 500
                    bullet_state = "ready"
                    score_value += 100
                    enemyX[i] = random.randint(0, 800 - 64)
                    enemyY[i] = random.randint(50, 150)

                enemy(enemyX[i], enemyY[i], i)

            # bullet movement
            if bulletY <= 0:
                bulletY = 500
                bullet_state = "ready"
            if bullet_state == "fire":
                fire_bullet(bulletX, bulletY)
                bulletY -= bullet_vy

            player(playerX, playerY)
            show_score(textX, textY)
        pygame.display.update()

    pygame.quit()
    quit()


welcome()

import math
import pygame
import time
from pygame import mixer

# initialize pygame
pygame.init()

# background
screen = pygame.display.set_mode((1200, 600))
mixer.music.load('background.mp3')
mixer.music.play(-1)

# caption and icon
# set caption and icon
pygame.display.set_caption("DX BALL")
icon = pygame.image.load('background.png')
pygame.display.set_icon(icon)
pygame.display.update()

# player image/ paddle(100 / 25 px)
paddle_img = []
# first
img = pygame.image.load('paddle.png')
img = pygame.transform.scale(img, (100, 25))
paddle_img.append(img)
# second
img = pygame.image.load('paddle_wide.png')
img = pygame.transform.scale(img, (200, 25))
paddle_img.append(img)
paddle_base = [100, 200]
paddle_height = [25, 25]


# ball image
ball_img = pygame.image.load('ball.png')
ball_img = pygame.transform.scale(ball_img, (15, 15))

# some color constants
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
color = (red, blue, green)

# tiles' size
base = 60
height = 30

# score
score_value = 0
textX = 10
textY = 10
font = pygame.font.Font('Bubblegum.ttf', 32)

# game over
game_over_font = pygame.font.Font('Bubblegum.ttf', 64)

# time
time_value = 0
textX_t = 10
textY_t = 40
# perk items:
# i = 3, j = 6 ---> wider paddle
# i = 0, j = 11 ---> extra life
perk_1_img = pygame.image.load('perk_wide_paddle.png')
perk_1_img = pygame.transform.scale(perk_1_img, (15, 15))
perk_2_img = pygame.image.load('extra_life.png')
perk_2_img = pygame.transform.scale(perk_2_img, (15, 15))


def game_over_text():
    game_over_txt = game_over_font.render("GAME OVER", True, (255, 100, 255))
    screen.blit(game_over_txt, (450, 300))


def show_score(x, y):
    score = font.render("SCORE : " + str(score_value), True, (255, 0, 0))
    screen.blit(score, (x, y))


def show_time(x, y):
    Time = font.render("TIME : " + str(time_value), True, (255, 0, 0))
    screen.blit(Time, (x, y))


def welc_text():
    text_font_1 = pygame.font.Font('moonstar.ttf', 64)
    text_1 = text_font_1.render("DX BALL", True, (255, 50, 0))
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


def draw_tiles(x, y, base, height, color):
    pygame.draw.rect(screen, color, (x, y, base, height))


def find_dist(x1, y1, x2, y2):
    return math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))


def isCollision(ball_x, ball_y, tile_x, tile_y):
    if find_dist(ball_x, ball_y, tile_x, tile_y) < 30:
        return True
    else:
        return False


def gameloop():
    # timer
    start_timer = time.time()

    # game specific variables
    exit_game = False
    game_over = False
    global score_value
    global time_value
    num_of_death = 0

    # paddle coordinates
    paddle_x = 500
    paddle_y = 525
    paddle_vx = 0
    img_no = 0

    # ball coordinates
    ball_x = 525
    ball_y = 510
    ball_vx = 0
    ball_vy = 0
    ball_state = "ready"

    # tiles
    tile = []
    for i in range(10):
        for j in range(20):
            head = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        tile.append(head)
    # perks
    wide_paddle_x = base * 6 + 10
    wide_paddle_y = height * 3 + 10
    xtra_life_x = base * 11 + 10
    xtra_life_y = height * 0 + 10

    while not exit_game:
        if game_over:
            game_over_text()
            score_value = 0
            time_value = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                else:
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
                        paddle_vx = 1
                    if event.key == pygame.K_LEFT:
                        paddle_vx = -1
                if event.type == pygame.KEYUP:
                    paddle_vx = 0
                if event.type == pygame.MOUSEMOTION:
                    if pygame.mouse.get_pos()[1] >= 300:
                        paddle_x = pygame.mouse.get_pos()[0]
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if ball_state == "ready" and pygame.mouse.get_pressed() == (1, 0, 0):
                        ball_state = "fire"
                        if pygame.mouse.get_pos()[0] > ball_x:
                            ball_vx = 1
                        elif pygame.mouse.get_pos()[0] < ball_x:
                            ball_vx = -1
                        else:
                            ball_vx = 0
                        ball_vy = -1

            paddle_x += paddle_vx
            if ball_state == "ready":
                ball_x = paddle_x + 42
            elif ball_state == "fire":
                if ball_x >= (1200 - 15):
                    ball_vx = -ball_vx
                elif ball_x <= 0:
                    ball_vx = -ball_vx
                elif ball_y <= 0:
                    ball_vy = -ball_vy
                elif (ball_x + 15 > paddle_x) and (ball_x < (paddle_x + 100)) and (ball_y + 15) > paddle_y:
                    ball_vy = -ball_vy
                elif (ball_y + 15) > 600:
                    if ball_y < 600:
                        num_of_death += 1
                    if num_of_death >= 3:
                        game_over = True
                        num_of_death = 0
                        ball_state = "undefined"
                        ball_y = 10000
                    else:
                        pygame.time.delay(1000)
                        # re-initialize
                        paddle_x = 500
                        paddle_y = 525
                        paddle_vx = 0
                        ball_x = 525
                        ball_y = 510
                        ball_vx = 0
                        ball_vy = 0
                        ball_state = "ready"

            if paddle_x > (1200 - paddle_base[img_no]):
                paddle_x = 1200 - paddle_base[img_no]
            elif paddle_x < 0:
                paddle_x = 0

            ball_x += ball_vx
            ball_y += ball_vy
            screen.blit(ball_img, (ball_x, ball_y))

            # perks
            if paddle_y - 15 < wide_paddle_y < (paddle_y + 25) and paddle_x - 15 < wide_paddle_x < (paddle_x + 100):
                img_no = 1
                bonus_sound = mixer.Sound('shimmer_1.wav')
                bonus_sound.set_volume(0.1)
                bonus_sound.play()
            if paddle_y - 15 < xtra_life_y < (paddle_y + 25) and paddle_x - 15 < xtra_life_x < (paddle_x + 100):
                num_of_death -= 1
                xtra_life_x = 10000
                xtra_life_y = 1000
                bonus_sound = mixer.Sound('shimmer_1.wav')
                bonus_sound.set_volume(0.1)
                bonus_sound.play()

            screen.blit(paddle_img[img_no], (paddle_x, paddle_y))

            # draw tiles
            temp = 9
            k = 0
            for i in range(10):
                for j in range(20):
                    if (i + j) > 7 and i >= k:
                        # collision
                        if isCollision(ball_x, ball_y, base * j, height * i):
                            tile[i][j] = 1
                            score_value += 10
                            explosion_sound = mixer.Sound('explosion03.wav')
                            explosion_sound.set_volume(0.1)
                            explosion_sound.play()

                        if tile[i][j] == 0:
                            draw_tiles(base * j, height * i, base, height, color[(i + j) % 3])
                        else:
                            draw_tiles(1000, 2000, base, height, black)

                            if i == 3 and j == 6:     # wider paddle
                                wide_paddle_y += 1
                            elif i == 0 and j == 11:     # extra life
                                xtra_life_y += 1

                        if (i + j) - temp == 2:
                            k += 1
                            temp = i + j

            show_score(textX, textY)

            end_timer = time.time()
            time_value = int(end_timer - start_timer)
            show_time(textX_t, textY_t)
            screen.blit(perk_1_img, (wide_paddle_x, wide_paddle_y))
            screen.blit(perk_2_img, (xtra_life_x, xtra_life_y))
            pygame.display.update()


welcome()

import pygame
import os
import random

pygame.init()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screen_width = 900
screen_height = 600

gamewindow = pygame.display.set_mode((screen_width, screen_height))

# background image
bgimg = pygame.image.load("img.png")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

pygame.display.set_caption("SnakeGame :o")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])


def plot_snake(gamewindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill(white)
        text_screen("Welcome to snakes", black, 200, 300)
        text_screen("Press Space Bar to Continue", black, 350, 530)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(60)


def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_vx = 0
    snake_vy = 0
    snake_size = 10
    init_speed = 5
    fps = 30

    # check if the file exists
    if not os.path.exists("highScore.txt"):
        with open("highScore.txt", "w") as f:
            f.write("0")
    with open("highScore.txt", "r") as f:
        highscore = f.read()

    food_x = random.randint(20, screen_width - 100)
    food_y = random.randint(20, screen_height - 100)

    score = 0

    snake_list = []
    snake_len = 1

    while not exit_game:
        if game_over:
            with open("highScore.txt", "w") as f:
                f.write(str(highscore))
            gamewindow.fill(white)
            text_screen("Game Over!! Press Enter to Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            welcome()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        snake_vx = init_speed
                        snake_vy = 0

                    if event.key == pygame.K_LEFT:
                        snake_vx = -init_speed
                        snake_vy = 0

                    if event.key == pygame.K_UP:
                        snake_vy = -init_speed
                        snake_vx = 0

                    if event.key == pygame.K_DOWN:
                        snake_vy = init_speed
                        snake_vx = 0

            snake_x += snake_vx
            snake_y += snake_vy

            if abs(snake_x - food_x) <= snake_size and abs(snake_y - food_y) <= snake_size:
                score += 10
                food_x = random.randint(20, screen_width - 100)
                food_y = random.randint(20, screen_height - 100)
                snake_len += 5
                if score > int(highscore):
                    highscore = score

            gamewindow.fill(white)
            gamewindow.blit(bgimg, (0, 0))
            text_screen("Score : " + str(score) + "   High Score : " + str(highscore), red, 5, 5)
            pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])

            head = [snake_x, snake_y]
            snake_list.append(head)

            if len(snake_list) > snake_len:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gamewindow, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()

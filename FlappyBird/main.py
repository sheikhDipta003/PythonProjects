import pygame
import random

pygame.init()

# define font and colors
font = pygame.font.SysFont('Bauhaus 93', 60)
white = (255, 255, 255)

# create a clock to control the frame rate and the speed of scrolling ground image thereby.
clock = pygame.time.Clock()
fps = 60

# window variables
screen_width = 700
screen_height = 700

# game variables
run = True
offset_bg_height = 100  # offset of the height of the background image from screen_height.
ground_scroll = 0  # position of the top-left corner of the ground image which will change with scrolling.
scroll_speed = 4  # speed of scrolling the ground image.
reset_ground_thresh = 35  # threshold value, after crossing which the ground image's position ground_scroll
# will be reset to 0 so that it will create the impression of a moving ground.

pipe_gap = 150  # gap between a top pipe and a bottom pipe
pipe_period = 1500  # A pair of pipes will appear after every 1500 milliseconds.
last_pipe = pygame.time.get_ticks() - pipe_period
# Stores the time when the last pipe was created. At the beginning, only a pair of pipes will be created. get_ticks()
# returns the current time; in this case, the time of the start of the game. If "pipe_period" is not subtracted, the
# pipes will start appearing only after 1.5 seconds has passed since the start of the game.

score = 0
pass_pipe = False

flying = False  # The bird is not initially in the flying state
game_over = False

# create window and set caption
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# load images
# Too large images have been resized with the help of pygame.transform.scale().
bg = pygame.transform.scale(pygame.image.load('images/bg.png'), (screen_width, screen_height - offset_bg_height))
ground = pygame.transform.scale(pygame.image.load('images/ground.png'), (screen_width, offset_bg_height))
restart_img = pygame.image.load('images/restart.png')


# function to convert a text into an image
def draw_text(text, a_font, text_color, x, y):
    img = a_font.render(text, True, text_color)  # converts the text into an image of color text_color
    screen.blit(img, (x, y))


# The score returned here is a local variable which is, later in the game-loop, assigned to the global score variable.
# The reason for that is- in python, global vars cannot be modified in local scope directly. If we wanted to modify,
# we would have to set 'score' as global var in the function; an approach that should be avoided in professional
# pygame. So, instead, we are just returning the local 'score' var and modifying the global 'score' var with the help
# of it.
def reset_game():
    pipe_group.empty()  # empties the pipe_group
    flappy.rect.x = 80
    flappy.rect.y = screen_height // 2
    score = 0
    return score


# Bird class
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []  # Empty list that will be containing all the sprites
        self.index = 0  # Index of the image from the list that is to be drawn currently
        self.counter = 0  # Controls the speed of animation

        for num in range(1, 4):
            img = pygame.image.load(f'images/bird{num}.png')
            self.images.append(img)

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False

    def update(self):
        # handle gravity
        if flying:
            self.vel += 0.5
            if self.vel > 8:  # Impose an upper limit on self.vel so that it does not go on increasing continuously.
                self.vel = 8
            if self.rect.bottom < (screen_height - offset_bg_height):
                self.rect.y += self.vel

        if not game_over:
            # handle jump
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.vel = -6
                self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0 and self.clicked:
                self.vel = -6
                self.clicked = False

            # handle the animation
            self.counter += 1
            flap_cooldown = 5  # Number of iterations through the sprites after which counter will be set to 0
            # and the next sprite will be displayed.

            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):  # Checking if the index is crossing the available sprites
                    self.index = 0

            self.image = self.images[self.index]  # loading the updated image/sprite

            # rotation of image according to the direction of flight of the bird
            # The second argument is the angle of rotation, which will be anti-clockwise when positive.
            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
        else:
            # rotate the bird so that it faces downward to give the impression of a dead bird
            self.image = pygame.transform.rotate(self.images[self.index], -90)


# Pipe class
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/pipe.png")
        self.rect = self.image.get_rect()
        # position 1 is from the top, position -1 is from the bottom
        if position == 1:
            # <src img>, <flip horizontally>, <flip vertically>
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - pipe_gap // 2]
        if position == -1:
            self.rect.topleft = [x, y + pipe_gap // 2]

    def update(self):
        self.rect.x -= scroll_speed
        # If a pair of pipes has crossed the left boundary, then remove them from the game memory so that they do not
        # continue updating unnecessarily.
        if self.rect.right < 0:
            self.kill()


# button class
class Button:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))  # draw the restart button
        action = False  # confirms if the mouse is over 'restart' button and it has been clicked
        pos = pygame.mouse.get_pos()  # returns a list containing x and y coordinate of mouse position
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:  # if the left mouse button has been pressed
                action = True

        return action


# create an instance of button class
restart = Button(restart_img, screen_width // 2 - 50, screen_height // 2 - 80)

# Create an instance of Bird class; in other words, create a "bird sprite".
flappy = Bird(80, screen_height // 2)
# bird_group keeps track of all the sprites of the bird. Essentially, it is a python list.
bird_group = pygame.sprite.Group()
bird_group.add(flappy)
# pipe_group keeps track of all the sprites of the pipe. Essentially, it is a python list.
pipe_group = pygame.sprite.Group()

while run:
    # the clock will tick at the rate of given fps
    clock.tick(fps)

    # drawing background image; blit() places the image on the game window by putting the top-left corner of the image
    # in (0, 0) position of game window.
    screen.blit(bg, (0, 0))

    # draw the bird and update its state
    bird_group.draw(screen)
    bird_group.update()

    # draw the pipe and update its state
    pipe_group.draw(screen)

    # draw the ground
    screen.blit(ground, (ground_scroll, screen_height - offset_bg_height))

    # check the score
    if len(pipe_group) > 0:  # if at least one pipe has been created
        if bird_group.sprites()[0].rect.left >= pipe_group.sprites()[0].rect.left \
                and bird_group.sprites()[0].rect.right <= pipe_group.sprites()[0].rect.right \
                and not pass_pipe:
            pass_pipe = True
        if pass_pipe:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                pass_pipe = False
                score += 1
    # print(score)
    draw_text(str(score), font, white, screen_width // 2, 20)

    # check if the bird has hit any pipe
    # groupcollide(<first-group>, <second-group>, <delete-first-group-upon-collision?>, <delete-second-group?>)
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
        game_over = True

    # Check if bird has hit the ground
    if flappy.rect.bottom >= (screen_height - offset_bg_height):
        game_over = True
        flying = False

    # scroll the ground when game is not over
    if not game_over and flying:

        # generate pipes
        time_now = pygame.time.get_ticks()  # get the current time
        if time_now - last_pipe > pipe_period:
            # controls the height of both the pipes
            pipe_height = random.randint(-100, 100)

            # Create two instances of Pipe class; in other words, create two "pipe sprites".
            btm_pipe = Pipe(screen_width, screen_height // 2 + pipe_height, -1)
            top_pipe = Pipe(screen_width, screen_height // 2 + pipe_height, 1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now

        ground_scroll -= scroll_speed  # Move the ground image to the left by 4 pixels with each game loop.
        if abs(ground_scroll) > reset_ground_thresh:
            ground_scroll = 0

        pipe_group.update()

    # check if The game is over and reset the game
    if game_over:
        if restart.draw():
            # print('clicked')
            game_over = False
            score = reset_game()    # returns 0, which is set to global 'score' var

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not flying and not game_over:
            flying = True

    pygame.display.update()
    # Updates all the changes happening above this line in every game loop.

pygame.quit()

import pygame
import random

#################################################################
# initialize (MUST)

pygame.init() #initialize(MUST)

# set screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# set title
pygame.display.set_caption('DDong Game')

#FPS
clock = pygame.time.Clock()
#################################################################

# 1. user game init(background image, game image, position, speed, font, etc..)
# background
background = pygame.image.load('C:\\_workspace\\girihan.github.io\\python\\pygame_basic\\background.png')
# character
character = pygame.image.load('C:\\_workspace\\girihan.github.io\\python\\pygame_basic\\character.png')
character_size = character.get_rect().size # image size
character_width = character_size[0] # character width
character_height = character_size[1] # character height
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height

# ddong
ddong = pygame.image.load('C:\\_workspace\\girihan.github.io\\python\\pygame_basic\\enemy.png')
ddong_size = ddong.get_rect().size # image size
ddong_width = ddong_size[0] # ddong width
ddong_height = ddong_size[1] # ddong height
ddong_x_pos = 0
ddong_y_pos = 0

# move position
to_x = 0

# move speed
character_speed = 0.6
ddong_speed = 0.5

# event loop
running = True
while running:
    dt = clock.tick(30) # set fps

    # 2. handling event(keyboard, mouse, etc )
    for event in pygame.event.get(): # what kind of event is occurred??
        if event.type == pygame.QUIT: # if close windoe event is occurred??
            running = False # end game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. character position handling
    character_x_pos += to_x * dt
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # ddong position
    ddong_y_pos += ddong_speed * dt

    # 4. collision handling
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    # check collision
    if character_rect.colliderect(ddong_rect):
        print('collision!!')
        running = False

    # 5. draw screen
    screen.blit(background, (0,0)) # draw background
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))
    # update screen
    pygame.display.update()
    
    # reset ddong position
    if ddong_y_pos + ddong_height >= screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, (screen_width - ddong_width))

# pause
pygame.time.delay(2000) # delay 2 sec

# exit pygame
pygame.quit()
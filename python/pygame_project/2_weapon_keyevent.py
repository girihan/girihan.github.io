import os
import pygame

#################################################################
# initialize (MUST)

pygame.init() #initialize(MUST)

# set screen size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# set title
pygame.display.set_caption('Nado Pang')

#FPS
clock = pygame.time.Clock()
#################################################################

# 1. user game init(background image, game image, position, speed, font, etc..)
current_path = os.path.dirname(__file__) # return current position
image_path = os.path.join(current_path, 'images')

# background
background = pygame.image.load(os.path.join(image_path, 'background.png'))

# stage
stage = pygame.image.load(os.path.join(image_path, 'stage.png'))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# character
character = pygame.image.load(os.path.join(image_path, 'character.png'))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - stage_height - character_height

# character move
character_to_x = 0
# character speed
character_speed = 5

# weapon
weapon = pygame.image.load(os.path.join(image_path, 'weapon.png'))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# multiple shot
weapons = []

# weapon speed
weapon_speed = 10


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
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. character position handling
    character_x_pos += character_to_x
    if character_x_pos < 0: 
        character_x_pos = 0
    if character_x_pos > screen_width - character_width: 
        character_x_pos = screen_width - character_width

    # weapon position
    # 100, 200 -> 180, 160, 140, ...
    # 500, 200 -> 180, 160, 140, ...
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # weapon postion will be going up
    # remove weapon when touch upper
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    
    # 4. collision handling

    # 5. draw screen
    screen.blit(background, (0,0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    # update screen
    pygame.display.update()


# pause
pygame.time.delay(2000) # delay 2 sec

# exit pygame
pygame.quit()

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

# event loop
running = True
while running:
    dt = clock.tick(30) # set fps
    
    # 2. handling event(keyboard, mouse, etc )
    for event in pygame.event.get(): # what kind of event is occurred??
        if event.type == pygame.QUIT: # if close windoe event is occurred??
            running = False # end game
        
    # 3. character position handling

    # 4. collision handling

    # 5. draw screen
    screen.blit(background, (0,0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    # update screen
    pygame.display.update()


# pause
pygame.time.delay(2000) # delay 2 sec

# exit pygame
pygame.quit()
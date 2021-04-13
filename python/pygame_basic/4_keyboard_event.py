import pygame

pygame.init() #initialize(MUST)

# set screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# set title
pygame.display.set_caption('Nado Game')

# load background image
background = pygame.image.load('C:\\_workspace\\girihan.github.io\\python\\pygame_basic\\background.png')

# load character(stripe)
character = pygame.image.load('C:\\_workspace\\girihan.github.io\\python\\pygame_basic\\character.png')
character_size = character.get_rect().size # image size
character_width = character_size[0] # character width
character_height = character_size[1] # character height
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height


to_x = 0
to_y = 0

# event loop
running = True
while running:
    for event in pygame.event.get(): # what kind of event is occurred??
        if event.type == pygame.QUIT: # if close windoe event is occurred??
            running = False # end game
        
        if event.type == pygame.KEYDOWN: # check if key is pressed
            if event.key == pygame.K_LEFT:
                to_x -= 5
            if event.key == pygame.K_RIGHT:
                to_x += 5
            if event.key == pygame.K_UP:
                to_y -= 5
            if event.key == pygame.K_DOWN:
                to_y += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    #screen.fill((0,0,255))
    screen.blit(background, (0,0)) # draw background
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()

# exit pygame
pygame.quit()
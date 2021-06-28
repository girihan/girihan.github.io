import pygame

pygame.init() #initialize(MUST)

# set screen size
screen_with = 480
screen_height = 640
screen = pygame.display.set_mode((screen_with, screen_height))

# set title
pygame.display.set_caption('Nado Game')

# load background image
background = pygame.image.load('C:\\_workspace\\girihan.github.io\\python\\pygame_basic\\background.png')

# event loop
running = True
while running:
    for event in pygame.event.get(): # what kind of event is occurred??
        if event.type == pygame.QUIT: # if close windoe event is occurred??
            running = False # end game

    #screen.fill((0,0,255))
    screen.blit(background, (0,0)) # draw background
    
    pygame.display.update()

# exit pygame
pygame.quit()
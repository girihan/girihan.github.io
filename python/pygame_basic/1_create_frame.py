import pygame

pygame.init() #initialize(MUST)

# set screen size
screen_with = 480
screen_height = 640
screen = pygame.display.set_mode((screen_with, screen_height))

# set title
pygame.display.set_caption('Nado Game')

# event loop
running = True
while running:
    for event in pygame.event.get(): # what kind of event is occurred??
        if event.type == pygame.QUIT: # if close windoe event is occurred??
            running = False

# exit pygame
pygame.quit()
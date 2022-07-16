import pygame
import random 
import sys
import pygame.locals

#Intialize pygame
pygame.init()

#Window size
window_width = 800
window_height = 403

#Creates game screen
screen = pygame.display.set_mode((window_width,window_height))

#Title & Icon
pygame.display.set_caption("Word Game")
icon = pygame.image.load('puzzle.png')
pygame.display.set_icon(icon)

#Background
background = pygame.image.load('backgroundVS.png') 


#Game Loop
running = True
while running:

    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

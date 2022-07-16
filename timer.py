import pygame
import random 
import sys
import pygame.locals

#Intialize pygame
pygame.init()

#Window size
window_width = 800
window_height = 534

#Creates game screen
screen = pygame.display.set_mode((window_width,window_height))

#Title & Icon
pygame.display.set_caption("Word Game")
icon = pygame.image.load('puzzle.png')
pygame.display.set_icon(icon)

#Background
background = pygame.image.load('background.png') 
clock = pygame.time.Clock()

counter, text = 60, 'Time: 60'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

#Game Loop
running = True
while running:

    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: 
            counter -= 1
            text = "Time:" +str(counter).rjust(3) if counter > 0 else 'Game Over!'
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(font.render(text, True, (255, 255, 255)), (650, 48))
    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()



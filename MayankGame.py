import pygame
import random 
import sys
import pygame.locals

#Intialize pygame
pygame.init()

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.display.set_caption("Horse hurdeler")


#ground
ground = pygame.image.load("assets/ground.png")
ground_rect = ground.get_rect(center=(640,400))

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("white")
    
    pygame.display.update()
    clock.tick(120)
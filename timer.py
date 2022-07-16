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
clock = pygame.time.Clock()



counter, text = 60, 'Time: 60'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

#Buttons
rows = 1
cols = 7
gap = 20
size = 50
boxes = []

#color
white = (255,255,255)
black = (0,0,0)

for row in range(rows):
    for col in range(cols):
        x = ((col * gap) + gap) + (size * col) + 140
        y = ((row * gap) + gap) + (size * row) + 300
        box = pygame.Rect(x,y,size,size)
        boxes.append(box)



buttons = []
A = 65


for ind, box in enumerate(boxes):
    letter = chr(A+ind)
    button = [box, letter]
    buttons.append(button)

btn_font = pygame.font.SysFont('arial', 3)
#Game Loop
running = True

while True:

    while running:

        screen.blit(background, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT: 
                counter -= 1
                text = "Time:" +str(counter).rjust(3) if counter > 0 else 'Game Over!'
            if event.type == pygame.QUIT:
                running = False
        
        screen.blit(font.render(text, True, (255, 255, 255)), (650, 20))
        pygame.display.flip()
        for box, letter in buttons:
            btn_text = btn_font.render(letter, True, black)
            btn_rect = btn_text.get_rect(center = (box.x + 20, box.y +20))
            screen.blit(btn_text, btn_rect)
            pygame.draw.rect(screen, black, box, 2)

        clock.tick(60)
        pygame.display.update()



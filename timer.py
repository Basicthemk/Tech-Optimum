from tkinter import N
from numpy import c_
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

#Loading Alphabets
a_image = pygame.image.load('Alphabets/A.png') 
b_image = pygame.image.load('Alphabets/B.png') 
c_image = pygame.image.load('Alphabets/C.png') 
d_image = pygame.image.load('Alphabets/D.png') 
e_image = pygame.image.load('Alphabets/E.png') 
f_image = pygame.image.load('Alphabets/F.png') 
g_image = pygame.image.load('Alphabets/G.png') 
h_image = pygame.image.load('Alphabets/H.png') 
i_image = pygame.image.load('Alphabets/I.png') 
j_image = pygame.image.load('Alphabets/J.png') 
k_image = pygame.image.load('Alphabets/K.png') 
l_image = pygame.image.load('Alphabets/L.png') 
m_image = pygame.image.load('Alphabets/M.png') 
n_image = pygame.image.load('Alphabets/N.png') 
o_image = pygame.image.load('Alphabets/O.png') 
p_image = pygame.image.load('Alphabets/P.png') 
q_image = pygame.image.load('Alphabets/Q.png') 
r_image = pygame.image.load('Alphabets/R.png') 
s_image = pygame.image.load('Alphabets/S.png') 
t_image = pygame.image.load('Alphabets/T.png') 
u_image = pygame.image.load('Alphabets/U.png') 
v_image = pygame.image.load('Alphabets/V.png') 
w_image = pygame.image.load('Alphabets/W.png') 
x_image = pygame.image.load('Alphabets/X.png') 
y_image = pygame.image.load('Alphabets/Y.png') 
z_image = pygame.image.load('Alphabets/Z.png') 




def select_letters():
    store_letters = []
    vowels = [a_image, e_image, i_image, o_image, u_image]
    consonants = [b_image, c_image, d_image, f_image, g_image, h_image, j_image, k_image, l_image, m_image, n_image, p_image, q_image, r_image, s_image, t_image, v_image, w_image, x_image, y_image, z_image]
    while len(store_letters) != 2:
        v_select = random.choice(vowels)
        if v_select not in store_letters:
            store_letters.append(v_select)
    while len(store_letters) != 7:
        c_select = random.choice(consonants)
        if c_select not in store_letters:
            store_letters.append(c_select)



#Timer Counter
counter, text = 60, 'Time: 60'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

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
            #If keystroke is pressed, check what it is
            if event.type  == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    screen.blit(a_image, (50,25))
                if event.key == pygame.K_b:
                    print('b')
                if event.key == pygame.K_c:
                    print('c')
                if event.key == pygame.K_d:
                    print('A')
                if event.key == pygame.K_e:
                    print('b')
                if event.key == pygame.K_f:
                    print('c')
                if event.key == pygame.K_g:
                    print('A')
                if event.key == pygame.K_h:
                    print('b')
                if event.key == pygame.K_i:
                    print('c')
                if event.key == pygame.K_j:
                    print('A')
                if event.key == pygame.K_k:
                    print('b')
                if event.key == pygame.K_l:
                    print('c')
                if event.key == pygame.K_m:
                    print('A')
                if event.key == pygame.K_n:
                    print('b')
                if event.key == pygame.K_o:
                    print('c')
                if event.key == pygame.K_p:
                    print('A')
                if event.key == pygame.K_q:
                    print('b')
                if event.key == pygame.K_r:
                    print('c')
                if event.key == pygame.K_s:
                    print('A')
                if event.key == pygame.K_t:
                    print('b')
                if event.key == pygame.K_u:
                    print('c')
                if event.key == pygame.K_v:
                    print('A')
                if event.key == pygame.K_w:
                    print('b')
                if event.key == pygame.K_x:
                    print('c')
                if event.key == pygame.K_y:
                    print('A')
                if event.key == pygame.K_z:
                    print('b')

        screen.blit(font.render(text, True, (255, 255, 255)), (620, 20))
        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()



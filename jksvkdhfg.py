import pygame
import os
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('game')

WHITE = (255, 255, 255)
BLACK = (0,0,0)

x = 200
y = 200

width = 20
height = 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  
                current_game = "shop"
                os.system("python shop.py")

    screen.fill(WHITE)
    pygame.display.flip()

pygame.quit()
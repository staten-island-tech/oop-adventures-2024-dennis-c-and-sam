import pygame
import subprocess
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

x = 200
y = 200

width = 20
height = 20

font = pygame.font.Font(None, 36)  # Initialize font
text = ""  # Initialize text variable

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                text = "You pressed 1"  # Set text when "1" is pressed
                current_game = "shop"
                subprocess.Popen(["python", "shop.py"])

    screen.fill(WHITE)
    
    if text:
        rendered_text = font.render(text, True, BLACK)
        screen.blit(rendered_text, (x, y))  # Display text on screen

    pygame.display.flip()

pygame.quit()
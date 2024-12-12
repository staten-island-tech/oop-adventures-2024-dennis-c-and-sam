import pygame
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

vel=5

# Variable to keep our game loop running 
running = True
  
# game loop 
while running: 
    
# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False

    keys = pygame.key.get_pressed() 
	
	# if left arrow key is pressed 
    if keys[pygame.K_a] and x>0: 
		
		# decrement in x co-ordinate 
		    x -= vel 
		
	# if left arrow key is pressed 
    if keys[pygame.K_d] and x<500-width: 
		
		# increment in x co-ordinate 
		    x += vel 
		
	# if left arrow key is pressed 
    if keys[pygame.K_w] and y>0: 
		
		# decrement in y co-ordinate 
		    y -= vel 
		
	# if left arrow key is pressed 
    if keys[pygame.K_s] and y<500-height: 
		# increment in y co-ordinate 
		    y += vel 
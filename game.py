import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Your vision")
exit = False
paused = False
#displays https://stackoverflow.com/questions/47803512/wall-collision-in-pygame
WallColor = (67,64,64)
UserColor = (78,82,124)
ButtonColor = (255,255,255)
ButtonLightUp = ()
Menutext = pygame.font.SysFont('Corbel',20) .render('menu' , True , ButtonColor)
width = screen.get_width() 
height = screen.get_height()
UserX = 305

UserY = 307

playerhitbox = (UserX,UserY)



#https://electronstudio.github.io/pygame-zero-book/chapters/maze.html 

while not exit:
    pygame.time.Clock().tick(60)  
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
            
    class GameLog:
        def movement():
            global UserX
            global UserY

            screen.fill((0,0,0))
            pygame.draw.circle(screen, UserColor,(UserX,UserY),5,0)
            if pygame.key.get_pressed()[K_LEFT]:
                LastX = UserX
                UserX -= 1
            if pygame.key.get_pressed()[K_RIGHT]:
                LastX = UserX
                UserX += 1
            if pygame.key.get_pressed()[K_UP]:
                LastY = UserY
                UserY -= 1
            if pygame.key.get_pressed()[K_DOWN]:
                LastY = UserY
                UserY += 1
        def button():
            pygame.draw.rect(screen,ButtonColor, pygame.Rect(545,5,50,25),1)
            screen.blit(Menutext , (547,7))
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if 545 <= pygame.mouse.get_pos()[0] <= 545 + 50 and 5 <= pygame.mouse.get_pos()[1] <= 5 + 25:
                    global paused
                    paused = True
        def gamePaused():
            global paused
            if paused == True:

                screen.blit(pygame.font.SysFont('Corbel',40) .render('Paused' , True , ButtonColor), (240,100))
                screen.blit(pygame.font.SysFont('Corbel',40) .render('Resume' , True , ButtonColor), (233,165))
                pygame.draw.rect(screen, ButtonColor, pygame.Rect(220,160,150,50),1)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 220 <= pygame.mouse.get_pos()[0] <= 220 + 150 and 160 <= pygame.mouse.get_pos()[1] <= 160 + 50:
                        paused = False
        def walls():
            global UserX
            global UserY
            maze = [
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1, 2, 0, 1],
                [1, 0, 1, 0, 1, 1, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 1],
                [1, 0, 1, 0, 1, 0, 0, 1],
                [1, 0, 1, 0, 1, 0, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1]
            ]  
            if  75 => UserX, < 75 and 0 => UserY > y:  
                position = maze[0][0]
            if  150 => UserX, < 150 and 0 => UserY > y:
                UserY -= 1
            if  225 => UserX, < 225 and 0 => UserY > y:
                UserY -= 1
            if  300 => UserX, < 300 and 0 => UserY > y:
                UserY -= 1
            if  375 => UserX, < 375 and 0 => UserY > y:
                UserY -= 1
            if  450 => UserX, < 450 and 0 => UserY > y:
                UserY -= 1
            if  525 => UserX, < 525 and 0 => UserY > y:
                UserY -= 1
            if  600 => UserX, < 600 and 0 => UserY > y:
                UserY -= 1
            if  0 => UserX, < 0 and -75 => UserY > y:  
                
            if  75 => UserX, < 75 and 75 => UserY > y:
            if  150 => UserX, < 150 and 75 => UserY > y:
            if  225 => UserX, < 225 and 75 => UserY > y:
            if  300 => UserX, < 300 and 75 => UserY > y:
            if  375 => UserX, < 375 and 75 => UserY > y:
            if  450 => UserX, < 450 and 75 => UserY > y:
            if  525 => UserX, < 525 and 75 => UserY > y:
            if  600 => UserX, < 600 and 75 => UserY > y:
            if  0 => UserX, < 0 and 150 => UserY > y:
            if  75 => UserX, < 75 and 150 => UserY > y:
            if  150 => UserX, < 150 and 150 => UserY > y:
            if  225 => UserX, < 225 and 150 => UserY > y:
            if  300 => UserX, < 300 and 150 => UserY > y:
            if  375 => UserX, < 375 and 150 => UserY > y:
            if  450 => UserX, < 450 and 150 => UserY > y:
            if  525 => UserX, < 525 and 150 => UserY > y:
            if  600 => UserX, < 600 and 150 => UserY > y:
            if  0 => UserX, < 0 and 225 => UserY > y:
            if  75 => UserX, < 75 and 225 => UserY > y:
            if  150 => UserX, < 150 and 225 => UserY > y:
            if  225 => UserX, < 225 and 225 => UserY > y:
            if  300 => UserX, < 300 and 225 => UserY > y:
            if  375 => UserX, < 375 and 225 => UserY > y:
            if  450 => UserX, < 450 and 225 => UserY > y:
            if  525 => UserX, < 525 and 225 => UserY > y:
            if  600 => UserX, < 600 and 225 => UserY > y:
            if  0 => UserX, < 0 and 300 => UserY > y:
            if  75 => UserX, < 75 and 300 => UserY > y:
            if  150 => UserX, < 150 and 300 => UserY > y:
            if  225 => UserX, < 225 and 300 => UserY > y:
            if  300 => UserX, < 300 and 300 => UserY > y:
            if  375 => UserX, < 375 and 300 => UserY > y:
            if  450 => UserX, < 450 and 300 => UserY > y:
            if  525 => UserX, < 525 and 300 => UserY > y:
            if  600 => UserX, < 600 and 300 => UserY > y:
            if  0 => UserX, < 0 and 375 => UserY > y:
            if  75 => UserX, < 75 and 375 => UserY > y:
            if  150 => UserX, < 150 and 375 => UserY > y:
            if  225 => UserX, < 225 and 375 => UserY > y:
            if  300 => UserX, < 300 and 375 => UserY > y:
            if  375 => UserX, < 375 and 375 => UserY > y:
            if  450 => UserX, < 450 and 375 => UserY > y:
            if  525 => UserX, < 525 and 375 => UserY > y:
            if  600 => UserX, < 600 and 375 => UserY > y:
            if  0 => UserX, < 0 and 450 => UserY > y:
            if  75 => UserX, < 75 and 450 => UserY > y:
            if  150 => UserX, < 150 and 450 => UserY > y:
            if  225 => UserX, < 225 and 450 => UserY > y:
            if  300 => UserX, < 300 and 450 => UserY > y:
            if  375 => UserX, < 375 and 450 => UserY > y:
            if  450 => UserX, < 450 and 450 => UserY > y:
            if  525 => UserX, < 525 and 450 => UserY > y:
            if  600 => UserX, < 600 and 450 => UserY > y:
            if  0 => UserX, < 0 and 525 => UserY > y:
            if  75 => UserX, < 75 and 525 => UserY > y:
            if  150 => UserX, < 150 and 525 => UserY > y:
            if  225 => UserX, < 225 and 525 => UserY > y:
            if  300 => UserX, < 300 and 525 => UserY > y:
            if  375 => UserX, < 375 and 525 => UserY > y:
            if  450 => UserX, < 450 and 525 => UserY > y:
            if  525 => UserX, < 525 and 525 => UserY > y:
            if  600 => UserX, < 600 and 525 => UserY > y:
            if  0 => UserX, < 0 and 600 => UserY > y:
            if  75 => UserX, < 75 and 600 => UserY > y:
            if  150 => UserX, < 150 and 600 => UserY > y:
            if  225 => UserX, < 225 and 600 => UserY > y:
            if  300 => UserX, < 300 and 600 => UserY > y:
            if  375 => UserX, < 375 and 600 => UserY > y:
            if  450 => UserX, < 450 and 600 => UserY > y:
            if  525 => UserX, < 525 and 600 => UserY > y:
            if  600 => UserX, < 600 and 600 => UserY > y:



                
                

    if paused == False:
        #User location
        GameLog.movement()

        #Map
        GameLog.walls()

        #npc location


        #item location and pick up


        #buttons(inventory,menu,etc)
        GameLog.button()
        
     
    GameLog.gamePaused()


    pygame.display.update()
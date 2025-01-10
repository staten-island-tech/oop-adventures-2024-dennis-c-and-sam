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
                UserX -= 1
            if pygame.key.get_pressed()[K_RIGHT]:
                UserX += 1
            if pygame.key.get_pressed()[K_UP]:
                UserY -= 1
            if pygame.key.get_pressed()[K_DOWN]:
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
            pygame.draw.rect(screen, WallColor, pygame.Rect(590,0,10,575),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0,0,600,10),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0,0,10,600),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0,590,600,10),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0,565,600,10),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0,540,600,10),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0,515,600,10),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0,490,600,10),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0,465,600,10),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0,440,600,10),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0,415,600,10),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0,390,600,10),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0,340,600,10),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0,315,600,10),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0,290,600,10),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0, 265,600,10),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0,240,600,10 ),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect( 0,215,600,10 ),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect( 0,190,600,10 ),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0, 165 ,600,10 ),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect( 0,140 ,600,10 ),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0, 115 ,600,10 ),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0, 90,600,10  ),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0, 65,600,10  ),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0, 40,600,10  ),0)
            pygame.draw.rect(screen, WallColor, pygame.Rect(0, 15,600,10  ),0)
            collide = Rect.collidepoint(playerhitbox) 
            if collide:
                UserX = UserX 
                
                

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



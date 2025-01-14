#grid http://www.codingwithruss.com/pygame/sprite-class-and-sprite-groups-explained/
x = 0
y = 0
py = 0
px = 0
tile = 1
posvert = 0
poshor = 0
for i in range (8):
   
    posvert += 1
    for e in range (9):
        
        
        
        print(f'position = [' ,posvert ,']''[' , poshor,  "]")
        poshor += 1
    poshor = 0

#r = 565
#for x in range(25):
    
   # print(f'pygame.draw.rect(screen, WallColor, pygame.Rect(', r,')')
   # r -= 25
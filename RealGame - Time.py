import pygame
import random
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)
yellow = (230,230,0)
brightyellow =(255,255,0)
red = (255,0,0)
darkgrey = (200,200,200)
grey = (230,230,230)
green = (0,255,0)
blue =(0,0,200)
lightblue = (0,0,100)

display_width = 600
display_height = 600

sidespace = display_width/5

workwidth = display_width - 2*sidespace
lane = workwidth/6
gamedisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Car Race')

clock = pygame.time.Clock()

font = pygame.font.SysFont(None,30)

maincar = pygame.image.load('maincar.png')
maincar = pygame.transform.rotate(maincar,90)
maincar = pygame.transform.scale(maincar,(int(lane),int(lane)))
hitcar1 = pygame.image.load('hitcar1.png')
hitcar1 = pygame.transform.rotate(hitcar1,270)
hitcar1 = pygame.transform.scale(hitcar1,(int(lane),int(lane)))
hitcar2 = pygame.image.load('hitcar2.png')
hitcar2 = pygame.transform.rotate(hitcar2,270)
hitcar2 = pygame.transform.scale(hitcar2,(int(lane),int(lane)))
hitcar3 = pygame.image.load('hitcar3.png')
hitcar3 = pygame.transform.rotate(hitcar3,270)
hitcar3 = pygame.transform.scale(hitcar3,(int(lane),int(lane)))
mainwall = pygame.image.load('Mainmenu.jpg')
mainwall = pygame.transform.scale(mainwall,(display_width,display_height))
sub = pygame.image.load('sub.jpg')
sub = pygame.transform.scale(sub,(display_width,display_height))

tree = pygame.image.load('tree.png')
tree = pygame.transform.scale(tree,(int(lane),int(lane)))

def button(msg,size,rectcol,inact,color,x,y,sizex,sizey,action = None):
    font = pygame.font.SysFont(None,size)

    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x < cur[0] < x+sizex and y < cur[1] < y+sizey:
        myrect = pygame.draw.rect(gamedisplay,inact,[x,y,sizex,sizey])
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            elif action == "start":
                gameloop()
            elif action == "startscreen":
                print("initiated")
                startscreen()
            
    else:
        myrect = pygame.draw.rect(gamedisplay,rectcol,[x,y,sizex,sizey])
    msg = font.render(msg,True,color)
    msgrect = msg.get_rect()
    msgrect.centerx = myrect.centerx
    msgrect.centery = myrect.centery
    gamedisplay.blit(msg,msgrect)

    cur = pygame.mouse.get_pos()
        
def pause():
    p = True
        
    while p:
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
            
        gamedisplay.blit(sub,[0,0])

        gamedisplay.blit(font.render("Game Paused..!!",True,grey),[100,100])
        button("Resume",25,darkgrey,grey,black,50,130,100,25,"pause")
        if 100 < cur[0] < 200 and 130 < cur[1] < 155:
            if click[0] ==1:
                p=False
            
        button("Restart",25,darkgrey,grey,black,155,130,100,25,"start")
        button("Mainmenu",25,darkgrey,grey,black,260,130,100,25,"startscreen")   

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    p = False
        

def startscreen():
    intro = True
    
    while intro==True:
        gamedisplay.blit(mainwall,[0,0])
        gamedisplay.blit(font.render("Main Menu",True,red),[100,100])
        
        button("Start",25,yellow,brightyellow,black,100,130,100,25,"start")
        button("Exit",25,yellow,brightyellow,black,100,160,100,25,"quit")   

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    intro = False
    
def trees():
    z = sidespace + workwidth 
    x = sidespace - lane
    
    y = 0

    while y < display_height :
        gamedisplay.blit(tree, [z,y])
        gamedisplay.blit(tree, [x,y])
        y += lane
    
def randomb(blockers):
    blockx = random.randrange(0,6)
    block = []
    block.append(sidespace+blockx*lane)
    block.append(-90)
    block.append(random.randint(1,3))
    blockers.append(block)

def check(carx,cary,x,lane):
    if ( x[0] <= carx <= x[0]+lane and x[1] <= cary <= x[1]+lane):
        return True
    else:
        return False

def gameloop():
    score = 0
    blockers = []
    gameover = False
    gameexit = False
    roadlines = list(range(0,display_height,30))
    carx = sidespace + lane
    cary = display_height - 2*lane

    while not gameexit:
        
        while gameover == True :
            gamedisplay.blit(sub,[0,0])
            
            gamedisplay.blit(font.render("Game Over..!!",True,grey),[100,100])
            button("Restart",25,darkgrey,grey,black,100,130,100,25,"start")
            button("Mainmenu",25,darkgrey,grey,black,210,130,100,25,"startscreen")   
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = False
                    gameexit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        startscreen()
                        gameloop()
                    elif event.key == pygame.K_c:
                        gameloop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = False
                gameexit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if carx -lane >= sidespace and carx <= sidespace+workwidth:
                        carx = carx - lane
                elif event.key == pygame.K_RIGHT:
                    if carx +lane >= sidespace and carx+lane <= sidespace+workwidth-lane:
                        carx = carx + lane
                elif event.key == pygame.K_DOWN:
                    if cary +lane >= 0 and cary+lane < display_height:
                        cary = cary + lane
                elif event.key == pygame.K_UP:
                    if cary -lane >= 0 and cary-lane < display_height:
                        cary = cary - lane
                elif event.key == pygame.K_p:
                        pause()

        gamedisplay.fill((150,150,150))

        for index, item in enumerate(roadlines):
            pygame.draw.line(gamedisplay,black,(sidespace+workwidth/2,item),(sidespace+workwidth/2,item+20),5)

            roadlines[index]+=10
            if roadlines[index]>=display_height:
                if index == len(roadlines)-1:
                    roadlines[index] = roadlines[0]-30
                else:
                    roadlines[index] = roadlines[index+1]-30
            
        pygame.draw.rect(gamedisplay,green,[0,0,sidespace,display_height])
        pygame.draw.rect(gamedisplay,green,[display_width-sidespace,0,sidespace,display_height])    
        gamedisplay.blit(maincar,[carx,cary])
        trees()
        gamedisplay.blit(font.render("Score :",True,black),[0,0])
        gamedisplay.blit(font.render(str(score),True,black),[10,25])
        
        if time.time()%1 < 0.05:
            randomb(blockers)
        
        for x in blockers:
            if x[2] == 1:
                gamedisplay.blit(hitcar1,[x[0],x[1]])
            elif x[2] == 2:
                gamedisplay.blit(hitcar2,[x[0],x[1]])
            else:
                gamedisplay.blit(hitcar3,[x[0],x[1]])

            x[1] = x[1] + 10;

            if check(carx+lane/2,cary+lane/2,x,lane) or check(carx+lane/2,cary,x,lane)or check(carx+lane/2,cary+lane,x,lane):
                gameover = True
                
            if x[1] >= display_height:
                del blockers[0]
                score+=1
                
        clock.tick(40)
        pygame.display.update()

    pygame.quit()
    quit()

startscreen()

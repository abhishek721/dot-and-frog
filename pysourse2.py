import pygame
import random
import math
import time

pygame.init()

screen = pygame.display.set_mode((800,600))
screen1 = pygame.display.set_mode((800,600))
sx=0 #frog x pos
sx_change = 0 # frog change in x pos
sy=100 #frog y pos
sy_change = 0

score_val= 0 # score of the game
#fish right
frog= pygame.image.load('toad.png') #frog image
def frog_img(x,y):
    screen.blit(frog,(x,y))
    
# drawing circle
cx= random.randint(0,790)
cy= random.randint(0,590)
def draw_circ(x,y):
    pygame.draw.circle(screen, (0,255,0), (cx, cy), 7)

#collision function 
def iscollision(p,q,r,s):
    distance = math.sqrt((math.pow((p-r),2)) + (math.pow((q-s),2)))  
    if distance<=20:
        return True
    else :
        return False  



#setting font
#score font
font = pygame.font.Font('freesansbold.ttf', 32)
def show_score():
    score = font.render("score :"+ str(score_val), True , (255,255,255))
    screen.blit(score,(10,10))

#game over font
font_over = pygame.font.Font('freesansbold.ttf', 50)
def show_over():
    game_over = font_over.render("GAME OVER", True, (0,0,0))
    screen1.blit(game_over,(350,300))

#adding background image
background = pygame.image.load('sea3.jpg')

#adding enemy
#submarine
ex= random.randint(400,700)
ey = random.randint(0,150)
ex_change=2
ey_change=.5
submarine = pygame.image.load('submarine.png')
def sub_marine(x,y):
    screen.blit(submarine,(x,y))

#setting bait
hx= random.randint(550,736)
hy = random.randint(450,536)
hx_change= 2
hy_change= .5
hook = pygame.image.load('hook2.png')
def hook_bait(x,y):
    screen.blit(hook,(x,y))

running = True

while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                sx_change = 3
            if event.key == pygame.K_LEFT:
                sx_change=-2
            if event.key == pygame.K_UP:
                sy_change = -.7
            if event.key == pygame.K_DOWN:
                sy_change = .5
        
    screen.blit(background,(0,0))
    #enemy block
    ex -= ex_change
    ey -= ey_change

    if ex<=0:
        ex=random.randint(400,700)
    if ey<=0:
        ey=150
    sub_marine(ex,ey)

    #bait
    hx -= hx_change
    if hx<=0:
        hx = random.randint(550,736)
    hook_bait(hx,hy)
    #collision 
    collision_dot = iscollision(sx,sy,cx,cy)
    if collision_dot:
        score_val +=1
        
        cx= random.randint(0,790)
        cy= random.randint(0,590)        
    sx += sx_change
    # submarine collision
    collision_sub= iscollision(sx,sy,ex,ey)
    if collision_sub:
        sx = random.randint(400,736)
        sy = random.randint(400,575)
        if score_val>0:
            score_val -= 1
    # bait collision
    collison_bait =iscollision(sx,sy,hx,hy)
    if collison_bait:
        show_over()
        time.sleep(5)
        hx=20000
        break

        
        
        
    if sx>=780:
        sx=780
    elif sx<=0:
        sx=0
    
    sy += sy_change
    if sy>=590:
        sy=590
    elif sy<=0:
        sy=0
    
    

    frog_img(sx,sy)
    draw_circ(cx,cy)
    show_score()
    
    

    pygame.display.update()        
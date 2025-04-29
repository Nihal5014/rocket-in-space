import pygame

WIDTH = 600
HEIGHT = 600
TITLE = 'rocket in space'
run = True
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
x = 300
y = 300
bg = pygame.image.load("images\\space backround.png")
img = pygame.image.load("images\\rocket.png")
img = pygame.transform.scale(img,[50,100])
while run == True:
    screen.blit(bg,(0,0))
    screen.blit(img,(x,y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            #click to move
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y = y - 20
            if event.key == pygame.K_s: 
                y = y + 20   
            if event.key == pygame.K_d: 
                x = x + 20
            if event.key== pygame.K_a: 
                x = x - 20  
    key_press = pygame.key.get_pressed()
    if  key_press[pygame.K_UP]:
        y = y - 0.5
    if  key_press[pygame.K_DOWN]:
        y = y + 0.5
    if  key_press[pygame.K_LEFT]:
        x = x - 0.5
    if  key_press[pygame.K_RIGHT]:
        x = x + 0.5
# press and hold to move 

    if y<0:
        y=0
    if x<0:
        x=0
    if x>550:
        x=550
    if y>500:
        y=500
    pygame.display.update()
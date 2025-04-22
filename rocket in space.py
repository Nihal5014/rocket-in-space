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
while run == True:
    screen.blit(bg,(0,0))
    screen.blit(img,(x,y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                y = y - 10




    pygame.display.update()
import pygame
import random
background_colour = (0,0,0)
(width, height) = (800, 600)
a=[(20,5),(15,5),(10,5),(5,5)]

up,down,left,right=(0,-10),(0,10),(-10,0),(10,0)
b=right
def draw():
    for i in a:
        pygame.draw.circle(screen, (255, 0,0), i, 5, 0)
def move(b):
    a.pop()

    x = (a[0][0] + b[0], a[0][1] + b[1])
    if x[0]>800:
        x=(5,x[1])
    if x[0]<0:
        x=(795,x[1])
    if x[1]>600:
        x=(x[0],5)
    if x[1]<0:
        x=(x[0],595)

    a.insert(0, x)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
clock=pygame.time.Clock()


c=(55,55)

running = True
while running:
    screen.fill(background_colour)
    draw()
    move(b)

    if c in a:
        c=(random.randint(0, 79) * 10 + 5,random.randint(0, 59) * 10 + 5)
        a.append(a[len(a)-1])
    o=a
    for i in range(1,len(a)):
        if a[0]==a[i]:
            o = [(20, 5), (15, 5), (10, 5), (5, 5)]
    a=o
    pygame.draw.circle(screen, (255, 0, 0), c, 5, 0)
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and b!=up:
                b=down
            if event.key == pygame.K_UP and b!=down:
                b=up
            if event.key == pygame.K_RIGHT and b!=left:
                b=right
            if event.key == pygame.K_LEFT and b!=right:
                b=left
    pygame.display.flip()


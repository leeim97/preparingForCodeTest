import pygame, sys
from pygame.locals import *

pygame.init()

width = 600
height = 400
screen = pygame.display.set_mode((width, height))

r1 = pygame.Rect(270, 170, 60, 60)
image1 = pygame.image.load('soccerBall.png')
image1 = pygame.transform.scale(image1, (60, 60))

# 초기값은 왼쪽 상단 방향
vel = [-3,-3]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    r1.x += vel[0]
    r1.y += vel[1]

    if r1.left < 0 or r1.right > width:
        vel[0] *= -1
    if r1.top < 0 or r1.bottom > height:
        vel[1] *= -1

    screen.fill((83, 193, 75))
    screen.blit(image1, r1)
    pygame.display.update()
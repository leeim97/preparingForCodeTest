import pygame, sys
from pygame.locals import *

pygame.init() # 초기화

width = 500
height = 500

screen = pygame.display.set_mode((width,height))


r1 = pygame.Rect(150,150,100,100)
image1 = pygame.image.load('dcon.png')
image2 = pygame.transform.scale(image1,(r1.w,r1.h))

# 화면위에서 발행하는 이벤트 반환
# print(pygame.event.get())
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    # 키보드 이벤트 처리
    keyInput = pygame.key.get_pressed()
    if keyInput[K_LEFT] and r1.left >= 0:
        r1.left -= 1
    elif keyInput[K_RIGHT] and r1.right <= width:
        r1.right +=1
    elif keyInput[K_UP] and r1.top >=0:
        r1.top -=1
    elif keyInput[K_DOWN] and r1.bottom <= height:
        r1.bottom +=1


    screen.fill((0,0,0))
    screen.blit(image1,r1)

    pygame.display.update()

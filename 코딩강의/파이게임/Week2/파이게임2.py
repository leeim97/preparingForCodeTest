import pygame, sys
from pygame.locals import *

pygame.init() # 초기화
screen = pygame.display.set_mode((300,300))

# 화면위에서 발행하는 이벤트 반환
# print(pygame.event.get())


red = 255

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYUP:
            if event.key == K_DOWN:
                if red >= 20:
                    red -= 20
                else:
                    red = 255

    screen.fill((red,0,0))
    pygame.display.update()
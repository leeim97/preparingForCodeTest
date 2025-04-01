import pygame, sys
from pygame.locals import *

pygame.init() # 초기화
screen = pygame.display.set_mode((300,300))

# 화면위에서 발행하는 이벤트 반환
# print(pygame.event.get())

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == MOUSEBUTTONUP:
            print(event.pos)

    screen.fill((0,0,0))
    pygame.display.update()
import pygame

pygame.init()
screen = pygame.display.set_mode((300,300))

myColor = (255,0,0)
screen.fill(myColor) # 색상 지정
pygame.display.update() #화면 업데이트

while True:
    print()
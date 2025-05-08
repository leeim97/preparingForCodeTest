import pygame, sys
from pygame.locals import *

def gameInit():
	global gameStart
	gameStart = False
	stick.centerx = width / 2
	ball.centerx = stick.centerx
	ball.bottom = stick.top


pygame.init()

# 글씨 띄우기
font = pygame.font.SysFont(pygame.font.get_default_font(),50)
text = font.render("Press SPACE KEY to Start",True,(255,255,255))

width = 800
height = 500
screen = pygame.display.set_mode((width, height))

stick = pygame.Rect(340, 470, 120, 20)

# 공
ball = pygame.Rect(240, 240, 20 ,20)
vel = [-1, 1]

# 벽돌들
brickList = []
x = 20
y = 10

for i in range(5):
	for j in range(9):
		brick = pygame.Rect(x,y,80,30)
		brickList.append(brick)
		x += 85
	x = 20
	y += 35

# 게임 시작 제어하기
gameStart = False
gameInit()

while True:
	pygame.time.delay(5)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		if event.type == KEYDOWN and event.key == K_SPACE:
			gameStart = True
	if gameStart:
		# 막대기의 움직임(좌우)
		keyInput = pygame.key.get_pressed()
		if keyInput[K_LEFT] and stick.left >= 0:
			stick.left -= 1
		elif keyInput[K_RIGHT] and stick.right <= width:
			stick.right += 1

		# 공 움직임
		ball.x += vel[0]
		ball.y += vel[1]

		if ball.left <0 or ball.right > width:
			vel[0] *= -1
		if ball.top <0 :
			vel[1] *= -1
		if ball.bottom > height:
			gameInit()


	# 공과 막대기의 충돌
	if ball.colliderect(stick):
		vel[1] *= -1

	# 공과 벽돌의 충돌
	for brick in brickList:
		if ball.colliderect(brick):
			brickList.remove(brick)
			vel[1] *=-1

	screen.fill((0, 0, 0))
	for brick in brickList:
		pygame.draw.rect(screen, (0,0,255), brick)

	if not gameStart:
		screen.blit(text, ((width - text.get_width()) / 2, (height - text.get_height()) / 2))

	pygame.draw.rect(screen, (255, 255, 255), stick)
	pygame.draw.rect(screen,(255,0,0),ball)
	pygame.display.update()
import pygame
import time
import math
pygame.init()

screen = pygame.display.set_mode((500,600))
pygame.display.set_caption("Duc Minh")

GRAY = (169,169,169)
AQUA = (0,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

font = pygame.font.SysFont('sans',50)
font1 = pygame.font.SysFont('sans',100)
b1 = font.render('+',True,BLACK)
b2 = font.render('-',True,BLACK)
b3 = font.render('Min',True,BLACK)
b4 = font.render('Sec',True,BLACK)
b5 = font.render('Start',True,BLACK)
b6 = font.render('Reset',True,BLACK)
clock = pygame.time.Clock()
mins = 0
secs = 0
total = 0
total_secs = 0
start = False
running = True
sound1 = pygame.mixer.Sound("music_demnguoc/tick.wav")
sound2 = pygame.mixer.Sound("music_demnguoc/timeout.wav")

while running:
	clock.tick(60)
	screen.fill(GRAY)
	mouse_x, mouse_y = pygame.mouse.get_pos()

	#Ve hinh chu nhat 
	pygame.draw.rect(screen, AQUA, (100,50,50,50))
	pygame.draw.rect(screen, AQUA, (100,130,50,50))
	pygame.draw.rect(screen, AQUA, (350,50,50,50))
	pygame.draw.rect(screen, AQUA, (350,130,50,50))
	pygame.draw.rect(screen, AQUA, (50,200,170,50))
	pygame.draw.rect(screen, AQUA, (280,200,170,50))
	pygame.draw.rect(screen, BLACK, (45,495,410,60))
	pygame.draw.rect(screen, AQUA, (50,500,400,50))

	#Ve min
	screen.blit(b3,(10,45))
	screen.blit(b3,(420,45))
	#Ve sec
	screen.blit(b4,(10,125))
	screen.blit(b4,(420,125))
	#Ve dau cong 
	screen.blit(b1,(110,45))
	screen.blit(b1,(110,125))
	#Ve dau tru
	screen.blit(b2,(365,45))
	screen.blit(b2,(365,125))
	#ve nut start
	screen.blit(b5,(85,200))
	#Ve nut reset 
	screen.blit(b6,(315,200))
	#Vẽ đồng hồ
	pygame.draw.circle(screen,BLACK,(250,380),100)
	pygame.draw.circle(screen,AQUA,(250,380),98)
	pygame.draw.circle(screen,BLACK,(250,380),5)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if (mouse_x > 100) and (mouse_x < 150) and (mouse_y > 50) and (mouse_y < 100):
					total_secs += 60
					total = total_secs
				if (mouse_x > 100) and (mouse_x < 150) and (mouse_y > 130) and (mouse_y < 180):
					total_secs += 1
					total = total_secs
				if (mouse_x > 350) and (mouse_x < 400) and (mouse_y > 50) and (mouse_y < 100):
					total_secs -= 60
					total = total_secs
				if (mouse_x > 350) and (mouse_x < 400) and (mouse_y > 130) and (mouse_y < 180):
					total_secs -= 1
					total = total_secs
				if (mouse_x > 50) and (mouse_x < 220) and (mouse_y > 200) and (mouse_y < 250):
					total = total_secs
					start = True
				if (mouse_x > 280) and (mouse_x < 450) and (mouse_y > 200) and (mouse_y < 250):
					total_secs = 0
	#Ghi lệnh cho nút start
	if start:
		if total_secs > 0:
			pygame.mixer.Sound.play(sound1)
			total_secs-=1
			time.sleep(1)
		else:
			pygame.mixer.Sound.play(sound2)
			start = False
	#Vẽ thời gian hiện tại
	mins = total_secs // 60
	secs = total_secs - (mins*60)
	text_time = font1.render(str(mins) + ':'+ str(secs),True,RED)
	screen.blit(text_time,(180,50))
	#Vẽ kim giây chạy
	x_sec = 250 + 90*math.sin(6*secs*math.pi/180)
	y_sec = 380 - 90*math.cos(6*secs*math.pi/180)
	pygame.draw.line(screen,RED,(250,380),(int(x_sec),int(y_sec)))
	#Vẽ kim phút chạy
	x_min = 250 + 50*math.sin(6*mins*math.pi/180)
	y_min = 380 - 50*math.cos(6*mins*math.pi/180)
	pygame.draw.line(screen,BLACK,(250,380),(int(x_min),int(y_min)))
	#Vẽ hình chữ nhật đỏ để giảm dần theo thời gian
	if total != 0:
		pygame.draw.rect(screen,RED,(50,500,int(400*(total_secs/total)),50))
	pygame.display.flip()

pygame.quit()
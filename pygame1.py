import pygame, sys
from pygame import *

#Khơi tạo các hàm trong thư viện pygame
pygame.init()

#Khơi tạo màn hình hiện thị set_mode là lấy giá trị chiều dài chiều rộng của phần mềm
windowgame = pygame.display.set_mode((800,500))
#set_caption là khởi tạo tên tiêu đề của phần mềm 
pygame.display.set_caption("Game of TheAnh")

#khơi tạo biến trong python
BGWG = (150,150,150)
RED = (255,0,0)
WHITE = (255,255,255)

while True:
	#Vẽ mầu nên cho ứng dụng 
	windowgame.fill(BGWG)

	#vVẽ hình chữ nhật bằng hàm rect  
	pygame.draw.rect(windowgame, RED, (100,50,50,50))
	pygame.draw.rect(windowgame, WHITE, (100,200,50,50))

	#Vẽ hình tròn với hàm cricle có tọa độ và bán kính 
	pygame.draw.circle(windowgame, WHITE, (250,400), 100)

	#Cần dùng hàm flip() ở cuối để thục hiện các hàm vẽ lên trên 
	pygame.display.flip() 	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit() 	
pygame.quit()
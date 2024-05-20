import pygame
from pygame.locals import *
import random

pygame.init()


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#colors
body_inner = (50, 175, 25)
body_outer = (100, 100, 200)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
green = (0, 255, 0)
bg = (255, 200, 150)
food_col = (200, 50 ,50)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

cell_size = 10
direction = 1 
update_snake = 0
food = [0, 0]
new_food = True
new_piece = [0, 0]
score = 0
game_over = False
clicked = False


again_rect = Rect(SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2, 160, 50)


#create snake
snake_pos = [[int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)]]
snake_pos.append([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + cell_size])
snake_pos.append([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + cell_size * 2])
snake_pos.append([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + cell_size * 3])

font = pygame.font.SysFont(None, 40)




def draw_screen():
	screen.fill(bg)
def draw_score():
	score_txt = 'Score: ' + str(score)
	score_img = font.render(score_txt, True, black)
	screen.blit(score_img, (0, 0))

def check_game_over(game_over):

	#if the snake has been eaten itself
	head_count = 0
	for segment in snake_pos:
		if snake_pos[0] == segment and head_count > 0:
			game_over = True
		head_count += 1 


	if snake_pos[0][0] < 0 or snake_pos[0][0] > SCREEN_WIDTH or snake_pos[0][1] < 0 or snake_pos[0][1] > SCREEN_HEIGHT:
		game_over = True

	return game_over

def draw_game_over():
	over_txt = 'Game Over!'
	over_img = font.render(over_txt, True, blue)
	pygame.draw.rect(screen, red, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 60, 160, 50))
	screen.blit(over_img, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 50))

	again_txt = 'PLay Again?'
	again_img = font.render(again_txt, True, blue)
	pygame.draw.rect(screen, red, again_rect)
	screen.blit(again_img, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 + 10))








run = True
while run:

	draw_screen()
	draw_score()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP and direction != 3:
				direction = 1
			if event.key == pygame.K_RIGHT and direction != 4:
				direction = 2
			if event.key == pygame.K_DOWN and direction != 1:
				direction = 3
			if event.key == pygame.K_LEFT and direction != 2:
				direction = 4



	#create food
	if new_food == True:
		new_food = False
		food[0] = cell_size * random.randint(0, (SCREEN_WIDTH / cell_size) - 1)
		food[1] = cell_size * random.randint(0, (SCREEN_WIDTH / cell_size) - 1)


	pygame.draw.rect(screen, food_col,(food[0], food[1], cell_size, cell_size))



	#check if food has been eaten
	if snake_pos[0] == food:
		new_food = True
		#create a new piece at the last point of the snake's tall
		new_piece = list(snake_pos[-1])
		if direction == 1:
			new_piece[1] += cell_size
		if direction == 3:
			new_piece[1] -= cell_size
		if direction == 2:
			new_piece[0] -= cell_size
		if direction == 4:
			new_piece[0] += cell_size

		snake_pos.append(new_piece)

		score += 1



	if game_over == False:
		if update_snake > 99:
			update_snake = 0
			snake_pos = snake_pos[-1:] + snake_pos[:-1]

			if direction == 1:
				snake_pos[0][0] = snake_pos[1][0]
				snake_pos[0][1] = snake_pos[1][1] - cell_size
			if direction == 3:
				snake_pos[0][0] = snake_pos[1][0]
				snake_pos[0][1] = snake_pos[1][1] + cell_size
			if direction == 2:
				snake_pos[0][1] = snake_pos[1][1]
				snake_pos[0][0] = snake_pos[1][0] + cell_size
			if direction == 4:
				snake_pos[0][1] = snake_pos[1][1]
				snake_pos[0][0] = snake_pos[1][0] - cell_size
			game_over = check_game_over(game_over)

	if game_over == True:
		draw_game_over()
		if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
			clicked = True
		if event.type == pygame.MOUSEBUTTONUP and clicked == True:
			clicked = False
			pos = pygame.mouse.get_pos()
			if again_rect.collidepoint(pos):
				direction = 1 
				update_snake = 0
				food = [0, 0]
				new_food = True
				new_piece = [0, 0]
				score = 0
				game_over = False


				#create snake
				snake_pos = [[int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)]]
				snake_pos.append([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + cell_size])
				snake_pos.append([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + cell_size * 2])
				snake_pos.append([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + cell_size * 3])









	#draw snake
	head = 1
	for x in snake_pos:
		if head == 0:
			pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
			pygame.draw.rect(screen, body_inner, (x[0] + 1, x[1] + 1, cell_size - 2, cell_size - 2))
		if head == 1:
			pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
			pygame.draw.rect(screen, red, (x[0] + 1, x[1] + 1, cell_size - 2, cell_size - 2))
			head = 0

	pygame.display.update()

	update_snake += 1

pygame.quit()

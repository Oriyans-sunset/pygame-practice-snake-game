import pygame
import sys
import random
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.randomise()
        
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, 'red',fruit_rect)
    
    def randomise(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x, self.y)        


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10)] 
        self.direction = Vector2(1,0)
        
    def draw_snake(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, 'black', block_rect)
            
    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
    
    def add_block(self):
        body_copy = self.body[:]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]        


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def update(self):
        self.snake.move_snake()
        self.check_fail()
        
    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomise()
            self.snake.add_block()
    
    def check_fail(self):
        if self.snake.body[0].x >= cell_number or self.snake.body[0].x < 0:
            self.game_over()
        if self.snake.body[0].y >= cell_number or self.snake.body[0].y < 0:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

pygame.init()
cell_size = 20
cell_number = 20
screen = pygame.display.set_mode((cell_size*cell_number, cell_size*cell_number))
clock = pygame.time.Clock()

main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT + 1
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == SCREEN_UPDATE:
            main_game.update()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)        
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)  
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(1,0)        
    
    
    screen.fill('white')
    
    main_game.draw_elements()  
    main_game.check_collision()
    
    pygame.display.update()
    clock.tick(60)
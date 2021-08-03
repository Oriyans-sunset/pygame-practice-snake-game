import pygame
import sys
import random
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.randomise()
        
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size, cell_size, cell_size)
        screen.blit(apple_surface, fruit_rect)
    
    def randomise(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x, self.y)        


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10)] 
        self.direction = Vector2(1,0)
        
        self.head_up = pygame.image.load('/Users/priyanshurastogi/Downloads/pygame-practice-snake-game/Snake-assests/Graphics/head_up.png').convert_alpha() 
        self.head_down = pygame.image.load('/Users/priyanshurastogi/Downloads/pygame-practice-snake-game/Snake-assests/Graphics/head_down.png').convert_alpha() 
        self.head_right = pygame.image.load('/Users/priyanshurastogi/Downloads/pygame-practice-snake-game/Snake-assests/Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('/Users/priyanshurastogi/Downloads/pygame-practice-snake-game/Snake-assests/Graphics/head_left.png').convert_alpha()
        
        self.tail_up = pygame.image.load('/Users/priyanshurastogi/Downloads/pygame-practice-snake-game/Snake-assests/Graphics/tail_up.png').convert_alpha()        
        self.tail_down = pygame.image.load('/Users/priyanshurastogi/Downloads/pygame-practice-snake-game/Snake-assests/Graphics/tail_down.png').convert_alpha()        
        self.tail_right = pygame.image.load('/Users/priyanshurastogi/Downloads/pygame-practice-snake-game/Snake-assests/Graphics/tail_right.png').convert_alpha() 
        self.tail_left = pygame.image.load('/Users/priyanshurastogi/Downloads/pygame-practice-snake-game/Snake-assests/Graphics/tail_left.png').convert_alpha()
        
        self.body_vertical = pygame.image.load('/Users/priyanshurastogi/Downloads/pygame-practice-snake-game/Snake-assests/Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('/Users/priyanshurastogi/Downloads/pygame-practice-snake-game/Snake-assests/Graphics/body_horizontal.png').convert_alpha()
        
        self.body_tr = pygame.image.load('/Users/priyanshurastogi/Downloads/pygame-practice-snake-game/Snake-assests/Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('/Users/priyanshurastogi/Downloads/pygame-practice-snake-game/Snake-assests/Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('/Users/priyanshurastogi/Downloads/pygame-practice-snake-game/Snake-assests/Graphics/body_br.png').convert_alpha() 
        self.body_bl = pygame.image.load('/Users/priyanshurastogi/Downloads/pygame-practice-snake-game/Snake-assests/Graphics/body_bl.png').convert_alpha()        
        
    def draw_snake(self):
        
        self.update_head_graphic()
        self.update_tail_graphic()
        
        for index,block in enumerate(self.body):
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body)-1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index+1] - block
                next_block = self.body[index-1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if (previous_block.x == -1 and next_block.y == -1) or (previous_block.y == -1 and next_block.x == -1):
                        screen.blit(self.body_tl, block_rect)
                    elif (previous_block.x == -1 and next_block.y == 1) or (previous_block.y == 1 and next_block.x == -1):
                        screen.blit(self.body_bl, block_rect)
                    elif (previous_block.x == 1 and next_block.y == -1) or (previous_block.y == -1 and next_block.x == 1):
                        screen.blit(self.body_tr, block_rect)
                    elif (previous_block.x == 1 and next_block.y == 1) or (previous_block.y == 1 and next_block.x == 1):
                        screen.blit(self.body_br, block_rect)                    
                
    
    def update_head_graphic(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0):
            self.head = self.head_left
        if head_relation == Vector2(-1,0):
            self.head = self.head_right
        if head_relation == Vector2(0,1):
            self.head = self.head_up
        if head_relation == Vector2(0,-1):
            self.head = self.head_down                  
    
    def update_tail_graphic(self):
        tail_relation = self.body[len(self.body)-2] - self.body[len(self.body)-1]
        if tail_relation == Vector2(1,0):
            self.tail = self.tail_left
        if tail_relation == Vector2(-1,0):
            self.tail = self.tail_right
        if tail_relation == Vector2(0,1):
            self.tail = self.tail_up
        if tail_relation == Vector2(0,-1):
            self.tail = self.tail_down

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
cell_size = 30
cell_number = 20
screen = pygame.display.set_mode((cell_size*cell_number, cell_size*cell_number))
clock = pygame.time.Clock()

apple_surface = pygame.image.load('/Users/priyanshurastogi/Downloads/pygame-practice-snake-game/Snake-assests/Graphics/apple.png').convert_alpha()
apple_surface = pygame.transform.scale(apple_surface, (40, 40))

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
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)        
    
    
    screen.fill('white')
    
    main_game.draw_elements()  
    main_game.check_collision()
    
    pygame.display.update()
    clock.tick(60)
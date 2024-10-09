
import pygame
import random

class SnakeGame:
    def __init__(self):
        pass

    def run(self):
        pass

class SnakeGame:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.body = [(200, 200), (220, 200), (240, 200)]
        self.direction = 'RIGHT'

class Food:
    def __init__(self):
        self.position = self.set_new_position()

    def set_new_position(self):
        return random.randrange(1, 60) * 10, random.randrange(1, 60) * 10

    def run(self):
        snake = Snake()
        food = Food()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((0, 0, 0))
            for pos in snake.body:
                pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(food.position[0], food.position[1], 10, 10))
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def run(self):
        snake = Snake()
        food = Food()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and snake.direction != 'DOWN':
                        snake.direction = 'UP'
                    elif event.key == pygame.K_DOWN and snake.direction != 'UP':
                        snake.direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                        snake.direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                        snake.direction = 'RIGHT'
            self.move_snake(snake)
            self.check_collision(snake, food)
            self.screen.fill((0, 0, 0))
            for pos in snake.body:
                pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(food.position[0], food.position[1], 10, 10))
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def move_snake(self, snake):
        head_x, head_y = snake.body[0]
        if snake.direction == 'UP':
            head_y -= 10
        elif snake.direction == 'DOWN':
            head_y += 10
        elif snake.direction == 'LEFT':
            head_x -= 10
        elif snake.direction == 'RIGHT':
            head_x += 10
        snake.body.insert(0, (head_x, head_y))

    def check_collision(self, snake, food):
        head_x, head_y = snake.body[0]
        if (head_x, head_y) == food.position:
            snake.body.append(snake.body[-1])
            food.position = food.set_new_position()
        elif (head_x < 0 or head_x >= self.screen_width or
              head_y < 0 or head_y >= self.screen_height or
              (head_x, head_y) in snake.body[1:]):
            pygame.quit()
            sys.exit()

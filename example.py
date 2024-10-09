
import random

class SnakeGame:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.snake_body = [(0, 0), (1, 0), (2, 0)]  # initial snake position
        self.food_position = self._generate_food()
        self.score = 0
        self.direction = 'right'

    def _generate_food(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) not in self.snake_body:
                return (x, y)

    def move_snake(self, direction):
        x, y = self.snake_body[0]
        if direction == 'up':
            y -= 1
        elif direction == 'down':
            y += 1
        elif direction == 'left':
            x -= 1
        elif direction == 'right':
            x += 1
        self.snake_body.insert(0, (x, y))
        if self.snake_body[0] == self.food_position:
            self.score += 10
        else:
            self.snake_body.pop()

    def check_collision(self):
        x, y = self.snake_body[0]
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return True
        if self.snake_body[0] in self.snake_body[1:]:
            return True
        return False

    def update_game(self):
        self.move_snake(self.direction)
        if self.check_collision():
            print("Game Over! Final Score:", self.score)
            exit()
        if self.snake_body[0] == self.food_position:
            self.food_position = self._generate_food()

    def play_game(self):
        while True:
            direction = input("Enter direction (up, down, left, right): ")
            self.direction = direction
            self.update_game()
            print("Score:", self.score)


if __name__ == '__main__':
    game = SnakeGame()
    game.play_game()
'''
# Snake-Game
The snake game is a classic arcade game where you control a snake that grows longer as it eats food. The goal of the game is to avoid hitting the walls or the snake's own body.

# How to Play the Snake Game

To play the snake game, simply use the arrow keys to move the snake. The snake will move in the direction of the arrow key that you press.

You can also press the spacebar to pause the game.

'''

# python code for snake game
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
SNAKE_SIZE = 20
SNAKE_SPEED = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Create the game window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake class
class Snake:
    def __init__(self):
        self.body = [(100, 50), (90, 50), (80, 50)]
        self.direction = (1, 0)

    def move(self):
        head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body = [head] + self.body[:-1]

    def change_direction(self, new_direction):
        if (new_direction[0], new_direction[1]) != (-self.direction[0], -self.direction[1]):
            self.direction = new_direction

    def check_collision(self):
        if (
            self.body[0][0] < 0
            or self.body[0][0] >= WIDTH
            or self.body[0][1] < 0
            or self.body[0][1] >= HEIGHT
        ):
            return True
        return False

    def grow(self):
        tail = (self.body[-1][0] - self.direction[0], self.body[-1][1] - self.direction[1])
        self.body.append(tail)

# Food class
class Food:
    def __init__(self):
        self.position = (random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE), random.randrange(0, HEIGHT - SNAKE_SIZE, SNAKE_SIZE))

    def randomize_position(self):
        self.position = (random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE), random.randrange(0, HEIGHT - SNAKE_SIZE, SNAKE_SIZE))

# Game loop
def game_loop():
    snake = Snake()
    food = Food()

    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -SNAKE_SIZE))
                if event.key == pygame.K_DOWN:
                    snake.change_direction((0, SNAKE_SIZE))
                if event.key == pygame.K_LEFT:
                    snake.change_direction((-SNAKE_SIZE, 0))
                if event.key == pygame.K_RIGHT:
                    snake.change_direction((SNAKE_SIZE, 0))

        snake.move()

        if snake.body[0] == food.position:
            snake.grow()
            food.randomize_position()
            score += 1

        if snake.check_collision():
            running = False

        win.fill(BLACK)

        for segment in snake.body:
            pygame.draw.rect(win, GREEN, pygame.Rect(segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

        pygame.draw.rect(win, WHITE, pygame.Rect(food.position[0], food.position[1], SNAKE_SIZE, SNAKE_SIZE))

        pygame.display.update()
        pygame.time.delay(1000 // SNAKE_SPEED)

    pygame.quit()
    quit()

# Start the game loop
game_loop()


# Snake-Game
# The snake game is a classic arcade game where you control a snake that grows longer as it eats food.
# The goal of the game is to avoid hitting the walls or the snake's own body.

# How to Play the Snake Game
# To play the snake game, simply use the arrow keys to move the snake. The snake will move in the direction
# of the arrow key that you press.
# You can also press the spacebar to pause the game.

# Import necessary libraries
import pygame  # This library is used for creating games
import random  # This library is used for generating random numbers

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400  # Width and height of the game window
SNAKE_SIZE = 20  # Size of the snake and food
SNAKE_SPEED = 10  # Speed at which the snake moves

# Colors
BLACK = (0, 0, 0)  # Black color for the background
WHITE = (255, 255, 255)  # White color for drawing the snake and food
GREEN = (0, 255, 0)  # Green color for the snake's body

# Create the game window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")  # Set the title of the game window

# Snake class
# This class defines the properties and behaviors of the snake
class Snake:
    def __init__(self):
        self.body = [(100, 50), (90, 50), (80, 50)]  # Initial body of the snake
        self.direction = (1, 0)  # Initial direction of the snake (right)

    def move(self):
        # Move the snake by updating its body positions
        head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body = [head] + self.body[:-1]

    def change_direction(self, new_direction):
        # Change the direction of the snake (up, down, left, or right)
        if (new_direction[0], new_direction[1]) != (-self.direction[0], -self.direction[1]):
            self.direction = new_direction

    def check_collision(self):
        # Check if the snake collides with the game boundaries
        if (
            self.body[0][0] < 0
            or self.body[0][0] >= WIDTH
            or self.body[0][1] < 0
            or self.body[0][1] >= HEIGHT
        ):
            return True
        return False

    def grow(self):
        # Make the snake grow longer when it eats food
        tail = (self.body[-1][0] - self.direction[0], self.body[-1][1] - self.direction[1])
        self.body.append(tail)

# Food class
# This class represents the food that the snake eats
class Food:
    def __init__(self):
        # Initialize the position of the food with random coordinates
        self.position = (random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE), random.randrange(0, HEIGHT - SNAKE_SIZE, SNAKE_SIZE))

    def randomize_position(self):
        # Randomize the position of the food when the snake eats it
        self.position = (random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE), random.randrange(0, HEIGHT - SNAKE_SIZE, SNAKE_SIZE))

# Game loop
# This is the main part of the game where everything happens
def game_loop():
    snake = Snake()  # Create the snake
    food = Food()  # Create the food

    score = 0  # Initialize the player's score

    running = True  # Variable to control the game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the game when the close button is clicked
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -SNAKE_SIZE))  # Change the direction when the up arrow key is pressed
                if event.key == pygame.K_DOWN:
                    snake.change_direction((0, SNAKE_SIZE))  # Change the direction when the down arrow key is pressed
                if event.key == pygame.K_LEFT:
                    snake.change_direction((-SNAKE_SIZE, 0))  # Change the direction when the left arrow key is pressed
                if event.key == pygame.K_RIGHT:
                    snake.change_direction((SNAKE_SIZE, 0))  # Change the direction when the right arrow key is pressed

        snake.move()  # Move the snake

        if snake.body[0] == food.position:
            snake.grow()  # Make the snake grow when it eats food
            food.randomize_position()  # Randomize the position of the food
            score += 1  # Increase the player's score

        if snake.check_collision():
            running = False  # Exit the game when the snake collides with the boundaries

        win.fill(BLACK)  # Fill the game window with a black background

        # Draw the snake's body segments
        for segment in snake.body:
            pygame.draw.rect(win, GREEN, pygame.Rect(segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

        # Draw the food
        pygame.draw.rect(win, WHITE, pygame.Rect(food.position[0], food.position[1], SNAKE_SIZE, SNAKE_SIZE))

        pygame.display.update()  # Update the game display
        pygame.time.delay(1000 // SNAKE_SPEED)  # Control the game speed

    pygame.quit()  # Quit Pygame
    quit()  # Quit the game

# Start the game loop
game_loop()  # This line starts the game

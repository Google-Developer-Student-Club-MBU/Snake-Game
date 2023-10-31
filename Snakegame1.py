import pygame

class SnakeGame:
    def __init__(self):
        # Initialize the pygame library
        pygame.init()

        # Set the screen size
        self.screen = pygame.display.set_mode((640, 480))

        # Create the snake
        self.snake = [(100, 100), (90, 100), (80, 100)]

        # Set the food position
        self.food = (300, 200)

        # Set the game speed
        self.game_speed = 10

        # Start the game loop
        self.game_loop()

    def game_loop(self):
        while True:

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Check for keyboard input
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.insert(0, (self.snake[0][0], self.snake[0][1] - 10))
                    elif event.key == pygame.K_DOWN:
                        self.snake.insert(0, (self.snake[0][0], self.snake[0][1] + 10))
                    elif event.key == pygame.K_LEFT:
                        self.snake.insert(0, (self.snake[0][0] - 10, self.snake[0][1]))
                    elif event.key == pygame.K_RIGHT:
                        self.snake.insert(0, (self.snake[0][0] + 10, self.snake[0][1]))

            # Check if the snake has collided with itself or the screen
            if self.snake[0][0] < 0 or self.snake[0][0] >= self.screen.get_width() or self.snake[0][1] < 0 or self.snake[0][1] >= self.screen.get_height() or self.snake[0] in self.snake[1:]:
                self.game_over()

            # Check if the snake has eaten the food
            if self.snake[0] == self.food:
                # Move the food to a new location
                self.food = (pygame.randint(0, self.screen.get_width()), pygame.randint(0, self.screen.get_height()))

                # Make the snake longer
                self.snake.append((self.snake[-1][0], self.snake[-1][1]))

            # Update the snake's position
            for i in range(len(self.snake) - 1, 0, -1):
                self.snake[i] = self.snake[i - 1]

            # Draw the snake and the food
            self.screen.fill((0, 0, 0))

            for segment in self.snake:
                pygame.draw.rect(self.screen, (255, 255, 255), (segment[0], segment[1], 10, 10))

            pygame.draw.rect(self.screen, (255, 0, 0), (self.food[0], self.food[1], 10, 10))

            # Update the display
            pygame.display.flip()

            # Clock tick
            pygame.time.Clock().tick(self.game_speed)

    def game_over(self):
        print("Game over!")
        pygame.quit()
        sys.exit()

# Import the pygame library
import pygame

# Create a class called SnakeGame
class SnakeGame:
    def __init__(self):
        # Initialize the pygame library
        pygame.init()

        # Set the screen size to 640x480 pixels
        self.screen = pygame.display.set_mode((640, 480))

        # Create the snake with an initial position
        self.snake = [(100, 100), (90, 100), (80, 100)]

        # Set the initial position of the food
        self.food = (300, 200)

        # Set the game speed (how fast the game runs)
        self.game_speed = 10

        # Start the game loop
        self.game_loop()

    def game_loop(self):
        # This is the main game loop where the game runs
        while True:

            # Handle events such as keyboard input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Quit the game
                    sys.exit()  # Exit the program

                # Check for keyboard input to control the snake's movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        # Move the snake upwards
                        self.snake.insert(0, (self.snake[0][0], self.snake[0][1] - 10))
                    elif event.key == pygame.K_DOWN:
                        # Move the snake downwards
                        self.snake.insert(0, (self.snake[0][0], self.snake[0][1] + 10))
                    elif event.key == pygame.K_LEFT:
                        # Move the snake to the left
                        self.snake.insert(0, (self.snake[0][0] - 10, self.snake[0][1]))
                    elif event.key == pygame.K_RIGHT:
                        # Move the snake to the right
                        self.snake.insert(0, (self.snake[0][0] + 10, self.snake[0][1]))

            # Check if the snake has collided with itself or the screen boundaries
            if (
                self.snake[0][0] < 0
                or self.snake[0][0] >= self.screen.get_width()
                or self.snake[0][1] < 0
                or self.snake[0][1] >= self.screen.get_height()
                or self.snake[0] in self.snake[1:]
            ):
                self.game_over()  # Call the game over function

            # Check if the snake has eaten the food
            if self.snake[0] == self.food:
                # Move the food to a new random location
                self.food = (
                    pygame.randint(0, self.screen.get_width()),
                    pygame.randint(0, self.screen.get_height()),
                )

                # Make the snake longer by adding a new segment to the tail
                self.snake.append((self.snake[-1][0], self.snake[-1][1]))

            # Update the snake's position
            for i in range(len(self.snake) - 1, 0, -1):
                self.snake[i] = self.snake[i - 1]

            # Draw the snake and the food on the screen
            self.screen.fill((0, 0, 0))  # Fill the screen with a black background

            # Draw the snake's body segments
            for segment in self.snake:
                pygame.draw.rect(self.screen, (255, 255, 255), (segment[0], segment[1], 10, 10))

            # Draw the food as a red square
            pygame.draw.rect(self.screen, (255, 0, 0), (self.food[0], self.food[1], 10, 10))

            # Update the display to show the changes
            pygame.display.flip()

            # Control the game speed by limiting the number of frames per second
            pygame.time.Clock().tick(self.game_speed)

    def game_over(self):
        # Function to handle the game over situation
        print("Game over!")  # Print "Game over!" to the console
        pygame.quit()  # Quit the game
        sys.exit()  # Exit the program

# Create an instance of the SnakeGame class to start the game
SnakeGame()

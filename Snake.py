import pygame
import random

# Initialize Pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 400, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake setup
snake = [(100, 100)]
dx, dy = CELL_SIZE, 0  # Start moving to the right

# Food position
food = (200, 200)

# Clock for controlling the speed
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Arrow key control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: dx, dy = -CELL_SIZE, 0
    if keys[pygame.K_RIGHT]: dx, dy = CELL_SIZE, 0
    if keys[pygame.K_UP]: dx, dy = 0, -CELL_SIZE
    if keys[pygame.K_DOWN]: dx, dy = 0, CELL_SIZE

    # Move the snake
    head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, head)

    # Eat food or move normally
    if head == food:
        food = (
            random.randrange(0, WIDTH, CELL_SIZE),
            random.randrange(0, HEIGHT, CELL_SIZE),
        )
    else:
        snake.pop()

    # Check for collision (walls or self)
    if (
        head in snake[1:] or
        head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT
    ):
        running = False

    # Draw snake and food
    for part in snake:
        pygame.draw.rect(screen, GREEN, (*part, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

    pygame.display.update()
    clock.tick(10)  # Frames per second

pygame.quit()

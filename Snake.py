import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Snake Game")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

snake = [(100, 100)]
dx, dy = CELL_SIZE, 0  # Start moving to the right

food = (200, 200)

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: dx, dy = -CELL_SIZE, 0
    if keys[pygame.K_RIGHT]: dx, dy = CELL_SIZE, 0
    if keys[pygame.K_UP]: dx, dy = 0, -CELL_SIZE
    if keys[pygame.K_DOWN]: dx, dy = 0, CELL_SIZE

    
    head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, head)

    if head == food:
        food = (
            random.randrange(0, WIDTH, CELL_SIZE),
            random.randrange(0, HEIGHT, CELL_SIZE),
        )
    else:
        snake.pop()

    if (
        head in snake[1:] or
        head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT
    ):
        running = False
        
    for part in snake:
        pygame.draw.rect(screen, GREEN, (*part, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

    pygame.display.update()
    clock.tick(10)  # Frames per second

pygame.quit()



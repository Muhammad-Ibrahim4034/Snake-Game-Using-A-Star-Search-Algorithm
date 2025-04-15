import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
CELL_SIZE = 32
WIDTH, HEIGHT = 18, 14
SCREEN_WIDTH, SCREEN_HEIGHT = WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (23, 63, 63)
RED = (255, 0, 0)
SNAKE_SPEED = 10

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH+50, SCREEN_HEIGHT+50))

food_image = pygame.image.load("apple.png")

# Snake initialization
snake = [(5, 5), (5, 6)]  # Initial snake body
snake_direction = (1, 0)  # Initial direction (right)
food = (random.randint(1, WIDTH - 2), random.randint(1, HEIGHT - 2))  # Initial food position

# Helper function to generate food
def generate_food():
    x = random.randint(1, WIDTH - 2)
    y = random.randint(1, HEIGHT - 2)
    while (x, y) in snake:
        x = random.randint(1, WIDTH - 2)
        y = random.randint(1, HEIGHT - 2)
    return (x, y)

# Function to render text on the screen
def draw_text(surface, text, size, color, x, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# Game loop
clock = pygame.time.Clock()
game_over = False
score = 0
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # Move snake
    head_x, head_y = snake[0]
    new_head = (head_x + snake_direction[0], head_y + snake_direction[1])

    # Check if snake hits the screen boundary
    if not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
        game_over = True

    # Check for self-collision
    if new_head in snake[1:]:
        game_over = True

    snake.insert(0, new_head)

    # Check collisions with food
    if new_head == food:
        food = generate_food()
        score += 10
    else:
        snake.pop()

    # Clear the screen
    screen.fill(WHITE)

    # Draw background
    screen.blit(background, (-20, -10))

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, BLUE, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw food
    food_x, food_y = food
    screen.blit(food_image, (food_x * CELL_SIZE, food_y * CELL_SIZE))

    # Draw score
    draw_text(screen, "Score: {}".format(score), 24, BLACK, 10, 10)

    pygame.display.flip()
    clock.tick(SNAKE_SPEED)

# Game over screen
font = pygame.font.SysFont(None, 48)
text = font.render("Game Over! Your Score: {}".format(score), True, BLACK)
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
screen.blit(text, text_rect)
pygame.display.flip()

# Wait for a few seconds before quitting
pygame.time.wait(3000)
pygame.quit()
sys.exit()
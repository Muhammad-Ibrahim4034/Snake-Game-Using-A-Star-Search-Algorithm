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
SNAKE_SPEED = 30

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

# A* algorithm for pathfinding
def a_star_algorithm(snake_head, food_pos, snake_body):
    # Initialize the result grid with -1 (unvisited)
    result = [[-1] * WIDTH for _ in range(HEIGHT)]

    # Initialize the queue with the snake's head
    queue = [snake_head]
    result[snake_head[1]][snake_head[0]] = 0

    while queue:
        x, y = queue.pop(0)

        # Check if we reached the food
        if (x, y) == food_pos:
            break

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy

            # Check if the new position is valid and not in the snake's body
            if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT and result[new_y][new_x] == -1 and (new_x, new_y) not in snake_body:
                result[new_y][new_x] = result[y][x] + 1
                queue.append((new_x, new_y))
    else:
        # If the food is not reachable, return None
        return None

    # Reconstruct the path
    path = []
    x, y = food_pos
    while (x, y) != snake_head:
        path.append((x, y))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT and result[new_y][new_x] == result[y][x] - 1:
                x, y = new_x, new_y
                break

    return path

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

    # Get the A* path
    path = a_star_algorithm(snake[0], food, snake[1:])

    # Check if there is no path for the snake
    if not path:
        game_over = True

    # Update snake direction
    if path:
        next_x, next_y = path[-1]
        dx, dy = next_x - snake[0][0], next_y - snake[0][1]

        # Prevent going backward
        if (dx, dy) != (-snake_direction[0], -snake_direction[1]):
            snake_direction = (dx, dy)
        else:
            # If going backward, choose a random direction
            snake_direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])

    # Move snake
    head_x, head_y = snake[0]
    new_head = (head_x + snake_direction[0], head_y + snake_direction[1])

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
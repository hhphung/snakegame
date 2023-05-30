import pygame
import random


pygame.init()

# game window
WIDTH, HEIGHT = 640, 480
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

#colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# snake's initial position and size
snake_size = 20
snake_x = WIDTH // 2
snake_y = HEIGHT // 2
snake_dx = 0
snake_dy = 0

#food's initial position and size
food_size = 20
food_x = random.randint(0, WIDTH - food_size)
food_y = random.randint(0, HEIGHT - food_size)

# track of the snake's body
snake_segments = []

clock = pygame.time.Clock()
game_over = False
score = 0

font = pygame.font.Font(None, 36)

def draw_snake():
    for segment in snake_segments:
        pygame.draw.rect(window, RED, [segment[0], segment[1], snake_size, snake_size])

def move_snake():
    global snake_x, snake_y, score
    snake_x += snake_dx
    snake_y += snake_dy
    snake_segments.append((snake_x, snake_y))
    if len(snake_segments) > score + 1:
        del snake_segments[0]

def draw_food():
    pygame.draw.rect(window, GREEN, [food_x, food_y, food_size, food_size])

def check_collision(x1, y1, x2, y2, size):
    if x1 >= x2 and x1 < x2 + size:
        if y1 >= y2 and y1 < y2 + size:
            return True
    return False

def show_score():
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))

def game_loop():
    global game_over, snake_x, snake_y, snake_dx, snake_dy, food_x, food_y, score

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_dx = -snake_size
                    snake_dy = 0
                elif event.key == pygame.K_RIGHT:
                    snake_dx = snake_size
                    snake_dy = 0
                elif event.key == pygame.K_UP:
                    snake_dy = -snake_size
                    snake_dx = 0
                elif event.key == pygame.K_DOWN:
                    snake_dy = snake_size
                    snake_dx = 0

        move_snake()

        window.fill(BLACK)
        draw_food()
        draw_snake()
        show_score()

        if check_collision(snake_x, snake_y, food_x, food_y, food_size):
            food_x = random.randint(0, WIDTH - food_size)
            food_y = random.randint(0, HEIGHT - food_size)
            score += 1

        # If the snake collides with itself, end the game
        for segment in snake_segments[:-1]:
            if segment == (snake_x, snake_y):
                game_over = True
                break

        pygame.display.update()
        clock.tick(10)

game_loop()
pygame.quit()
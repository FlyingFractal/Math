import pygame
import os

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)  # Black background for fallback

# Create a game window that can resize
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Pong Game")

# Load sound and background image
background_image = pygame.image.load("background_image.jpg")  # Add a background image
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Background Music
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(loops=-1, start=0.0)  # Loops indefinitely

# Initialize Paddles, Ball, and Fonts
paddle_width, paddle_height = 15, 100
ball_radius = 10

# Left Paddle
left_paddle = pygame.Rect(50, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
left_paddle_speed = 0

# Right Paddle
right_paddle = pygame.Rect(WIDTH - 50 - paddle_width, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle_speed = 0

# Ball
ball = pygame.Rect(WIDTH // 2 - ball_radius // 2, HEIGHT // 2 - ball_radius // 2, ball_radius * 2, ball_radius * 2)
ball_dx = 5
ball_dy = 5

# Score
left_score = 0
right_score = 0

# Font
font = pygame.font.SysFont('Arial', 36)

# Game Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    # Get the screen dimensions and resize the background image
    WIDTH, HEIGHT = screen.get_width(), screen.get_height()
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    # Draw the background
    screen.blit(background_image, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= 10
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += 10
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= 10
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += 10

    # Ball movement
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collision with top/bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy = -ball_dy

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_dx = -ball_dx

    # Ball out of bounds (Left or Right)
    if ball.left <= 0:
        right_score += 1
        ball.x = WIDTH // 2 - ball_radius // 2
        ball.y = HEIGHT // 2 - ball_radius // 2
    elif ball.right >= WIDTH:
        left_score += 1
        ball.x = WIDTH // 2 - ball_radius // 2
        ball.y = HEIGHT // 2 - ball_radius // 2

    # Draw paddles and ball
    pygame.draw.rect(screen, (255, 255, 255), left_paddle)
    pygame.draw.rect(screen, (255, 255, 255), right_paddle)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)

    # Display score
    left_score_text = font.render(str(left_score), True, (255, 255, 255))
    right_score_text = font.render(str(right_score), True, (255, 255, 255))
    screen.blit(left_score_text, (WIDTH // 4, 20))
    screen.blit(right_score_text, (3 * WIDTH // 4 - right_score_text.get_width(), 20))

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

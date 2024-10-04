import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("벽돌깨기 게임")

paddle_width = 100
paddle_height = 10
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - 30, paddle_width, paddle_height)

ball_size = 10
ball = pygame.Rect(screen_width // 2 - ball_size // 2, screen_height // 2 - ball_size // 2, ball_size, ball_size)
ball_speed = [3, -3]  

brick_width = (screen_width - 80) // 10  
brick_height = 20
bricks = []
for i in range(10):
    for j in range(5):
        brick = pygame.Rect(i * (brick_width + 8) + 5, j * (brick_height + 10) + 35, brick_width, brick_height)
        bricks.append(brick)

score = 0
lives = 3
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= 6
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.right += 6

    ball.left += ball_speed[0]
    ball.top += ball_speed[1]

    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]

    if ball.colliderect(paddle):
        if ball.bottom <= paddle.top + ball_speed[1]:
            ball_speed[1] = -ball_speed[1]

    if ball.top >= screen_height:
        lives -= 1
        if lives == 0:
            running = False
        else:
            ball.left = screen_width // 2 - ball_size // 2
            ball.top = screen_height // 2 - ball_size // 2
            ball_speed = [3, -3]

    hit_index = ball.collidelist(bricks)
    if hit_index != -1:
        hit_brick = bricks.pop(hit_index)
        ball_speed[1] = -ball_speed[1]
        score += 1

    if not bricks:
        running = False

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    for brick in bricks:
        pygame.draw.rect(screen, BLUE, brick)

    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (20, 10))
    screen.blit(lives_text, (screen_width - 120, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
 
import pygame
import sys
from main.menu import main_menu

def main_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pong")

    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Paddle dimensions and initial positions
    paddle_width = 10
    paddle_height = 60
    paddle_speed = 5

    player_paddle = pygame.Rect(50, 300 - paddle_height // 2, paddle_width, paddle_height)
    opponent_paddle = pygame.Rect(750 - paddle_width, 300 - paddle_height // 2, paddle_width, paddle_height)

    # Ball dimensions and initial position
    ball_radius = 10
    ball_speed_x = 3
    ball_speed_y = 3

    ball = pygame.Rect(400 - ball_radius, 300 - ball_radius, ball_radius * 2, ball_radius * 2)

    # Score
    player_score = 0
    opponent_score = 0

    font = pygame.font.Font(None, 74)

    def draw_paddle(paddle):
        pygame.draw.rect(screen, WHITE, paddle)

    def draw_ball(ball):
        pygame.draw.circle(screen, WHITE, ball.center, ball_radius)

    def draw_scores(player_score, opponent_score):
        player_text = font.render(str(player_score), True, WHITE)
        opponent_text = font.render(str(opponent_score), True, WHITE)
        screen.blit(player_text, (300 - player_text.get_width() // 2, 10))
        screen.blit(opponent_text, (500 + opponent_text.get_width() // 2, 10))

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get keys pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player_paddle.top > 0:
            player_paddle.y -= paddle_speed
        if keys[pygame.K_s] and player_paddle.bottom < screen.get_height():
            player_paddle.y += paddle_speed

        # Move opponent paddle (simple AI with increasing difficulty)
        speed_factor = 1 + (player_score - opponent_score) * 0.1
        if ball.centerx > opponent_paddle.centerx:
            if opponent_paddle.top < ball.centery:
                opponent_paddle.y += paddle_speed * speed_factor
            elif opponent_paddle.bottom > ball.centery:
                opponent_paddle.y -= paddle_speed * speed_factor

        # Ball movement
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Ball collision with top and bottom walls
        if ball.top <= 0 or ball.bottom >= screen.get_height():
            ball_speed_y *= -1

        # Ball collision with paddles
        if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
            ball_speed_x *= -1

        # Ball out of bounds (score)
        if ball.left <= 0:
            opponent_score += 1
            ball.center = (400, 300)
            ball_speed_x *= -1
        elif ball.right >= screen.get_width():
            player_score += 1
            ball.center = (400, 300)
            ball_speed_x *= -1

        # Clear the screen
        screen.fill(BLACK)

        # Draw paddles and ball
        draw_paddle(player_paddle)
        draw_paddle(opponent_paddle)
        draw_ball(ball)

        # Draw scores
        draw_scores(player_score, opponent_score)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate to 60 FPS
        clock.tick(60)

        # Check for ESC key press to return to main menu
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

    # Return to main menu
    choice = main_menu()
    if choice == "start":
        main_game()
    elif choice == "exit":
        print("Exiting...")
        pygame.quit()
        sys.exit(0)

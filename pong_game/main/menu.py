import pygame

def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Main Menu")

    font = pygame.font.Font(None, 36)
    start_text = font.render("Start Game", True, (0, 0, 0))
    exit_text = font.render("Exit Game", True, (0, 0, 0))
    start_text_rect = start_text.get_rect(center=(400, 250))
    exit_text_rect = exit_text.get_rect(center=(400, 350))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_text_rect.collidepoint(mouse_pos):
                    return "start"
                elif exit_text_rect.collidepoint(mouse_pos):
                    return "exit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "exit"

        screen.fill((255, 255, 255))
        screen.blit(start_text, start_text_rect)
        screen.blit(exit_text, exit_text_rect)
        pygame.display.flip()

    pygame.quit()

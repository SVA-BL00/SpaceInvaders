import pygame

def selection_screen(screen, width, height):
    font = pygame.font.Font(None, 74)
    small = pygame.font.Font(None, 50)
    
    options = ["Flash", "Bombman"]
    selected_option = 0
    
    running = True
    while running:
        screen.fill((0, 0, 0))

        title = font.render("Select Your Player", True, (255, 255, 255))
        screen.blit(title, (width // 2 - title.get_width() // 2, 100))

        for i, option in enumerate(options):
            color = (0, 255, 0) if i == selected_option else (255, 255, 255)
            text = small.render(option, True, color)
            screen.blit(text, (width // 2 - text.get_width() // 2, 250 + i * 60))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                if event.key == pygame.K_RETURN:
                    return selected_option
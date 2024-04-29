import pygame
import random


puzzle_Image = []
background = pygame.image.load(puzzle_Image)
rect_Size = width, height = 900, 900

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((900, 900))
    background_rect = background.get_rect()
    running = True

    while running:

        screen.blit(background, background_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_game_loop()
            elif event.type == pygame.QUIT:
                running = False
                break
 
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
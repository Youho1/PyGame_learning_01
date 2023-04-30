import sys
import pygame
from pygame.locals import QUIT

pygame.init()
display_size = (400, 300)
SURFACE = pygame.display.set_mode(display_size)

def main():
    """ main routine """
    sysfont = pygame.font.SysFont(None, 36)
    counter = 0
    while True:
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()
    

        counter += 1
        black = (0, 0, 0)
        #red = (255, 0, 0)
        SURFACE.fill(black)
        font_color = (225, 225, 225)
        count_image = sysfont.render("count is {}".format(counter), True, font_color)
        SURFACE.blit(count_image, (50, 50))
        pygame.display.update()

if __name__ == '__main__':
    main()

# draw_ellipse.py

import sys
import pygame 
from pygame.locals import QUIT, Rect

pygame.init()
monitor_size = (400, 250)
SURFACE = pygame.display.set_mode(monitor_size)
FPSCLOCK = pygame.time.Clock()

def main():
    # main routine
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
        white = (255, 255, 255)
        SURFACE.fill(white)

        # red
        color = (255, 0, 0) #red
        pygame.draw.ellipse(SURFACE, color, (50, 50, 140, 60))
        pygame.draw.ellipse(SURFACE, color, (250, 30, 90, 90))

        # greed
        color = (0, 255, 0) #green
        line_width = 5
        My_Ellipse = (50, 150, 110, 60)
        pygame.draw.ellipse(SURFACE, color, My_Ellipse, line_width)

        center = (250, 130)
        width_height = (90, 90)
        line_width = 20
        pygame.draw.ellipse(SURFACE, color, (center, width_height), line_width)

        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()

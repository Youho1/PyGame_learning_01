# draw_line1 
# line(Surface, color, start_pos, end_pos, width=1) -> Rect

import sys
import pygame 
from pygame.locals import QUIT

pygame.init()
monitor_size = (400, 220)
Surface = pygame.display.set_mode(monitor_size)
FPSClock = pygame.time.Clock()

def main():

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        Surface.fill((255, 255, 255))

        # red horizontal line width=1
        color = (255, 0, 0)
        point_start = (10, 80)
        point_end = (200, 80)
        pygame.draw.line(Surface, color, point_start, point_end)

        # red horizontal line  width=15
        red = (255, 0, 0)
        point_start = (10, 150)
        point_end = (200, 150)
        line_width = 15
        pygame.draw.line(Surface, red, point_start, point_end, line_width)

        # green Vertical line width=1
        green = (0, 255, 0)
        point_start = (250, 30)
        point_end = (250, 200)
        pygame.draw.line(Surface, green, point_start, point_end)

        # blue Vertical line width=10
        point_start = (300, 30)
        point_end = (380, 200)
        line_width = 10
        blue = (0, 0, 255)
        pygame.draw.line(Surface, blue, point_start, point_end, line_width)

        pygame.display.update()
        FPSClock.tick(3)
        

if __name__ == '__main__':
    main()
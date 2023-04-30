# draw_lines0.py

import sys
import pygame
import random
from pygame.locals import QUIT 

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((0, 0, 0))

        pointlist = []
        for _ in range(10):
            xpos = random.randint(0, 400)
            ypos = random.randint(0, 300)
            pointlist.append((xpos, ypos))

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        pygame.draw.lines(SURFACE, (r, g, b), True, pointlist, 5)
        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ == '__main__':
    main()
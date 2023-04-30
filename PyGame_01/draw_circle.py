import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255, 255, 255))

        # red : fill circle
        radius = 20
        center = (50, 20)
        red = (255, 0, 0)
        pygame.draw.circle(SURFACE, red, center, radius)

        # red: 線の太さ10
        center = (150, 50)
        line_width = 10
        pygame.draw.circle(SURFACE, red, center, radius, line_width)

        # green: radius=10
        center = (50, 150)
        radius = 10
        green = (0, 255, 0)
        pygame.draw.circle(SURFACE, green, center, radius)

        # green: radius=20
        center = (150, 150)
        radius = 20
        pygame.draw.circle(SURFACE, green, center, radius)

        # green: radius=30
        center = (250, 150)
        radius = 30
        pygame.draw.circle(SURFACE, green, center, radius)

        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()


# draw_image1.py

import sys 
import pygame 
from pygame.locals import QUIT 

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()

def main():
    image = pygame.image.load("images/image1.png")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255, 255, 255))
        dest = (20, 50)
        SURFACE.blit(image, dest)

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()
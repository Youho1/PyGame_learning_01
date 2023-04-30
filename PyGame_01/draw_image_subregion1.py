import sys 
import pygame 
from pygame.locals import QUIT,Rect 

pygame.init()
SURFACE = pygame.display.set_mode((1200, 800))
FPSCLOCK = pygame.time.Clock()

def main():
    image = pygame.image.load("images/image1.png")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        SURFACE.fill((255, 255, 255))
        SURFACE.blit(image, (0, 0))
        SURFACE.blit(image, (250, 50), Rect(50, 50, 100, 100))

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()

    
import sys 
from random import randint 
import pygame 
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE

pygame.init()
pygame.key.set_repeat(5, 5)
screen = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()

def main():
    # values
    walls = 80
    ship_y = 250
    velocity = 0
    score = 0
    slope = randint(1, 6)
    sysfont = pygame.font.SysFont(None, 36)
    ship_image = pygame.image.load(("images/ship.png"))
    bang_image = pygame.image.load(("images/bang.png"))
    holes = []
    for xpos in range(walls):
        holes.append(Rect(xpos * 10, 100, 10, 400))
    game_over = False

    # game 
    while True:
        is_space_down = False 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    is_space_down = True
        
        # 自機を移動
        if not game_over:
            score += 10
            velocity += -3 if is_space_down else 3
            ship_y += velocity 

            # 洞窟をスクロール
            edge = holes[-1].copy()
            test = edge.move(0, slope)
            if test.top <= 0 or test.buttom >= 600:
                slope = randint(1, 6) * (-1 if slope > 0 else 1)
                edge.inflate_ip(0, -20)

            edge.move_ip(10, slope)
            holes.append(edge)
            
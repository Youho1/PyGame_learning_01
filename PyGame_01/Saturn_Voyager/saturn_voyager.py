import sys
from random import randint 
import pygame 
from pygame.locals import QUIT, KEYDOWN, KEYUP, \
    K_LEFT, K_Right, K_UP, K_DOWN

pygame.init()
screen = pygame.display.set_mode((800, 800))
FPSCLOCK = pygame.time.Clock()

def main():
    game_over = False
    score = 0
    speed = 25
    stars = []
    keymap = []
    ship = [0, 0]
    scope_image = pygame.image.load("scopr.png")
    rock_image = pygame.image.load("rock.png")

    scorefont = pygame.font.SysFont(None, 36)
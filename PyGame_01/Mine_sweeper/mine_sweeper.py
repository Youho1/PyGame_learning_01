# mine_sweeper.py 
import sys
from math import floor 
from random import randint 
import pygame 
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from enum import Enum

WIDTH = 20 
HEIGHT = 15
SIZE = 50
NUM_OF_BOMBS = 20

class StageState(Enum):
    EMPTY = 0
    BOMB = 1
    OPENED = 2
    
OPEN_COUNT = 0
CHECKED = [[0 for _ in range(WIDTH)] for _ in range (HEIGHT)] 

pygame.init()
Screen = pygame.display.set_mode([WIDTH*SIZE, HEIGHT * SIZE])
FPSCLOCK = pygame.time.Clock()

def num_of_bomb(field, x_pos, y_pos):
    # 周囲にある爆弾の数を返す
    count = 0
    for yoffset in range(-1, 2):
        for xoffset in range(-1, 2):
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and \
                field[ypos][xpos] == StageState.BOMB:
                count += 1
    return count

def open_tile (field, x_pos, y_pos):
    global OPEN_COUNT
    # チェック済みならば何もしない
    if CHECKED[y_pos][x_pos]:
        return
    # 今から探索するので、探索済みのflagをtrue
    CHECKED[y_pos][x_pos] = True

    # x-1は左探索　x+1は右探索　y-1は上探索 y+1は下探索
    for yoffset in range(-1, 2):
        for xoffset in range(-1, 2):
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
            # ウィンドウ内（インデックスが0以上かつ WIDTH or HEIGHT未満　開いていない状態なら開く）
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and \
                field[ypos][xpos] == StageState.EMPTY:
                field[ypos][xpos] = StageState.OPENED
                OPEN_COUNT += 1
                count = num_of_bomb(field, xpos, ypos)
                if count == 0 and \
                    not (xpos == x_pos and ypos == y_pos):
                    open_tile(field, xpos, ypos)

def main():
    smallfont = pygame.font.SysFont(None, 36)
    largefont = pygame.font.SysFont(None, 72)
    message_clear = largefont.render("!!CLEARED!!", True, (0, 255, 255))
    message_over = largefont.render("GAME OVER!!", True, (0, 255, 255))
    message_rect = message_clear.get_rect()
    message_rect.center = (WIDTH*SIZE/2, HEIGHT*SIZE/2)
    game_over = False
    
    field = [[StageState.EMPTY for xpos in range(WIDTH)] for ypos in range(HEIGHT)]
    
    # 爆弾を設置
    count = 0
    while count < NUM_OF_BOMBS:
        xpos, ypos = randint(0, WIDTH-1), randint(0, HEIGHT-1)
        if field[ypos][xpos] == StageState.EMPTY:
            field[ypos][xpos] = StageState.BOMB
            count += 1
    
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and \
                event.button == 1:
                xpos, ypos = floor(event.pos[0] / SIZE), \
                    floor(event.pos[1] / SIZE)
                if field[ypos][xpos] == StageState.BOMB:
                    game_over = True
                else:
                    open_tile(field, xpos, ypos)
        
        # 描画
        Screen.fill((0, 0, 0))
        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                tile = field[ypos][xpos]
                rect = (xpos * SIZE, ypos * SIZE, SIZE, SIZE)

                if tile == StageState.EMPTY or tile == StageState.BOMB:
                    pygame.draw.rect(Screen, (192, 192, 192), rect)

                    if game_over and tile == StageState.BOMB:
                        pygame.draw.ellipse(Screen, (225, 225, 0), rect)
                elif tile == StageState.OPENED:
                    count = num_of_bomb(field, xpos, ypos)
                    if count > 0:
                        num_image = smallfont.render("{}".format(count), True, (255, 255, 0))
                        Screen.blit(num_image, (xpos*SIZE+10, ypos*SIZE+10))

        # 線の描画
        for index in range(0, WIDTH*SIZE, SIZE):
            pygame.draw.line(Screen, (96, 96, 96), (index, 0), (index, HEIGHT*SIZE))

        for index in range(0, HEIGHT*SIZE, SIZE):
            pygame.draw.line(Screen, (96, 96, 96), (0, index), (WIDTH*SIZE, index))

        # メッセージの描画
        if OPEN_COUNT == WIDTH*HEIGHT - NUM_OF_BOMBS:
            Screen.blit(message_clear, message_rect.topleft)
        elif game_over:
            Screen.blit(message_over, message_rect.topleft)
        
        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == '__main__':
    main()
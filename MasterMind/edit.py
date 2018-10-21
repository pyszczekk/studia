import pygame, time
from pygame.locals import *
black = [21, 8, 43]
yellow = [66, 161, 244]  # niebieski hir
light = [252, 236, 168]
blue = [0, 26, 59]
white = [242, 242, 242]
gray = [225, 219, 237]
dark_blue = [0, 15, 33]
dark_black = [0, 0, 0]
def text(text, color, size):
    myfont = pygame.font.Font('Black_Ops_One/BlackOpsOne-Regular.ttf', size)
    letter = myfont.render(text, 100, color)
    return letter

def hover(x1, y1, x2, y2, width, height, color, sound, current_screen, gameDisplay):

    if x2 > pygame.mouse.get_pos()[0] > x1 and y2 > pygame.mouse.get_pos()[1] > y1:
        button = pygame.draw.rect(gameDisplay, color, (x1, y1, width, height))

    if sound == 0:
        sound=1


    return 0
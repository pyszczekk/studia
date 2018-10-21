import edit
import pygame
from pygame.locals import *
black = [21, 8, 43]
yellow = [66, 161, 244]  # niebieski hir
light = [252, 236, 168]
blue = [0, 26, 59]
white = [242, 242, 242]
gray = [225, 219, 237]
dark_blue = [0, 15, 33]
dark_black = [0, 0, 0]
def instruction_screen(screen, sound, current_screen, gameDisplay):
    screen.fill(white)
    screen.blit(edit.text("How to play?", yellow, 100), (54, 16))
    screen.blit(edit.text("How to play?", yellow, 100), (46, 24))
    screen.blit(edit.text("How to play?", dark_black, 100), (50, 20))
    inst = pygame.image.load("instructions2.png")
    screen.blit(inst, (0, 0))
    brain = pygame.image.load("brain.png")
    screen.blit(brain, (530, 440))

    # button back to main screen
    pygame.draw.rect(gameDisplay, blue, (50, 600, 200, 50))
    edit.hover(50, 600, 250, 650, 200, 50, dark_black, sound, current_screen, gameDisplay)
    screen.blit(edit.text("I got it", gray, 20), (110, 615))

    if pygame.mouse.get_pressed()[0]:
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        if 50 <= mouseX <= 250 and 600 <= mouseY <= 650:
            current_screen = 0  # main screen



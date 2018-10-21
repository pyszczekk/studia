import pygame, sys, time, random
from pygame.locals import *
import edit
current_screen = 0
black = [21, 8, 43]
yellow = [66, 161, 244]  # niebieski hir
light = [252, 236, 168]
blue = [0, 26, 59]
white = [242, 242, 242]
gray = [225, 219, 237]
dark_blue = [0, 15, 33]
dark_black = [0, 0, 0]
sound=0
def current():
    global current_screen
    return current_screen
def main(screen, gameDisplay):
    global current_screen,sound
# print("main screen")
    screen.fill(white)
    # screen.blit(bg, (-70, -20))
    img1 = pygame.image.load("brain6.png")
    img2 = pygame.image.load("brain3.png")
    screen.blit(img2, (0, 440))
    screen.blit(img1, (560, 370))
    screen.blit(edit.text("Master Mind", yellow, 100), (64, 34))
    screen.blit(edit.text("Master Mind", yellow, 100), (56, 26))
    screen.blit(edit.text("Master Mind", dark_black, 100), (60, 30))
    mouse = pygame.mouse

    # button instrukcje:
    pygame.draw.rect(gameDisplay, blue, (250, 200, 300, 50))
    edit.hover(250, 200, 550, 250, 300, 50, dark_blue,sound, current_screen, gameDisplay)
    screen.blit(edit.text("How to play?", white, 20), (330, 215))

    screen.blit(edit.text("Choose a difficulty", yellow, 36), (223, 297))
    screen.blit(edit.text("Choose a difficulty", yellow, 36), (217, 303))
    screen.blit(edit.text("Choose a difficulty", dark_black, 36), (220, 300))
    # button easy:
    pygame.draw.rect(gameDisplay, black, (250, 350, 300, 50))
    edit.hover(250, 350, 550, 400, 300, 50, dark_black,sound, current_screen, gameDisplay)
    screen.blit(edit.text("Easy", gray, 20), (370, 365))

    # button medium:
    pygame.draw.rect(gameDisplay, black, (250, 420, 300, 50))
    edit.hover(250, 420, 550, 470, 300, 50, dark_black,sound, current_screen, gameDisplay)
    screen.blit(edit.text("Medium", gray, 20), (355, 435))

    # button hard:
    pygame.draw.rect(gameDisplay, black, (250, 490, 300, 50))
    edit.hover(250, 490, 550, 540, 300, 50, dark_black,sound, current_screen, gameDisplay)
    screen.blit(edit.text("Hard", gray, 20), (370, 505))

    # button AI
    pygame.draw.rect(gameDisplay, black, (250, 560, 300, 50))
    edit.hover(250, 560, 550, 610, 300, 50, dark_black,sound, current_screen, gameDisplay)
    screen.blit(edit.text("AI GAME", gray, 20), (355, 575))

    if mouse.get_pressed()[0]:
        mouseX = mouse.get_pos()[0]
        mouseY = mouse.get_pos()[1]
        if 250 <= mouseX <= 550 and 200 <= mouseY <= 250:
            current_screen = 1  # instructions
        elif 250 <= mouseX <= 550 and 350 <= mouseY <= 400:
            current_screen = 2  # easy
        elif 250 <= mouseX <= 550 and 420 <= mouseY <= 470:
            current_screen = 3  # medium
        elif 250 <= mouseX <= 550 and 490 <= mouseY <= 540:
            current_screen = 4  # hard
        elif 250 <= mouseX <= 550 and 560 <= mouseY <= 610:
            current_screen = 5  # hard
import pygame, sys, time, random
from pygame.locals import *
import code_generate, edit, check
black = [21, 8, 43]
yellow = [66, 161, 244]  # niebieski hir
light = [252, 236, 168]
blue = [0, 26, 59]
white = [242, 242, 242]
gray = [225, 219, 237]
dark_blue = [0, 15, 33]
dark_black = [0, 0, 0]
ball = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
        [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
hint = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
c1, c2, c3, c4, c5, c6, level, count, kod = 0, 0, 0, 0, 0, 0, 0, 0, 0
last = []
moving = -1
sound=0
kod = 0
current_screen=2
def blockedColor(number):
    global c1, c2, c3, c4, c5, c6
    if number==1:
        c1=1
    elif number==2:
        c2=1
    elif number==3:
        c3=1
    elif number==4:
        c4=1
    elif number==5:
        c5=1
    elif number==6:
        c6=1
    return 0
def current():
    return current_screen

def easy_game(screen, gameDisplay):
    global  kod, code, moving, sound
    global checking
    global current_screen
    global ball
    global count
    global c1, c2, c3, c4, c5, c6
    global level
    global last
    if kod == 0:
        kod = 1
        code = code_generate.code_generate("easy")
        # print(code)

    screen.fill(white)
    # board
    board = pygame.image.load("board.png")
    screen.blit(board, (0, 0))
    brain = pygame.image.load("brain7-cloud.png")
    screen.blit(brain, (520, 200))
    pos = pygame.mouse.get_pos()
    if level < 11:
        for i in range(level + 1):
            for j in range(4):
                if ball[i][j] != 0:
                    if i < 6:
                        screen.blit(pygame.image.load(str(ball[i][j]) + ".png"), (j * 74 + 85, 559 - i * 45))
                    else:
                        screen.blit(pygame.image.load(str(ball[i][j]) + ".png"), (j * 74 + 85, 559 - i * 45.5))
                else:
                    continue

    # ball = pygame.draw.circle(gameDisplay, yellow, pos, 20)
    # button back to main screen

    if moving != -1 and pygame.mouse.get_pressed()[0]:
        #print(pos)
        if pos[1] < (557 + (level + 1) * 50) and pos[1] > ((557 - (level + 1) * 50)):

            if pos[0] >= 90 and pos[0] <= 115:
                if ball[level][0] == 0:
                    ball[level][0] = moving
                    last.append(0)
                    blockedColor(moving)
                else:
                    moving = -1
                    count -= 1
            elif pos[0] >= 160 and pos[0] <= 185:
                if ball[level][1] == 0:
                    ball[level][1] = moving
                    blockedColor(moving)
                    last.append(1)
                else:
                    moving = -1
                    count -= 1
            elif pos[0] >= 240 and pos[0] <= 260:
                if ball[level][2] == 0:
                    ball[level][2] = moving
                    blockedColor(moving)
                    last.append(2)
                else:
                        moving = -1
                        count -= 1
            elif pos[0] >= 315 and pos[0] <= 335:
                if ball[level][3] == 0:
                    ball[level][3] = moving
                    blockedColor(moving)
                    last.append(3)
                else:
                    moving = -1
                    count -= 1
            else:
                moving = -1
                count -= 1
            moving = -1
        else:
            moving = -1
            count -= 1
    pygame.draw.rect(gameDisplay, blue, (550, 50, 200, 50))
    edit.hover(550, 50, 750, 100, 200, 50, dark_black,sound, current_screen, gameDisplay)
    screen.blit(edit.text("Main Menu", gray, 20), (590, 65))
    if pygame.mouse.get_pressed()[0]:
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]

        if 550 <= mouseX <= 750 and 50 <= mouseY <= 100:
            current_screen = 0  # main screen
    # button new game
    pygame.draw.rect(gameDisplay, blue, (550, 120, 200, 50))
    edit.hover(550, 120, 750, 170, 200, 50, dark_black, sound, current_screen, gameDisplay)
    screen.blit(edit.text("New Game", gray, 20), (595, 135))
    if pygame.mouse.get_pressed()[0]:
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        if 550 <= mouseX <= 750 and 120 <= mouseY <= 170:
            time.sleep(1)
            # print("new game")
            count = 0
            kod = 0
            checking = 0
            last = []
            moving = -1
            while level > 0:
                hint[level] = [0, 0]
                level -= 1

            c1, c2, c3, c4, c5, c6 = 0, 0, 0, 0, 0, 0
            ball = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                    [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    pygame.draw.rect(gameDisplay, blue, (550, 600, 200, 50))
    if count == 4:
        edit.hover(550, 600, 750, 650, 200, 50, dark_black, sound, current_screen, gameDisplay)
    screen.blit(edit.text("Check", gray, 20), (615, 615))
    if pygame.mouse.get_pressed()[0]:
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        if 550 <= mouseX <= 750 and 600 <= mouseY <= 650 and count == 4:
            # print("sprawdzam")
            checking = 1
            level += 1
            count = 0
            last=[]
            moving= -1
            c1 = 0
            c2 = 0
            c3 = 0
            c4 = 0
            c5 = 0
            c6 = 0
    # undo button
    pygame.draw.rect(gameDisplay, blue, (550, 530, 200, 50))
    if count > 0:
        edit.hover(550, 530, 750, 580, 200, 50, dark_black, sound, current_screen, gameDisplay)
    screen.blit(edit.text("Undo", gray, 20), (622, 545))
    if pygame.mouse.get_pressed()[0]:
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        if 550 <= mouseX <= 750 and 530 <= mouseY <= 580 and count > 0:
            # print("cofam")
            count -= 1
            if ball[level][last[len(last)-1]] == 1:
                c1 = 0
            elif ball[level][last[len(last)-1]] == 2:
                c2 = 0
            elif ball[level][last[len(last)-1]] == 3:
                c3 = 0
            elif ball[level][last[len(last)-1]] == 4:
                c4 = 0
            elif ball[level][last[len(last)-1]] == 5:
                c5 = 0
            elif ball[level][last[len(last)-1]] == 6:
                c6 = 0
            if len(last)>0:
                ball[level][last[len(last)-1]] = 0
                last.pop()
            else:
                ball[level][count] = 0

    if pygame.mouse.get_pressed()[0]:
        pressed_color = screen.get_at(pos)

        # print(pressed_color, pos)
        if count < 4:
            if pressed_color == (255, 39, 1, 255) and (pos[1] > 610 and pos[1] < 650) and c1 == 0:
                #print("red")
                moving = 1
                count += 1

            elif pressed_color == (255, 251, 1, 255) and (pos[1] > 610 and pos[1] < 650) and c2 == 0:
                #print("yellow")
                moving = 2
                count += 1

            elif pressed_color == (1, 249, 1, 255) and ( pos[1] > 610 and pos[1] < 650) and c3 == 0:
                #print("green")
                moving = 3
                count += 1
            elif pressed_color == (1, 253, 255, 255) and ( pos[1] > 610 and pos[1] < 650) and c4 == 0:
                #print("blue")
                moving = 4
                count += 1
            elif pressed_color == (149, 56, 255, 255) and (pos[1] > 610 and pos[1] < 650) and c5 == 0:
                #print("purple")
                moving = 5
                count += 1
            elif pressed_color == (255, 48, 147, 255) and ( pos[1] > 610 and pos[1] < 650) and c6 == 0:
                #print("pink")
                moving = 6
                count += 1
    if level < 11:
        for i in range(level + 1):
            for j in range(count):
                if ball[i][j] != 0:
                    if i < 6:
                        screen.blit(pygame.image.load(str(ball[i][j]) + ".png"), (j * 74 + 85, 559 - i * 45))
                    else:
                        screen.blit(pygame.image.load(str(ball[i][j]) + ".png"), (j * 74 + 85, 559 - i * 45.5))
                else:
                    break
                    # print(checking)

    if level < 11:
        hint[level] = check.check(ball[level], code)
        # print(hint)
        for i in range(level):
            if hint[i][0] == 0 and hint[i][1] == 0:
                continue
            else:
                screen.blit(pygame.image.load(str(hint[i][0]) + str(hint[i][1]) + ".png"), (410, 560 - i * 48 + i * 2))
                # print("dodano")
            if hint[i][1] == 4:
                # print("wygrana")
                sound=0
                current_screen = 6  # wygrana
        checking = 0
    if level == 11:
        sound=0
        current_screen = 7

    if moving >= 0:
        pin = screen.blit(pygame.image.load(str(moving) + ".png"), (pos[0] - 18, pos[1] - 18))
        pygame.display.update()
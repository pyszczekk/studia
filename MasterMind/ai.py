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
ai_colors = [0, 0, 0, 0, 0, 0, 0, 0]
ai_code = [0, 0, 0, 0]
ai_rightColor = 0
moving = -1
sound=0
kod = 0
current_screen=5

ai_colors = [0,0,0,0,0,0,0,0]
ai_rightColor=0
ai_code=[0,0,0,0]
red_yellow=1
color_place=[0,[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3]]
def current():
    return current_screen
def sumElem(tab):
    sum=0
    for i in range(len(tab)):
        sum+=tab[i]
    return sum
def ai_codes(tab):
    red = 0
    yellow =0
    green =0
    blue =0
    purple=0
    pink=0
    for i in range(4):
        if tab[i]==1:
            red+=1
        elif tab[i]==2:
            yellow+=1
        elif tab[i]==3:
            green+=1
        elif tab[i]==4:
            blue+=1
        elif tab[i]==5:
            purple+=1
        elif tab[i]==6:
            pink+=1

    if red==0 and yellow ==0:
        if blue == 0 and green == 0:
            if purple>2 and purple!=4:
                x = 0
                for i in range(4):
                    if tab[i] == 5 and x < 2:
                        x += 1
                        tab[i] = 6
                        break

        if blue >= 2 and blue != 4:
            x = 0

            for i in range(4):
                if tab[i] == 4 and x < 2:
                    x += 1
                    tab[i] = random.randrange(5, 7, 1)
        if blue ==2:
            for i in range(4):
                if tab[i]==4:
                    tab[i]=random.randrange(5, 7, 1)
        if blue >= 1 and green >= 1:
            if (tab[2] == 3 or tab[3] == 4) and (tab[2] == 3 or tab[3] == 4):
                tab[0], tab[1], tab[2], tab[3] = tab[2], tab[3], tab[0], tab[1]
        if green==3:
            for i in range(4):
                if tab[i] == 3:
                    tab[i] = random.randrange(5, 7, 1)
                    break
    if pink == 3:
        for i in range(4):
            if tab[i]==6:
                tab[i]=5


    if yellow>=2 and yellow!=4:
        x=0
        for i in range(4):

            if tab[i]==2 and x<2:
                x+=1
                tab[i]= random.randrange(3, 7, 1)

    if yellow >=1 and red>=1:
        if (tab[2]==1 or tab[3]==1) and (tab[2]==2 or tab[3]==2):
            tab[0], tab[1], tab[2], tab[3]= tab[2], tab[3], tab[0], tab[1]

    if tab[0]!=tab[1]!=tab[2]!=tab[3] and ((yellow == 0 or red == 0) or (blue==0 or green==0 and (yellow==0 and red==0))):

        tab.sort()

    return tab

def ai_game(screen, gameDisplay):
    global kod, code, moving, ai_colors, ai_rightColor, red_yellow, ai_code, sound, color_place
    if kod == 0:
        kod = 1
        code = code_generate.code_generate("medium")
        code = ai_codes(code)

    global checking
    global current_screen
    global ball
    global count
    global c1, c2, c3, c4, c5, c6
    global level
    global last
    screen.fill(white)
    # board
    board = pygame.image.load("board.png")
    screen.blit(board, (0, 0))
    brain = pygame.image.load("brain9.png")
    screen.blit(brain, (515, 391))
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

    #buttons:
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
    edit.hover(550, 120, 750, 170, 200, 50, dark_black,sound, current_screen, gameDisplay)
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
            ai_colors=[0,0,0,0,0,0,0]
            ai_rightColor = 0
            ai_colors = [0, 0, 0, 0, 0, 0, 0, 0]
            ai_rightColor = 0
            ai_code = [0, 0, 0, 0]
            red_yellow = 1
            while level > 0:
                hint[level] = [0, 0]
                level -= 1

            ball = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                    [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    #start button
    pygame.draw.rect(gameDisplay, blue, (550, 190, 200, 50))
    edit.hover(550, 190, 750, 240, 200, 50, dark_black,sound, current_screen, gameDisplay)
    if level ==0:
        screen.blit(edit.text("Start Game", gray, 20), (590, 205))
    else:
        screen.blit(edit.text("Try Again", gray, 20), (595, 205))
    if pygame.mouse.get_pressed()[0]:
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]

        if 550 <= mouseX <= 750 and 190 <= mouseY <= 240:
            #print("zaczynam sam sb grac")
            if level == 0:
                ball[level] = [1,1,2,2]
                level+=1
                count=4
                time.sleep(1)
            elif level == 1:
                if hint[level-1][0]==0 and hint[level-1][1]==0:
                    ball[level] = [3, 3, 4, 4]
                    red_yellow=0
                else:
                    if hint[0][0]+hint[0][1]==4:
                        if hint[0][1]==0:
                            ball[level]=[2,2,1,1]
                        else:
                            ball[level]=[1,2,1,2]
                    else:
                        ball[level]=[1,1,1,1]
                    red_yellow=1
                level+=1
                count=4
                time.sleep(1)
            elif level == 2:
                if hint[level - 1][0] == 0 and hint[level - 1][1] == 0 and red_yellow==0:
                    ball[level]=[5, 5, 6, 6]
                    red_yellow=-1
                if red_yellow==1:
                    if hint[0][0] + hint[0][1] == 4:
                        ball[level] = [2, 1, 2,1]

                    elif (hint[0][0]+hint[0][1]==2 and hint[1][0]+hint[1][1]==0) or (hint[0][0]+hint[0][1]>2 and hint[1][0]+hint[1][1]==1):
                        ball[level]=[2,2,2,2]
                    else:
                        ai_colors[1]=hint[1][1]
                        if hint[1][1]>2:
                            ai_colors[2] = hint[0][1] + hint[0][0] - 2
                        else:
                            ai_colors[2]=hint[0][1]+hint[0][0]-hint[1][1]
                        ai_rightColor = sum(ai_colors)

                        if hint[0][0]==0:
                            if ai_colors[1]>1:
                                for i in range(ai_colors[1]):
                                    ai_code[i]=1;
                            if ai_colors[1]==1:
                                ai_code[0]=1
                            if ai_colors[2]!=0:
                                x=ai_colors[2]
                                l = 2
                                while x>0:
                                    if ai_code[l]==0:
                                        ai_code[l]=2
                                        x -= 1
                                    l+=1

                        else:
                            if hint[0][1]==0:
                                if ai_colors[2]>1:
                                    for i in range(ai_colors[2]):
                                        ai_code[i] = 2
                                if ai_colors[2]==1:
                                    ai_code[0]=2
                                if ai_colors[1] != 0:
                                    x = ai_colors[1]
                                    l = 2
                                    while x > 0:
                                        if ai_code[l] == 0:
                                            ai_code[l] = 1
                                            x -= 1
                                        l += 1

                            else:
                                #mieszane
                                if ai_rightColor==2:
                                    if hint[1][1]==0:
                                        ai_code=[2,0,2,0]
                                    elif ai_colors[2]==0:
                                        ai_code=[1,0,1,0]
                                    else:
                                        ai_code=[1,2,0,0]
                                elif ai_rightColor==3:
                                    if hint[1][1]==1:
                                        ai_code=[1,2,2,0]
                                    elif hint[1][1]==2:
                                        ai_code=[1,2,1,0]
                                    else:
                                        if ai_colors[2]==0:
                                            ai_code=[1,0,1,1]

                                elif ai_rightColor==4:
                                    ai_code=[1,2,1,2]

                        for i in range(4):
                            ball[level][i]=ai_code[i]

                        for i in range(4):
                            if ball[level][i]==0:
                                ball[level][i]=3



                elif red_yellow == 0:
                    if hint[level-1][0]+hint[level-1][1]==4:
                        if hint[level-1][1]==0:
                            ball[level]=[4,4,3,3]
                        else:
                            ball[level]=[3,4,3,4]
                    elif hint[1][0]+hint[1][1]==0:
                        red_yellow=-1
                    else:
                        ball[level]=[3,3,3,3]




                level += 1
                count = 4
                time.sleep(1)
            elif level == 3:
                if red_yellow == 1:
                   # print(ball)
                    if ball[2]==[2,2,2,2]:
                        ai_colors[2]=hint[2][1]
                        ai_rightColor=sum(ai_colors)
                    else:
                        if ai_rightColor == hint[2][1]+hint[2][0]:
                            if hint[2][0]==0:
                                for i in range(4):
                                    ball[level][i] = ai_code[i]
                                    if ball[level][i] == 0:
                                        ball[level][i] = 4
                            elif hint[2][1]==0:
                                ai_code[0], ai_code[1],ai_code[2],ai_code[3]=ai_code[1],ai_code[0],ai_code[3],ai_code[2]
                                for i in range(4):
                                    ball[level][i] = ai_code[i]
                                    if ball[level][i] == 0:
                                        ball[level][i] = 4
                            elif hint[2][0]!=0 and hint[2][1]!=0:
                                for i in range(3):
                                    if (ai_code[i]==1 or ai_code[i]==2) and ai_code[i]!=ai_code[i+1]:
                                        ai_code[i], ai_code[i+1]=ai_code[i+1],ai_code[i]
                                        break
                                for i in range(4):
                                    ball[level][i] = ai_code[i]
                                    if ball[level][i] == 0:
                                        ball[level][i] = 4
                        else:
                            x=hint[2][1]+hint[2][0]-ai_rightColor
                            ai_colors[3]=x

                            ai_rightColor+=x
                            while x>0:
                                for i in range(4):
                                    if ai_code[i]==0:
                                        ai_code[i]=3
                                        x-=1
                                        break

                            if hint[2][1]==0:
                                ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3],  ai_code[2]
                            elif hint[2][1]!=0 and hint[2][0]!=0:
                                for i in range(3):
                                    if ai_code[i]==1 or ai_code[i]==2:
                                        ai_code[i], ai_code[i+1]=ai_code[i+1],ai_code[i]
                                        break


                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 4





                elif red_yellow==0:
                    if hint[1][0] + hint[1][1] == 4:
                        ball[level] = [4, 3, 4,3]

                    elif (hint[1][0]+hint[1][1]==2 and hint[2][0]+hint[2][1]==0) or (hint[1][0]+hint[1][1]>2 and hint[2][0]+hint[2][1]==1):
                        ball[level]=[4,4,4,4]
                    else:
                        ai_colors[3]=hint[2][1]
                        if hint[2][1]>2:
                            ai_colors[4] = hint[1][1] + hint[1][0] - 2
                        else:
                            ai_colors[4]=hint[1][1]+hint[1][0]-hint[2][1]
                        ai_rightColor = sum(ai_colors)

                        if hint[1][0]==0:

                            if ai_colors[3]>1:
                                for i in range(ai_colors[3]):
                                    ai_code[i]=3
                            if ai_colors[3]==1:
                                ai_code[0]=3
                            if ai_colors[4]!=0:
                                x=ai_colors[4]
                                l = 2
                                while x>0:
                                    if ai_code[l]==0:
                                        ai_code[l]=4
                                        x -= 1
                                    l+=1

                        else:
                            if hint[1][1]==0:
                                if ai_colors[4]>1:
                                    for i in range(ai_colors[4]):
                                        ai_code[i] = 4
                                if ai_colors[4]==1:
                                    ai_code[0]=4
                                if ai_colors[3] != 0:
                                    x = ai_colors[3]
                                    l = 2
                                    while x > 0:
                                        if ai_code[l] == 0:
                                            ai_code[l] = 3
                                            x -= 1
                                        l += 1

                            else:
                                #mieszane
                                if ai_rightColor==2:
                                    if hint[2][1]==0:
                                        ai_code=[4,0,4,0]
                                    elif ai_colors[4]==0:
                                        ai_code=[3,0,3,0]
                                    else:
                                        ai_code=[3,4,0,0]
                                elif ai_rightColor==3:
                                    if hint[2][1]==1:
                                        ai_code=[3,4,4,0]
                                    elif hint[2][1]==2:
                                        ai_code=[3,4,3,0]
                                    else:
                                        if ai_colors[4]==0:
                                            ai_code=[3,0,3,3]

                                elif ai_rightColor==4:
                                    ai_code=[3,4,3,4]

                        for i in range(4):
                            ball[level][i]=ai_code[i]

                        for i in range(4):
                            if ball[level][i]==0:
                                ball[level][i]=5


                elif red_yellow==-1:
                    if hint[2][0] + hint[2][1] == 4:
                        if hint[2][1]==0:
                            ball[level]=[6,6,5,5]
                        else:
                            ball[level] = [6, 5, 6, 5]
                    else:
                        ball[level]=[5,5,5,5]

                level += 1
                count = 4
                time.sleep(1)
            elif level == 4:

                """czerwony i zolty na swoich pozycjach, zmiana pozycji pozostalych i dodanie kolejnych"""
                if red_yellow==1:
                    if ai_rightColor == hint[3][1] + hint[3][0]:
                        if hint[3][0] == 0:
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 5
                        elif hint[3][1] == 0:
                            ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3], ai_code[2]
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 5
                        elif hint[3][0] != 0 and hint[3][1] != 0:
                            for i in range(4):
                                if ai_code[i]!=1 and ai_code[i]!=2:
                                    for j in range(i+1,4):
                                        if ai_code[j] != 1 and ai_code[j] != 2:
                                            ai_code[i], ai_code[j]=ai_code[j], ai_code[i]
                                            break
                                    break

                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 5
                    else:
                        x = hint[3][1] + hint[3][0] - ai_rightColor
                        ai_colors[4] = x


                        ai_rightColor += x
                        while x > 0:
                            for i in range(4):
                                if ai_code[i] == 0:
                                    ai_code[i] = 4
                                    x -= 1
                                    break

                        if hint[3][1] == 0:
                            ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3], ai_code[2]
                        elif hint[3][1] != 0 and hint[3][0] != 0:
                            for i in range(4):
                                if ai_code[i]!=1 and ai_code[i]!=2:
                                    for j in range(i+1,4):
                                        if ai_code[j] != 1 and ai_code[j] != 2 and ai_code[i]!=ai_code[j]:
                                            ai_code[i], ai_code[j]=ai_code[j], ai_code[i]
                                            break
                                    break

                        for i in range(4):
                            ball[level][i] = ai_code[i]
                            if ball[level][i] == 0:
                                ball[level][i] = 5


                elif red_yellow==0:
                    if ball[3] == [4,4,4,4]:
                        ai_colors[4] = hint[3][1]
                        ai_rightColor = sum(ai_colors)
                    else:
                        if ai_rightColor == hint[3][1] + hint[3][0]:
                            if hint[3][0] == 0:
                                for i in range(4):
                                    ball[level][i] = ai_code[i]
                                    if ball[level][i] == 0:
                                        ball[level][i] = 6
                            elif hint[3][1] == 0:
                                ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3], ai_code[2]
                                for i in range(4):
                                    ball[level][i] = ai_code[i]
                                    if ball[level][i] == 0:
                                        ball[level][i] = 6
                            elif hint[3][0] != 0 and hint[3][1] != 0:
                                for i in range(3):
                                    if (ai_code[i] == 3 or ai_code[i] == 4) and ai_code[i] != ai_code[i + 1]:
                                        ai_code[i], ai_code[i + 1] = ai_code[i + 1], ai_code[i]
                                        break
                                for i in range(4):
                                    ball[level][i] = ai_code[i]
                                    if ball[level][i] == 0:
                                        ball[level][i] = 6
                        else:
                            x = hint[3][1] + hint[3][0] - ai_rightColor
                            ai_colors[5] = x

                            ai_rightColor += x
                            while x > 0:
                                for i in range(4):
                                    if ai_code[i] == 0:
                                        ai_code[i] = 5
                                        x -= 1
                                        break

                            if hint[3][1] == 0:
                                ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3], ai_code[2]
                            elif hint[3][1] != 0 and hint[3][0] != 0:
                                for i in range(3):
                                    if ai_code[i] == 3 or ai_code[i] == 4:
                                        ai_code[i], ai_code[i + 1] = ai_code[i + 1], ai_code[i]
                                        break

                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                elif red_yellow==-1:
                    if hint[2][0] + hint[2][1] == 4:
                        ball[level] = [ 5, 6, 5,6]

                    elif (hint[2][0] + hint[2][1] == 2 and hint[3][0] + hint[3][1] == 0) or (
                                hint[2][0] + hint[2][1] > 2 and hint[3][0] + hint[3][1] == 1):
                        ball[level] = [6, 6, 6, 6]
                level += 1
                count = 4
                time.sleep(1)
            elif level == 5:
                if red_yellow==1:
                    if ai_rightColor == hint[4][1] + hint[4][0]:
                        if hint[4][0] == 0:
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[4][1] == 0:
                            ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3], ai_code[2]
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[4][0] != 0 and hint[4][1] != 0:
                            for i in range(4):
                                if ai_code[i]!=1 and ai_code[i]!=2:
                                    for j in range(i+1,4):
                                        if ai_code[j] != 1 and ai_code[j] != 2:
                                            ai_code[i], ai_code[j]=ai_code[j], ai_code[i]
                                            break
                                    break
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                    else:
                        x = hint[4][1] + hint[4][0] - ai_rightColor
                        ai_colors[5] = x


                        ai_rightColor += x
                        while x > 0:
                            for i in range(4):
                                if ai_code[i] == 0:
                                    ai_code[i] = 5
                                    x -= 1
                                    break

                        if hint[4][1] == 0:
                            ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3], ai_code[2]
                        elif hint[4][1] != 0 and hint[4][0] != 0:
                            for i in range(4):
                                if ai_code[i]!=1 and ai_code[i]!=2:
                                    for j in range(i+1,4):
                                        if ai_code[j] != 1 and ai_code[j] != 2 and ai_code[i]!=ai_code[j]:
                                            ai_code[i], ai_code[j]=ai_code[j], ai_code[i]
                                            break
                                    break

                        for i in range(4):
                            ball[level][i] = ai_code[i]
                            if ball[level][i] == 0:
                                ball[level][i] = 6
                elif red_yellow==0:
                    if ai_rightColor == hint[4][1] + hint[4][0]:
                        if hint[4][0] == 0:
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[4][1] == 0:
                            ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3], ai_code[2]
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[4][0] != 0 and hint[4][1] != 0:
                            for i in range(4):
                                if ai_code[i]!=1 and ai_code[i]!=2:
                                    for j in range(i+1,4):
                                        if ai_code[j] != 4 and ai_code[j] != 3 and ai_code[j]!=ai_code[i]:
                                            ai_code[i], ai_code[j]=ai_code[j], ai_code[i]
                                            break
                                    break


                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                    else:
                        x = hint[4][1] + hint[4][0] - ai_rightColor
                        ai_colors[6] = x


                        ai_rightColor += x
                        while x > 0:
                            for i in range(4):
                                if ai_code[i] == 0:
                                    ai_code[i] = 6
                                    x -= 1
                                    break

                        if hint[4][1] == 0:
                            ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3], ai_code[2]
                        elif hint[4][1] != 0 and hint[4][0] != 0:
                            for i in range(4):
                                if ai_code[i]!=1 and ai_code[i]!=2:
                                    for j in range(i+1,4):
                                        if ai_code[j] != 3 and ai_code[j] != 4 and ai_code[i]!=ai_code[j]:
                                            ai_code[i], ai_code[j]=ai_code[j], ai_code[i]
                                            break
                                    break

                        for i in range(4):
                            ball[level][i] = ai_code[i]
                            if ball[level][i] == 0:
                                ball[level][i] = 6
                elif red_yellow==0:
                    if ai_rightColor == hint[level-1][1] + hint[level-1][0]:
                        if hint[level-1][0] == 0:
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[level-1][1] == 0:
                            ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3], ai_code[2]
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[level-1][0] != 0 and hint[level-1][1] != 0:
                            for i in range(4):
                                if ai_code[i] != 3 and ai_code[i] != 4:
                                    for j in range(i + 1, 4):
                                        if ai_code[j] != 3 and ai_code[j] != 4 and ai_code[i] != ai_code[j]:
                                            ai_code[i], ai_code[j] = ai_code[j], ai_code[i]
                                            break
                                    break

                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                    else:

                        x = hint[level-1][1] + hint[level-1][0] - ai_rightColor
                        ai_colors[6] = x

                        ai_rightColor += x
                        while x > 0:
                            for i in range(4):
                                if ai_code[i] == 0:
                                    ai_code[i] = 6
                                    x -= 1
                                    break

                        if hint[level-1][1] == 0:
                            ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3], ai_code[2]
                        elif hint[level-1][1] != 0 and hint[level-1][0] != 0:
                            for i in range(4):
                                if ai_code[i] != 3 and ai_code[i] != 4:
                                    for j in range(i + 1, 4):
                                        if ai_code[j] != 3 and ai_code[j] != 4 and ai_code[i] != ai_code[j]:
                                            ai_code[i], ai_code[j] = ai_code[j], ai_code[i]
                                            break
                                    break

                        for i in range(4):
                            ball[level][i] = ai_code[i]
                            if ball[level][i] == 0:
                                ball[level][i] = 6
                elif red_yellow==-1:
                    if hint[2][0]+hint[2][1]==4:
                        ball[level] = [6, 5, 5, 6]
                    elif ball[level-1]==[6,6,6,6] and hint[2][1]==3:
                        ball[level]=[5,6,6,6]
                    elif ball[level-1]==[6,6,6,6] and hint[2][0]!=0 and hint[2][1]!=0:
                        ball[level] = [6, 6, 5, 6]

                level += 1
                count = 4
                time.sleep(1)
            elif level == 6:
                if red_yellow==1:
                    if ai_rightColor == hint[5][1] + hint[5][0]:
                        if hint[5][0] == 0:
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[5][1] == 0:
                            ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3], ai_code[2]
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[5][0] != 0 and hint[5][1] != 0:
                            for i in range(4):
                                if ai_code[i]!=1 and ai_code[i]!=2:
                                    for j in range(i+1,4):
                                        if ai_code[j] != 1 and ai_code[j] != 2 and ai_code[i]!=ai_code[j]:
                                            ai_code[i], ai_code[j]=ai_code[j], ai_code[i]
                                            break
                                    break

                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                    else:

                        x = hint[5][1] + hint[5][0] - ai_rightColor
                        ai_colors[6] = x

                        ai_rightColor += x
                        while x > 0:
                            for i in range(4):
                                if ai_code[i] == 0:
                                    ai_code[i] = 6
                                    x -= 1
                                    break

                        if hint[5][1] == 0:
                            ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3], \
                                                                             ai_code[2]
                        elif hint[5][1] != 0 and hint[5][0] != 0:
                            for i in range(4):
                                if ai_code[i] != 1 and ai_code[i] != 2:
                                    for j in range(i + 1, 4):
                                        if ai_code[j] != 1 and ai_code[j] != 2 and ai_code[i] != ai_code[j]:
                                            ai_code[i], ai_code[j] = ai_code[j], ai_code[i]
                                            break
                                    break

                        for i in range(4):
                            ball[level][i] = ai_code[i]
                            if ball[level][i] == 0:
                                ball[level][i] = 6


                elif red_yellow==0:
                    if ai_rightColor == hint[level-1][1] + hint[level-1][0]:
                        if hint[level-1][0] == 0:
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[level-1][1] == 0:
                            ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3], \
                                                                             ai_code[2]
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[level-1][0] != 0 and hint[level-1][1] != 0:
                            for i in range(4):
                                if ai_code[i] != 3 and ai_code[i] != 4:
                                    for j in range(i + 1, 4):
                                        if ai_code[j] != 3 and ai_code[j] != 4 and ai_code[i] != ai_code[j]:
                                            ai_code[i], ai_code[j] = ai_code[j], ai_code[i]
                                            break
                                    break

                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i]==0:
                                    ball[level][i]=6
                elif red_yellow == -1:
                    if hint[2][0]+hint[2][1]==4:
                        ball[level] = [5, 6, 6, 5]
                    elif ball[level-1]==[6,6,6,6] and hint[2][1]==3:
                        ball[level]=[6,5,6,6]
                    elif ball[level-1]==[6,6,6,6] and hint[2][0]!=0 and hint[2][1]!=0:
                        ball[level] = [6, 6,  6,5]


                level += 1
                count = 4
                time.sleep(1)
            elif level ==7:
                if red_yellow == 1:
                    if ai_rightColor == hint[level-1][1] + hint[level-1][0]:
                        if hint[level-1][0] == 0:
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[level-1][1] == 0:
                            ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3], \
                                                                             ai_code[2]
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[level-1][0] != 0 and hint[level-1][1] != 0:
                            for i in range(4):
                                if ai_code[i] != 1 and ai_code[i] != 2:
                                    for j in range(i + 1, 4):
                                        if ai_code[j] != 1 and ai_code[j] != 2 and ai_code[i] != ai_code[j]:
                                            ai_code[i], ai_code[j] = ai_code[j], ai_code[i]
                                            break
                                    break

                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i]==0:
                                    ball[level][i]=6


                elif red_yellow==0:
                    if ai_rightColor == hint[level - 1][1] + hint[level - 1][0]:
                        if hint[level - 1][0] == 0:
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[level - 1][1] == 0:
                            ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3], \
                                                                             ai_code[2]
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[level - 1][0] != 0 and hint[level - 1][1] != 0:
                            for i in range(4):
                                if ai_code[i] != 3 and ai_code[i] != 4:
                                    for j in range(i + 1, 4):
                                        if ai_code[j] != 3 and ai_code[j] != 4 and ai_code[i] != ai_code[j]:
                                            ai_code[i], ai_code[j] = ai_code[j], ai_code[i]
                                            break
                                    break

                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                elif red_yellow==-1:
                    ball[level] = [6, 5, 5, 6]
                level += 1
                count = 4
                time.sleep(1)
            elif level ==8:
                if red_yellow == 1:
                    if ai_rightColor == hint[level - 1][1] + hint[level - 1][0]:
                        if hint[level - 1][0] == 0:
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[level - 1][1] == 0:
                            ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3], \
                                                                             ai_code[2]
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[level - 1][0] != 0 and hint[level - 1][1] != 0:
                            for i in range(4):
                                if ai_code[i] != 1 and ai_code[i] != 2:
                                    for j in range(i+1,4):
                                        if ai_code[j] != 1 and ai_code[j] != 2 and ai_code[i] != ai_code[j]:
                                            ai_code[i], ai_code[j] = ai_code[j], ai_code[i]
                                            break
                                    break

                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                if red_yellow==0:
                    if ai_rightColor == hint[level - 1][1] + hint[level - 1][0]:
                        if hint[level - 1][0] == 0:
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[level - 1][1] == 0:
                            ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3], \
                                                                             ai_code[2]
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[level - 1][0] != 0 and hint[level - 1][1] != 0:
                            for i in range(4):
                                if ai_code[i] != 3 and ai_code[i] != 4:
                                    for j in range(i + 1, 4):
                                        if ai_code[j] != 3 and ai_code[j] != 4 and ai_code[i] != ai_code[j]:
                                            ai_code[i], ai_code[j] = ai_code[j], ai_code[i]
                                            break
                                    break

                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6


                level += 1
                count = 4
                time.sleep(1)

            elif level == 9:
                if red_yellow == 1:
                    if ai_rightColor == hint[level - 1][1] + hint[level - 1][0]:
                        if hint[level - 1][0] == 0:
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[level - 1][1] == 0:
                            ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3], \
                                                                             ai_code[2]
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[level - 1][0] != 0 and hint[level - 1][1] != 0:
                            for i in range(4):
                                if ai_code[i] != 1 and ai_code[i] != 2:
                                    for j in range(i + 1, 4):
                                        if ai_code[j] != 1 and ai_code[j] != 2 and ai_code[i] != ai_code[j]:
                                            ai_code[i], ai_code[j] = ai_code[j], ai_code[i]
                                            break
                                    break

                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                if red_yellow == 0:
                    if ai_rightColor == hint[level - 1][1] + hint[level - 1][0]:
                        if hint[level - 1][0] == 0:
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[level - 1][1] == 0:
                            ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3], \
                                                                             ai_code[2]
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[level - 1][0] != 0 and hint[level - 1][1] != 0:
                            for i in range(4):
                                if ai_code[i] != 3 and ai_code[i] != 4:
                                    for j in range(i + 1, 4):
                                        if ai_code[j] != 3 and ai_code[j] != 4 and ai_code[i] != ai_code[j]:
                                            ai_code[i], ai_code[j] = ai_code[j], ai_code[i]
                                            break
                                    break

                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                level += 1
                count = 4
                time.sleep(1)
            elif level == 10:
                if red_yellow == 1:
                    if ai_rightColor == hint[level - 1][1] + hint[level - 1][0]:
                        if hint[level - 1][0] == 0:
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[level - 1][1] == 0:
                            ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3], \
                                                                             ai_code[2]
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[level - 1][0] != 0 and hint[level - 1][1] != 0:
                            for i in range(4):
                                if ai_code[i] != 1 and ai_code[i] != 2:
                                    for j in range(3,i , -1):
                                        if ai_code[j] != 1 and ai_code[j] != 2 and ai_code[i] != ai_code[j]:
                                            ai_code[i], ai_code[j] = ai_code[j], ai_code[i]
                                            break
                                    break

                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                if red_yellow == 0:
                    if ai_rightColor == hint[level - 1][1] + hint[level - 1][0]:
                        if hint[level - 1][0] == 0:
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[level - 1][1] == 0:
                            ai_code[0], ai_code[1], ai_code[2], ai_code[3] = ai_code[1], ai_code[0], ai_code[3], \
                                                                             ai_code[2]
                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                        elif hint[level - 1][0] != 0 and hint[level - 1][1] != 0:
                            for i in range(4):
                                if ai_code[i] != 3 and ai_code[i] != 4:
                                    for j in range(i + 1, 4):
                                        if ai_code[j] != 3 and ai_code[j] != 4 and ai_code[i] != ai_code[j]:
                                            ai_code[i], ai_code[j] = ai_code[j], ai_code[i]
                                            break
                                    break

                            for i in range(4):
                                ball[level][i] = ai_code[i]
                                if ball[level][i] == 0:
                                    ball[level][i] = 6
                level += 1
                count = 4
                time.sleep(1)


    #algorytm wykluczania mozliwosci
    if level < 11:
        for i in range(level + 1):
            for j in range(4):
                if ball[i][j] != 0:
                    if i < 6:
                        screen.blit(pygame.image.load(str(ball[i][j]) + ".png"), (j * 74 + 85, 559 - i * 45))
                    else:
                        screen.blit(pygame.image.load(str(ball[i][j]) + ".png"), (j * 74 + 85, 559 - i * 45.5))
                else:
                    break
    if level < 11:
        if count == 4:
            hint[level-1] = check.check2(ball[level-1],code)
            #print(hint)
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
    return 0

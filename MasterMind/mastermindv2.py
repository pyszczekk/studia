#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:02:58 2017

@author: pyszczekk
"""
import pygame
from pygame.locals import *
import sys, time, random, easy, medium, hard, ai, main

pygame.init()
pygame.mixer.music.load("letsplayagame.wav")
pygame.mixer.music.play()

rozdzielczosc = (800, 700)
gameDisplay = pygame.display.set_mode(rozdzielczosc, DOUBLEBUF)
screen = pygame.display.get_surface()
pygame.display.set_caption("MasterMind created by pyszczekk")

pygame.display.flip()
clock = pygame.time.Clock()
# zmienne ekranow:
current_screen = 0  # 0-main screen; 1- intructions; 2- easy; 3-medium; 4-hard; 5 - ai; 6-win; 7-lose

bg = pygame.image.load("bg.jpg")
# colors:
black = [21, 8, 43]
yellow = [66, 161, 244]  # niebieski hir
light = [252, 236, 168]
blue = [0, 26, 59]
white = [242, 242, 242]
gray = [225, 219, 237]
dark_blue = [0, 15, 33]
dark_black = [0, 0, 0]
# cursor:
cursor = 0
default_cursor = pygame.cursors.ball
hover_cursor = pygame.cursors.broken_x
pygame.mouse.set_cursor(*default_cursor)

sound = 0

def text(text, color, size):
    myfont = pygame.font.Font('Black_Ops_One/BlackOpsOne-Regular.ttf', size)
    letter = myfont.render(text, 100, color)
    return letter

def hover(x1, y1, x2, y2, width, height, color):
    global current_screen, sound
    if x2 > pygame.mouse.get_pos()[0] > x1 and y2 > pygame.mouse.get_pos()[1] > y1:
        button = pygame.draw.rect(gameDisplay, color, (x1, y1, width, height))

    if sound == 0:
        sound=1
    if current_screen == 1 and sound == 1:
        pygame.mixer.music.load("umm-2.wav")
        pygame.mixer.music.play()

        sound=2
    if current_screen == 2 and sound ==1:
        pygame.mixer.music.load("hello.wav")
        pygame.mixer.music.play()

        sound = 2
    if current_screen == 3 and sound == 1:
        pygame.mixer.music.load("good.wav")
        pygame.mixer.music.play()

        sound = 2
    if current_screen == 4 and sound == 1:
        pygame.mixer.music.load("hello3.wav")
        pygame.mixer.music.play()

        sound = 2
    if current_screen == 5 and sound == 1:
        pygame.mixer.music.load("helloai.wav")
        pygame.mixer.music.play()

        sound = 2

    return 0

def instruction_screen():
    global sound,current_screen
    screen.fill(white)
    screen.blit(text("How to play?", yellow, 100), (54, 16))
    screen.blit(text("How to play?", yellow, 100), (46, 24))
    screen.blit(text("How to play?", dark_black, 100), (50, 20))
    inst = pygame.image.load("instructions2.png")
    screen.blit(inst, (0, 0))
    brain = pygame.image.load("brain.png")
    screen.blit(brain, (530, 440))

    # button back to main screen
    pygame.draw.rect(gameDisplay, blue, (50, 600, 200, 50))
    hover(50, 600, 250, 650, 200, 50, dark_black)
    screen.blit(text("I got it", gray, 20), (110, 615))

    if pygame.mouse.get_pressed()[0]:
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        global current_screen
        if 50 <= mouseX <= 250 and 600 <= mouseY <= 650:
            current_screen = 0  # main screen

def winScreen():
    global current_screen,sound
    screen.fill(light)
    win = pygame.image.load("win.png")
    screen.blit(win, (0, -50))
    screen.blit(text("OMG!", black, 96), (273, 35))
    start = time.time()
    screen.blit(text("click on the screen to close :) ", black, 15), (270, 670))
    pygame.mixer.music.load("win2.wav")
    if sound ==0:
        sound = 1
    pygame.display.update()
    if sound==1:
        pygame.mixer.music.play()
        time.sleep(1.5)
        sound=2


    if pygame.mouse.get_pressed()[0]:
        current_screen = 0
    return 0

def loseScreen():
    global current_screen, sound
    screen.fill(light)
    win = pygame.image.load("lose.png")
    screen.blit(win, (0, -50))
    screen.blit(text("DAMN!", black, 96), (237, 35))
    start = time.time()
    screen.blit(text("click on the screen to close :) ", black, 15), (270, 670))
    pygame.mixer.music.load("loser.wav")
    if sound == 0:
        sound = 1
    pygame.display.update()
    if sound == 1:
        pygame.mixer.music.play()
        time.sleep(1.5)
        sound = 2
    if pygame.mouse.get_pressed()[0]:
        current_screen = 0
    return 0

running = True
while running:
    pygame.mouse.set_cursor(*default_cursor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if current_screen == 0:
        current_screen = main.current()
        main.main(screen, gameDisplay)
        easy.current_screen=2
        medium.current_screen=3
        hard.current_screen=4
        ai.current_screen=5
        easy.ball = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        easy.hint = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        easy.c1, easy.c2, easy.c3, easy.c4, easy.c5, easy.c6, easy.level, easy.count, easy.kod = 0, 0, 0, 0, 0, 0, 0, 0, 0
        easy.last = []
        easy.moving = -1
        easy.sound = 0
        medium.ball = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        medium.hint = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        medium.level, medium.count, medium.kod = 0, 0, 0
        medium.last = []
        medium.moving = -1
        medium.sound = 0
        hard.ball = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        hard.hint = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        hard.level, hard.count, hard.kod = 0, 0, 0
        hard.last = []
        hard.moving = -1
        hard.sound = 0
        ai.ball = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        ai.hint = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        ai.level, ai.count, ai.kod = 0, 0, 0
        ai.last = []
        ai.ai_colors = [0, 0, 0, 0, 0, 0, 0, 0]
        ai.ai_code = [0, 0, 0, 0]
        ai.ai_rightColor = 0
        ai.moving = -1
        ai.sound = 0
        sound=0

    elif current_screen == 1:
        instruction_screen()
        main.current_screen=0
    elif current_screen == 2:
       easy.easy_game(screen, gameDisplay)
       current_screen=easy.current()
       main.current_screen = 0
    elif current_screen == 3:
        medium.medium_game(screen, gameDisplay)
        current_screen = medium.current()
        main.current_screen = 0
    elif current_screen == 4:
        hard.hard_game(screen, gameDisplay)
        current_screen = hard.current()
        main.current_screen = 0
    elif current_screen == 5:
        ai.ai_game(screen, gameDisplay)
        current_screen = ai.current()
        main.current_screen = 0
    elif current_screen == 6:
        winScreen()
        main.current_screen = 0
    elif current_screen == 7:
        loseScreen()

    pygame.display.update()
    clock.tick(10)
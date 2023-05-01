import os
import sys

import pygame

sys.path.insert(0, os.getcwd())

import utils
from utils.pygame_ import emerge_from_color, fade_out, fade_into_color
import screen_size

pygame.display.init()

window = pygame.display.set_mode((screen_size.width, screen_size.height))

utils.init(False)

import game as game_
import menu as menu_
from splash import SplashScreen

SPLASH_SCREEN = -1
MENU = 0
OPTIONS = 1
GAME = 2

game_state = SPLASH_SCREEN

game = game_.Game()  # pyright: ignore
menu = menu_.Menu()
splash = SplashScreen()

while True:
    match game_state:
        case -1:
            if not splash.update():
                game_state = 0

            splash.draw()

        case 0:
            # menu
            menu.open()
            menu.update()
            menu.draw()
        case 1:
            # options
            pass
        case 2:
            # game
            game.update()
            game.draw()

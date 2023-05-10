import os
import sys

sys.path.insert(0, os.getcwd())

import menu as menu_
import game as game_

import screen_size
import pygame

pygame.display.init()
window = pygame.display.set_mode((screen_size.width, screen_size.height))

# NOTE imports must be like this due to pygame init requirements

from zoom import ZoomScreen
from splash import SplashScreen

SPLASH_SCREEN = -1
MENU = 0
ZOOM_INTO_GAME = 1
GAME = 2

game_state = SPLASH_SCREEN

# load sprites
menu_.Menu.load_menu_sprites_from_path(path="res/menu")
menu_.Menu.set_window()


def main():
    global game_state

    print("entry -> splash")

    while True:
        match game_state:
            case -1:
                if not SplashScreen.update():
                    print("splash -> menu")
                    game_state = 0
                SplashScreen.draw()
            case 0:
                if not menu_.Menu.update():
                    print("menu -> zoom")
                    game_state = 1
                menu_.Menu.draw_to_window()
            case 1:
                if not ZoomScreen.update():
                    print("zoom -> game")
                    game_state = 2
                ZoomScreen.draw()
            case 2:
                Game.update()
                Game.draw()


if __name__ == "__main__":
    main()

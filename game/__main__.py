import menu as menu_
import game as game_
import os
import sys

import screen_size
import pygame


sys.path.insert(0, os.getcwd())


pygame.display.init()
window = pygame.display.set_mode((screen_size.width, screen_size.height))

# imports must be like this due to pygame init requirements

from zoom import ZoomScreen
from splash import SplashScreen

SPLASH_SCREEN = -1
MENU = 0
ZOOM_INTO_GAME = 1
GAME = 2

game_state = SPLASH_SCREEN

game = game_.Game()
menu = menu_.Menu()
splash = SplashScreen()
zoom = ZoomScreen()

# load sprites
menu.load_menu_sprites_from_path(path="res/menu")
menu.set_window()

def main():
    global game_state

    print("entry -> splash")

    while True:
        match game_state:
            case -1:
                if not splash.update():
                    print("splash -> menu")
                    game_state = 0
                splash.draw()
            case 0:
                if not menu.update():
                    print("menu -> zoom")
                    game_state = 1
                menu.draw_to_window()
            case 1:
                if not zoom.update():
                    print("zoom -> game")
                    game_state = 2
                zoom.draw()
            case 2:
                game.update()
                game.draw()


if __name__ == "__main__":
    main()

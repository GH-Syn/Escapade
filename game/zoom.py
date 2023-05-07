"""
This module houses the ZoomScreen class which zooms into the main menu

module: game.zoom
   ⚪ draw
     ↪️ Draw  screen surface to primary display surface
   ⚪ update
     ↪️ Updates user events such as quit and button presses

license: MIT
author: Joshua Rose
date: 07/05/2023
"""

import json
import sys

import pygame


class ZoomScreen:
    """
    Zooms into main menu when play button is pressed.
    """

    datafile = open("data/theme.json", "r")
    transition = json.load(datafile)["SplashScreen"]["default"]
    datafile.close()

    window = pygame.display.get_surface()

    surface = scaled_surface = pygame.Surface(window.get_size(), pygame.SRCALPHA)

    # Define the colors and fonts for the splash screen
    background_color = transition["bg_color"]
    text_color = transition["text_color"]

    font_size = transition["font_size"]

    # Get the center of the screen
    center_x = window.get_width() // 2
    center_y = window.get_height() // 2

    winwidth = int(window.get_width())
    winheight = int(window.get_height())

    done = False

    ZOOM_POINT = (740, 540)

    # Define the fade in/out time in seconds
    fade_time = transition["fade_time"] / 1000

    final_scale_factor = 1500

    # Define zoom animation
    timer = pygame.time.Clock()
    scale = 1
    alpha = 255

    image = pygame.image.load("res/menu/open_menu_1.png").convert_alpha()
    surface.blit(image, (0, 0))

    @classmethod
    def update(cls):
        """
        Updates user events such as button presses and quit events
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        if cls.scale < cls.final_scale_factor:
            if cls.scale > 4:
                if cls.alpha > 0:
                    cls.alpha -= 25
                    cls.scaled_surface.set_alpha(cls.alpha, pygame.SRCALPHA)
                else:
                    cls.done = True
                    return False
            if cls.scale < 7:
                cls.scaled_surface = pygame.transform.scale(
                    cls.scaled_surface,
                    (cls.winwidth * cls.scale, cls.winheight * cls.scale),
                )
                cls.scaled_surface_rect = cls.scaled_surface.get_rect(
                    center=(cls.center_x, cls.center_y)
                )
            else:
                cls.done = True
                return False
            cls.scale += 0.1

        cls.timer.tick(60)
        return True

    @classmethod
    def draw(cls):
        """Draw to screen as declared in class var"""

        cls.scaled_surface.set_alpha(cls.alpha)
        cls.window.blit(cls.scaled_surface, cls.scaled_surface_rect)

        pygame.display.update()

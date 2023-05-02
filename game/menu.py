import re
import os
import pygame
from pygame.constants import SRCALPHA

from utils.pygame_ import fade_into_color


class Menu:
    window = pygame.display.get_surface()
    font = os.path.join("res/fonts/Silkscreen", "silkscr.ttf")

    DEFAULT_MENU_BACKGROUND_COLOR = (25, 25, 25)

    clock = pygame.time.Clock()
    dt = 0
    fps = 24

    images_ = [i for i in os.listdir("res/menu")]
    images = sorted(images_, key=lambda x: int(x.split("_")[-1].split(".")[0]))
    scroll = [
        pygame.image.load(os.path.join("res", "menu", i)).convert_alpha()
        for i in images
    ]

    opening = True
    opening_frame = 0
    opening_tick = 0
    image = scroll[0]

    mask = pygame.Surface(window.get_size(), SRCALPHA)

    @classmethod
    def open(cls):
        """Open the scroll thing for the main menu"""
        if not cls.opening:
            return
        if cls.opening_frame < len(cls.scroll):
            cls.opening_tick += 1
            if cls.opening_tick >= 3:
                cls.image = cls.scroll[cls.opening_frame]
                cls.opening_tick = 0
                cls.opening_frame += 1
        # blit mask
        else:
            cls.opening = False
            return

    @classmethod
    def draw(cls):
        # cls.window.fill(cls.DEFAULT_MENU_BACKGROUND_COLOR)

        cls.open()
        cls.window.blit(cls.image, (0, 0))

    @classmethod
    def update(cls):
        cls.dt = cls.clock.tick(cls.fps) / 1000.0
        pygame.display.update()

import os
from tqdm import tqdm
import pygame
from pygame.constants import SRCALPHA

# TODO: remove un-used imports
import re  # pyright: ignore
from utils.pygame_ import fade_into_color  # pyright: ignore


class Menu:
    window = pygame.display.get_surface()
    pygame.font.init()
    font = os.path.join("res/fonts/Silkscreen", "silkscr.ttf")

    DEFAULT_MENU_BACKGROUND_COLOR = (25, 25, 25)

    clock = pygame.time.Clock()
    dt = 0
    fps = 24

    menu_sprites: list[pygame.SurfaceType] = []
    images = []

    with tqdm(
        total=len(os.listdir("res/menu")), dynamic_ncols=True, desc="Loading menu files"
    ) as pbar:
        for j in os.listdir("res/menu"):
            try:
                if j.endswith(".png"):
                    image = pygame.image.load(
                        os.path.join("res", "menu", j)
                    ).convert_alpha()
                    menu_sprites.append(image)
            finally:
                pbar.update(1)

    opening = True
    opening_frame = 0
    opening_tick = 0
    image: pygame.Surface = menu_sprites[0]

    mask = pygame.Surface(window.get_size(), SRCALPHA)

    @classmethod
    def open(cls):
        """Play main menu animation"""
        if not cls.opening:
            return
        if cls.opening_frame < len(cls.menu_sprites):
            cls.opening_tick += 1
            if cls.opening_tick >= 3:
                cls.image = cls.menu_sprites[cls.opening_frame]
                cls.opening_tick = 0
                cls.opening_frame += 1
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

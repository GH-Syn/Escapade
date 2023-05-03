import os
from tqdm import tqdm
import pygame
from pygame.constants import SRCALPHA

import re

class Menu:
    window = pygame.display.get_surface()
    pygame.font.init()
    font = os.path.join("res/fonts/Silkscreen", "silkscr.ttf")

    DEFAULT_MENU_BACKGROUND_COLOR = (25, 25, 25)

    clock = pygame.time.Clock()
    dt = 0
    fps = 24

    menu_sprites: list[pygame.SurfaceType] = []
    paths = []
    images = []

    with tqdm(
        total=len(os.listdir("res/menu")), dynamic_ncols=True, desc="Looking for files"
    ) as pbar:
        for j in os.listdir("res/menu"):
            try:
                if j.endswith(".png"):
                    image = pygame.image.load(
                        os.path.join("res", "menu", j)
                    ).convert_alpha()
                    paths.append(os.path.join("res", "menu", j))
            finally:
                pbar.update(1)

    paths: list[str] = paths
    with tqdm(
        total=len(paths),
        dynamic_ncols=True,
        desc="Cooking up some animations",
    ) as pbar:
        for path in paths:
            if not path in ["old", "background", "menu.png", "sign", "sign_scaled.png"]:
                images.append(pygame.image.load(path).convert_alpha())
                pbar.update(1)

    path = "res/menu"
    pattern = re.compile(r"^open_menu_[1-6]\.png$")
    menu_sprites.clear()
    menu_sprites = []

    for filename in sorted(os.listdir(path)):
        if pattern.match(filename):
            menu_sprites.append(
                pygame.image.load(os.path.join(path, filename)).convert_alpha()
            )

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
            if cls.opening_tick >= 6:
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

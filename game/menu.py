import os
import re
import sys

import pygame
from pygame.constants import SRCALPHA
from tqdm import tqdm


class Menu:
    """Handles menu events and animations"""

    pygame.font.init()
    pygame.display.init()

    window = pygame.display.get_surface() if pygame.display.get_surface() else None
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
    play_button_rect = pygame.Rect(700, 180, 105, 40)
    quit_button_rect = pygame.Rect(700, 245, 105, 40)

    mx, my = pygame.mouse.get_pos()

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
        cls.open()

    def load_menu_sprites_from_path(cls, path="res/menu"):
        """
        Recursively iterate through path and return a list of menu sprites.
        """

        with tqdm(
            total=len(os.listdir(path)),
            dynamic_ncols=True,
            desc=" 👀 Looking for files",
        ) as pbar:
            for j in os.listdir("res/menu"):
                try:
                    if j.endswith(".png"):
                        if j not in [
                            "old",
                            "background",
                            "menu.png",
                            "sign",
                            "sign_scaled.png",
                        ]:
                            image = pygame.image.load(
                                os.path.join("res", "menu", j)
                            ).convert_alpha()
                            cls.menu_sprites.append(image)
                finally:
                    pbar.update(1)

    @classmethod
    def sort_menu_sprites_by_pattern(cls):
        """
        Fetch menu sprites that match a given pattern.
        """
        for filename in sorted(os.listdir(cls.path)):
            if cls.pattern.match(filename):
                cls.menu_sprites.append(
                    pygame.image.load(os.path.join(
                        cls.path, filename)).convert_alpha()
                )

    @classmethod
    def draw_to_window(cls):
        """
        Draw menu to window.
        """
        cls.play_open_animation()
        cls.window.blit(cls.image, (0, 0))

    @classmethod
    def update(cls):
        # if user presses buttons
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                cls.mx, cls.my = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect.collidepoint(cls.play_button_rect, (cls.mx, cls.my)):
                    return False
                elif pygame.Rect.collidepoint(cls.quit_button_rect, (cls.mx, cls.my)):
                    pygame.quit()
                    sys.exit(0)

        cls.dt = cls.clock.tick(cls.fps) / 1000.0
        pygame.display.update()
        return True

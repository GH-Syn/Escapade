import os
import re
import sys

import pygame
from pygame.constants import SRCALPHA
from tqdm import tqdm


class Menu:
    pygame.display.init()
    window = pygame.display.get_surface() if pygame.display.get_surface() else None
    pygame.font.init()
    font = os.path.join("./res/fonts/Silkscreen", "slkscr.ttf")

    DEFAULT_MENU_BACKGROUND_COLOR = (25, 25, 25)

    clock = pygame.time.Clock()
    dt = 0
    fps = 24

    menu_sprites: list[pygame.SurfaceType] = []
    paths = []
    images = []
    paths: list[str] = paths

    path = "res/menu"
    pattern = re.compile(r"^open_menu_[1-6]\.png$")
    menu_sprites.clear()
    menu_sprites = []

    opening = True
    opening_frame = 0
    opening_tick = 0

    if window is not None:
        mask = pygame.Surface(window.get_size(), SRCALPHA)
    play_button_rect = pygame.Rect(700, 180, 105, 40)
    quit_button_rect = pygame.Rect(700, 245, 105, 40)

    mx, my = pygame.mouse.get_pos()

    def __init__(self):
        self.load_menu_sprites_from_path()
        self.sort_menu_sprites_by_pattern()
        Menu.image: pygame.Surface = Menu.menu_sprites[0]

    @classmethod
    def play_open_animation(cls):
        """Play main menu animation"""
        if not cls.opening:
            return
        if cls.opening_frame < len(cls.menu_sprites):
            cls.opening_tick += 1
            if cls.opening_tick >= 6:
                cls.image = cls.menu_sprites[cls.opening_frame]
                cls.opening_tick = 0
                cls.opening_frame += 1
            return

        cls.opening = False

    @classmethod
    def load_menu_sprites_from_path(cls, path="res/menu"):
        """Recursively iterate through path and return a list of menu sprites"""

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
        for filename in sorted(os.listdir(cls.path)):
            if cls.pattern.match(filename):
                cls.menu_sprites.append(
                    pygame.image.load(os.path.join(cls.path, filename)).convert_alpha()
                )

    @classmethod
    def draw_to_window(cls):
        """Draw menu to window"""
        cls.play_open_animation()
        cls.window.blit(cls.image, (0, 0))

    @classmethod
    def update_event_loop(cls):
        """Wait for user input from event loop"""
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

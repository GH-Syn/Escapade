import os
import pygame
import pygame_gui


class Menu:

    window = pygame.display.get_surface()
    font = os.path.join('res/fonts/Silkscreen', 'silkscr.ttf')

    GUI_manager = pygame_gui.UIManager(window.get_size())
    DEFAULT_MENU_BACKGROUND_COLOR = (25, 25, 25)

    clock = pygame.time.Clock()
    dt = 0
        
    @classmethod
    def draw(cls):
        cls.window.fill(cls.DEFAULT_MENU_BACKGROUND_COLOR)

    @classmethod
    def update(cls):
        cls.GUI_manager.update(cls.dt)
        cls.dt = cls.clock.tick(24) / 1000.0


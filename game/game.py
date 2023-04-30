import pygame
import pygame_gui


class Game:

    DEFAULT_GAME_BACKGROUND_COLOR = '#8d8d9b'
    window = pygame.display.get_surface()
    current_map = ...
    GUI_manager = pygame_gui.UIManager(window.get_size())
    dt = 0
    clock = pygame.time.Clock()

    @classmethod
    def draw(cls):
        Game.window.fill(Game.DEFAULT_GAME_BACKGROUND_COLOR)

    @classmethod
    def update(cls):
        Game.GUI_manager.update(Game.dt)
        Game.dt = Game.clock.tick(30) / 1000.0
        pygame.display.update()

import pygame


class Game:
    DEFAULT_GAME_BACKGROUND_COLOR = "#8d8d9b"
    window = pygame.display.get_surface()

    dt = 0
    clock = pygame.time.Clock()

    @classmethod
    def draw(cls):
        cls.window.fill(Game.DEFAULT_GAME_BACKGROUND_COLOR)

    @classmethod
    def update(cls):
        Game.dt = Game.clock.tick(30) / 1000.0
        pygame.display.update()

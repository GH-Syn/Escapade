"""
This module houses the game class which is responsible for calling the main game loop

module: game.game
   ⚪ draw
     ↪️ fills the window with the games background color
   ⚪ update
     ↪️ regulate deltatime and update frames

license: MIT
author: Joshua Rose
date: 07/05/2023
"""


import pygame

class Game:
    """
    Responsible for running game loop.
    """

    DEFAULT_GAME_BACKGROUND_COLOR = "#8d8d9b"
    window = pygame.display.get_surface()

    dt = 0
    clock = pygame.time.Clock()

    @classmethod
    def draw(cls):
        """
        Fill the window with game background color.
        """
        cls.window.fill(Game.DEFAULT_GAME_BACKGROUND_COLOR)

    @classmethod
    def update(cls):
        """
        Regulate time elapsed since last frame and update frames.
        """
        Game.dt = Game.clock.tick(30) / 1000.0
        pygame.display.update()

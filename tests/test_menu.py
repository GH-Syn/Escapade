import os
import unittest
import pytest
import pygame

from game.menu import Menu


class TestMenu(unittest.TestCase):
    def setUp(self) -> None:
        self.menu = Menu
        return super().setUp()

    @pytest.mark.skipif("DISPLAY" not in os.environ, reason="No display available")
    def test_window_is_not_none(self):
        if pygame.display.get_surface():
            self.assertIsNotNone(self.menu.window)
        else:
            self.assertIsNone(self.menu.window)

    def test_font_loaded(self):
        try:
            if pygame.font.get_init():
                self.assertTrue(pygame.font.get_init())
            else:
                pygame.font.init()
        finally:
            self.assertTrue(pygame.font.get_init())

    def test_surface_type(self):
        pygame.font.init()
        my_font = pygame.font.Font(self.menu.font, 8)
        self.assertIsInstance(my_font, pygame.font.FontType)
        random_render = my_font.render("text", True, (0, 0, 0), None)
        assert isinstance(random_render, pygame.SurfaceType)

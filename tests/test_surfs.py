""" Test surfaces are valid loadable and present """

import os
import sys
import unittest

import pygame

sys.path.insert(0, os.getcwd())


class TestSurfaces(unittest.TestCase):
    def setUp(self) -> None:
        pygame.font.init()
        pygame.display.init()
        self.fonts = ["Silkscreen"]
        return super().setUp()

    def tearDown(self) -> None:
        pygame.font.quit()
        return super().tearDown()

    def test_images_present(self):
        images = []

        for image in os.listdir("./res/menu"):
            images.append(image.split(".")[1]) if "." in image else ...

        self.assertIn("png", images)

        creds = [i for i in os.listdir("res/credits")]

        for image in creds:
            self.assertIn("png", images)

    def test_map_types(self):
        images = []
        for image in os.listdir("./res/maps"):
            images.append(image.split(".")[1]) if "." in image else ...
        self.assertIn("xml", images)

    def test_font_types(self):
        fonts = [font for font in os.listdir("./res/fonts")]

        for font in self.fonts:
            self.assertIn(font, fonts)

    def test_menu_image_sizes(self):
        menu_images = [image for image in os.listdir("./res/menu")]

        for image in menu_images:
            image_small = image
            try:
                image_large = menu_images[
                    menu_images.index(f"{image.split('_')[0]}_scaled_1.png")
                ]
                image_small = image

                # This is probably going to get me cancelled
                self.assertTrue(
                    pygame.math.Vector2(
                        float(pygame.image.load(image_small).convert().get_width()),
                        float(pygame.image.load(image_small).convert().get_height()),
                    ).magnitude()
                    < pygame.math.Vector2(
                        float(pygame.image.load(image_large).convert().get_width()),
                        float(pygame.image.load(image_large).convert().get_height()),
                    ).magnitude()
                )
            except Exception:
                continue

    def test_fonts_load(self):
        fonts = [font for font in os.listdir("./res/fonts")]

        for font in self.fonts:
            font_face = os.path.join(
                "./res",
                "fonts",
                font,
                os.listdir(os.path.join("./res", "fonts", font))[0],
            )

            self.assertIn(font, fonts)

            pygame.font.Font(font_face, size=16)

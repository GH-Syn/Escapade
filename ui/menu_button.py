import os
import pygame


class MenuButton(pygame.sprite.Sprite):
    font = pygame.font.Font(os.path.join("res/fonts/Silkscreen", "silkscr.ttf"))

    def __init__(self, y_position: tuple, text, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("res/ui/menu_button.png").convert()
        image_text_render = MenuButton.font.render(text, True, "#323e4f")

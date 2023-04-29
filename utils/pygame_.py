import pygame


def init(
    init_display=True,
    init_base=True,
    init_mixer=True,
    init_font=True,
):
    """Initialize components selectively.

    :param display: Handles visuals of pygame such as rendering and vfx
    :param base: The SDL backend of pygame
    :param mixer: Controls audio output in the pygame library
    :param fonts: Displays and renders system fonts
    """
    if init_base:
        pygame.base.init()
    if init_display:
        pygame.display.init()
    if init_mixer:
        pygame.mixer.pre_init()
    if init_font:
        pygame.font.init()

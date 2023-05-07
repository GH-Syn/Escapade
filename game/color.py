from game.consts import entity_colorkey

global e_colorkey
e_colorkey = entity_colorkey


def set_global_colorkey(colorkey):
    """Set the standard colorkey to apply to everything that is a loaded pygame image
    :param colorkey: colorkey as a tuple
    example: (255, 255, 255) would be white, removing white backgrounds
    (0, 0, 0) would be black and it would remove black backgrounds
    """

    global e_colorkey
    e_colorkey = colorkey


def swap_color(img, old_c, new_c):
    """Swap the color on two images

    :param img: Image surface to swap the color of
    :param old_c: The old image color
    :param new_c: New image color
    :return: pygame.surface.Surface
    """

    global e_colorkey

    img.set_colorkey(old_c)
    surf = img.copy()

    surf.fill(new_c)
    surf.blit(img, (0, 0))
    surf.set_colorkey(entity_colorkey)

    return surf

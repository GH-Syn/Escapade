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


import pygame


def fade_into_color(surface, duration, color):
    """
    Fades in the given surface over the specified duration using the specified color as a mask.
    """
    fade_surface = pygame.Surface((1500, 1000))
    fade_surface.fill(color)
    alpha = 0
    alpha_step = 255 / (duration / 30)  # 30 frames per second

    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    while alpha < 255:
        # Calculate current alpha value based on elapsed time
        elapsed_time = pygame.time.get_ticks() - start_time
        alpha = int(alpha_step * elapsed_time / 1000)
        if alpha > 255:
            alpha = 255

        # Draw fade surface onto main surface
        fade_surface.set_alpha(alpha)
        surface.blit(fade_surface, (0, 0))

        # Update display and wait for next frame
        pygame.display.update()
        clock.tick(30)


def emerge_from_color(surface, duration, color):
    """
    Fades out the given surface over the specified duration using the specified color as a mask.
    :param surface: Target surface to draw to
    :param duration: Duration in milliseconds
    :param color: rgb (tuple) or hex (as string) color value
    """

    fade_surface = pygame.Surface((1500, 1000))
    fade_surface.fill(color)
    alpha = 255
    alpha_step = 255 / (duration / 30)  # 30 frames per second

    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    while alpha > 0:
        # Calculate current alpha value based on elapsed time
        elapsed_time = pygame.time.get_ticks() - start_time
        alpha = 255 - int(alpha_step * elapsed_time / 1000)
        if alpha < 0:
            alpha = 0

        # Draw fade surface onto main surface
        fade_surface.set_alpha(alpha)
        surface.blit(fade_surface, (0, 0))

        # Update display and wait for next frame
        pygame.display.update()
        clock.tick(30)


def fade_out(source, target, duration):
    """
    Fades out the given surface by linearly decreasing its alpha value over time.
    :param source: Pygame window that everything is drawn to
    :param surface: Pygame surface to be faded out.
    :param duration: Time in milliseconds for the fade-out effect to complete.
    """
    alpha = 255  # initial alpha value
    alpha_step = 255 / duration  # amount to decrement alpha per millisecond

    # create a copy of the surface to avoid modifying the original
    faded_surface = target.copy()

    # set the initial alpha value of the faded surface
    faded_surface.set_alpha(alpha)

    # create a Pygame clock to track time elapsed
    clock = pygame.time.Clock()

    # loop until the surface is completely faded out
    while alpha > 0:
        # decrement the alpha value based on elapsed time
        elapsed = clock.tick()
        alpha -= alpha_step * elapsed

        # ensure alpha doesn't go below zero
        alpha = max(alpha, 0)

        # update the alpha value of the faded surface
        faded_surface.set_alpha(alpha)

        # draw the faded surface onto the screen
        source.blit(faded_surface, (0, 0))

        # update the Pygame display
        pygame.display.update()

    # return the final faded surface
    return faded_surface

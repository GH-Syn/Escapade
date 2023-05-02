import json
import sys
import os
import pygame


class SplashScreen:
    datafile = open("data/theme.json", "r")
    transition = json.load(datafile)["SplashScreen"]["default"]
    datafile.close()

    window = pygame.display.get_surface()

    surface = pygame.Surface(window.get_size(), pygame.SRCALPHA)

    # Define the colors and fonts for the splash screen
    background_color = transition["bg_color"]
    text_color = transition["text_color"]

    font_size = transition["font_size"]
    font = os.path.join("res/fonts/Silkscreen", "slkscr.ttf")

    label_text = "Escapade"
    label_font = pygame.font.Font(font, font_size)
    label_surf = label_font.render(label_text, True, text_color)

    # Get the center of the screen
    center_x = window.get_width() // 2
    center_y = window.get_height() // 2

    # Create the label rect and add it to the GUI manager
    label_rect = pygame.Rect(
        center_x - (label_surf.get_width() // 2),
        center_y - (label_surf.get_height() // 2),
        label_surf.get_width(),
        label_surf.get_height(),
    )

    done = False

    # Set the alpha of the label to 0 to start with
    label_surf.set_alpha(0)

    # Define the fade in/out time in seconds
    fade_time = transition["fade_time"] / 1000

    # Define the timer to control the fade in/out animation
    timer = pygame.time.Clock()
    current_time = 0.0
    alpha = 0

    @classmethod
    def update(cls):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return False
                elif event.key == pygame.K_ESCAPE:
                    return False

        # Update the GUI manager
        delta_time = cls.timer.tick(60) / 1000.0
        cls.current_time += delta_time

        # Fade in/out the label
        if cls.current_time < cls.fade_time:
            # Fade in
            alpha = int(255 * (cls.current_time / cls.fade_time))
        elif cls.current_time > (cls.fade_time * 2):
            # Fade out and quit
            alpha = int(
                255 - (255 * ((cls.current_time - (cls.fade_time * 2)) / cls.fade_time))
            )
            if alpha <= 0:
                cls.done = True
                return False
        else:
            # Hold for a moment
            alpha = 255

        cls.label_surf.set_alpha(alpha)
        return True

    @classmethod
    def draw(cls):
        """Draw to screen as declared in class var"""

        cls.surface.fill(cls.background_color)
        cls.surface.blit(cls.label_surf, cls.label_rect)
        cls.window.blit(cls.surface, (0, 0))

        pygame.display.update()

import os
from .color import swap_color
import pygame
from .consts import entity_colorkey
from .engine import blit_center

global e_colorkey, particle_images

e_colorkey = entity_colorkey
particle_images = {}

class Particle(object):
    """Basic particle class that has simple movement, colors and what not."""

    def __init__(
        self,
        x: int | float,
        y: int | float,
        particle_type: str,
        motion: list[int | float],
        decay_rate: int | float,
        start_frame: int,
        custom_color: None | tuple = None,
    ):
        """Particle class to display basic particles.
        :param x: The x position of a particle
        :param y: The y position of the particle
        :param particle_type: differentiates the particle with a string to do different physics
        :param motion: The direction of the particle
        :param decay_rate: The rate at which the particle decreases in radius
        :start_frame: The frame at which the particle starts to move
        :custom color: An optional color for the particle
        """

        self.x = x
        self.y = y
        self.type = particle_type
        self.motion = motion
        self.decay_rate = decay_rate
        self.color = custom_color
        self.frame = start_frame

    @staticmethod
    def particle_file_sort(l):
        """Sorts a given list of particles

        :param l: List of particles to sort
        :type l: list
        :return: A list of sorted particles
        :rtype: list
        """

        l2 = [int(obj[:-4]) for obj in l]

        l2.sort()

        l3 = [str(obj) + ".png" for obj in l2]

        return l3

    @classmethod
    def load_particle_images(cls, path):
        """Load a list of particle images from a given path.

        This function is mainly for if you have a lot of particles that you wish to
        use that are different in appearance.

        :param path: The path (relative to the working directory) of the particle images.
        """

        global particle_images, e_colorkey

        file_list = os.listdir(path)

        for folder in file_list:
            try:
                img_list = os.listdir(path + "/" + folder)
                img_list = Particle.particle_file_sort(img_list)
                images = []
                for img in img_list:
                    images.append(
                        pygame.image.load(path + "/" + folder + "/" + img).convert()
                    )
                for img in images:
                    img.set_colorkey(e_colorkey)
                particle_images[folder] = images.copy()
            except:
                pass

    def draw(self, surface, scroll):
        """Blit the particle to screen.
        :param surface: Pygame surface to blit the particle to
        :param scroll: The camera offset
        """

        global particle_images

        if self.frame > len(particle_images[self.type]) - 1:
            self.frame = len(particle_images[self.type]) - 1
        if self.color == None:
            blit_center(
                surface,
                particle_images[self.type][int(self.frame)],
                (self.x - scroll[0], self.y - scroll[1]),
            )
        else:
            blit_center(
                surface,
                swap_color(
                    particle_images[self.type][int(self.frame)],
                    (255, 255, 255),
                    self.color,
                ),
                (self.x - scroll[0], self.y - scroll[1]),
            )

    def update(self):
        """Update the particles motion variables and decreate radius"""
        self.frame += self.decay_rate
        running = True

        if self.frame > len(particle_images[self.type]) - 1:
            running = False

        self.x += self.motion[0]
        self.y += self.motion[1]

        return running

"""
This module houses functions that help the game run.

module: game.engine
   ⚪ set_global_colorkey
     ↪️ Set the standard colorkey to apply to everything that is a loaded pygame image
   ⚪ collision_test
     ↪️ Tests if an object is colliding with any entity in `object_list`

license: MIT
author: Joshua Rose
date: 07/05/2023
"""

import pygame
from game.entity import Entity
from game.consts import entity_colorkey

global e_colorkey
e_colorkey = entity_colorkey


def collision_test(object_1, object_list: list):
    """Tests if an object is colliding with any entity in `object_list`

    :param object_1: Object as a sprite
    :param object_list: list containing 1 or more sprites
    :return: bool
    """

    collision_list = []
    for obj in object_list:
        if obj.rect.colliderect(object_1.rect):
            collision_list.append(obj)
    return collision_list

def simple_entity(x: int, y: int, e_type: str):
    """A simple entity with very basic properties (inherits Entity as used)

    :param x: X position of entity
    :param y: Y position of entity
    :param e_type: Entity type as a string
    :return `Entity`:
    """

    return Entity(x, y, 1, 1, e_type)


def flip(img: pygame.SurfaceType, flip_up=True):
    """Flip image (vertically) from its current state to a flipped image state

    :param flip_up: flips the image up if true and down if false
    :return: pygame.surface.Surface
    """

    return pygame.transform.flip(img, flip_up, False)


def blit_center(surf: pygame.SurfaceType, surf2: pygame.SurfaceType, pos):
    """Blit an image to the center of a given surface listed as `pos`
    :param surf: The surface in question to blit to or the (parent) surface
    :param surf2: The surface in which you would like to change the position to
    :param pos: The position (current position) of `surf2`
    """

    x = int(surf2.get_width() / 2)
    y = int(surf2.get_height() / 2)
    surf.blit(surf2, (pos[0] - x, pos[1] - y))


# animation stuff

global animation_database  # pyright: ignore
animation_database = {}

global animation_higher_database  # pyright: ignore
animation_higher_database = {}

Entity.animation_database = animation_database
Entity.animation_higher_database = animation_higher_database


def animation_sequence(
    sequence: list[list[int]],
    base_path: str,
    colorkey=(255, 255, 255),
    transparency=255,
):
    """Load an animation sequence from a given path.

    :param sequence: A list containing elements that follow the convention of [int_a, int_b]
    For example, a sequence might look like [[0,1],[1,1],[2,1],[3,1],[4,2]]
    The first numbers are the image name(as integer), while the second number shows the duration of it in the sequence
    :param base_path: The path in which to load the animation sequence from relative to the working directory
    :param colorkey: The colorkey (transparency mask): to give
    :param transparency: The alpha/opacity value at which to render the animation at
    """

    global animation_database

    result = []

    for frame in sequence:
        image_id = base_path + base_path.split("/")[-2] + "_" + str(frame[0])
        image = pygame.image.load(image_id + ".png").convert()
        image.set_colorkey(colorkey)
        image.set_alpha(transparency)

        animation_database[image_id] = image.copy()

        [result.append(image_id) for _ in range(frame[1])]

    return result


def get_animation_database():
    return animation_database


def get_animation_higher_database():
    return animation_higher_database


def get_frame(ID):
    """Get the given frame in the animation database"""
    global animation_database
    return animation_database[ID]


def load_animations(path: str):
    """Load animations from a text file

    :param path: Path of text file to load animations from

    no return value(s)
    """

    global animation_higher_database, e_colorkey

    data = []

    with open(path + "entity_animations.txt", "r") as f:
        data = f.read()
        f.close()

    for animation in data.split("\n"):
        sections = animation.split(" ")
        anim_path = sections[0]

        entity_info = anim_path.split("/")
        entity_type = entity_info[0]

        animation_id = entity_info[1]
        timings = sections[1].split(";")
        tags = sections[2].split(";")
        sequence = []

        n = 0

        for timing in timings:
            sequence.append([n, int(timing)])
            n += 1

        anim = animation_sequence(sequence, path + anim_path, e_colorkey)

        if entity_type not in animation_higher_database:
            animation_higher_database[entity_type] = {}
        animation_higher_database[entity_type][animation_id] = [anim.copy(), tags]

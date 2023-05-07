import math
import os

import pygame

global e_colorkey
e_colorkey = (255, 255, 255)


def set_global_colorkey(colorkey):
    """Set the standard colorkey to apply to everything that is a loaded pygame image
    :param colorkey: colorkey as a tuple
    example: (255, 255, 255) would be white, removing white backgrounds
    (0, 0, 0) would be black and it would remove black backgrounds
    """

    global e_colorkey
    e_colorkey = colorkey



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


<<<<<<< Updated upstream
class PhysicsObject(object):
    """2D physics object used for basic movement and collision"""

    def __init__(self, x, y, x_size, y_size):
        """Physics object constructor with basic parameters.
        :param x: X position of object
        :param y: Y position of object
        :param x_size: The width of the object
        :param y_size: The height of the object
        """

        self.width = x_size
        self.height = y_size
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.x = x
        self.y = y
        self.vel = pygame.math.Vector2(0, 0)

    def move(self, movement):
        """Move physics object in a given direction provided by `movement`

        :param movement: The movement as a list with elements (integers) that dictate the movment direction.
        Example of what `movement` might look like: [1, -2] 1 is the x (positive) and -2 is the y (negative)
        So moving forwards 1 in the x direction is the same as moving right, and moving -2 in the y directoin is the same as moving up.

        """

        self.vel.x = movement[0]
        self.vel.y = movement[1]

        self.rect.x = int(self.vel.x)
        self.rect.y = int(self.vel.y)
    
    def collide(self, platforms, ramps):
        """Collide with objects platforms and ramps

        :param platforms: A list of platforms (as a list) to detect collision with.
        :param ramps: Any ramps (sprites with diagonal sides) that need to be mentioned (default=[])
        """

        ramps = ramps
        block_hit_list = collision_test(self.rect, platforms)
        collision_types = {
            "top": False,
            "bottom": False,
            "right": False,
            "left": False,
            "slant_bottom": False,
            "data": [],
        }

        # added collision data to "collision_types". ignore the poorly chosen variable name
        for block in block_hit_list:
            markers = [False, False, False, False]
            if self.vel.x > 0:
                self.rect.right = block.left
                collision_types["right"] = True
                markers[0] = True
            elif self.vel.y < 0:
                self.rect.left = block.right
                collision_types["left"] = True
                markers[1] = True
            collision_types["data"].append([block, markers])
            self.x = self.rect.x

        self.y += self.vel.y
        self.rect.y = int(self.y)
        block_hit_list = collision_test(self.rect, platforms)

        for block in block_hit_list:
            markers = [False, False, False, False]
            if self.vel.y > 0:
                self.rect.bottom = block.top
                collision_types["bottom"] = True
                markers[2] = True
            elif self.vel.y < 0:
                self.rect.top = block.bottom
                collision_types["top"] = True
                markers[3] = True
            collision_types["data"].append([block, markers])
            self.change_y = 0
            self.y = self.rect.y

        return collision_types


def simple_entity(x, y, e_type):
=======
def simple_entity(x: int, y: int, e_type: str):
>>>>>>> Stashed changes
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


class Entity(object):
    """Entity object with rotation, speed, animation and various other actions"""

    global animation_database, animation_higher_database

    def __init__(self, x: int, y: int, size_x: int, size_y: int, e_type: str):
        """Entity constructor for setting size, entity type and position

        :param x: X position of entity
        :param y: Y position of entity
        :param size_x: width of entity
        :param size_y: height of entity
        :param e_type: Entity type as a string
        """

        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.obj = PhysicsObject(x, y, size_x, size_y)
        self.animation: None | int = None
        self.image = None
        self.animation_frame = 0
        self.animation_tags = []
        self.offset = [0, 0]
        self.rotation = 0
        self.type = e_type  # used to determine animation set among other things
        self.action_timer = 0
        self.action = ""
        # self.set_action("idle")  # overall action for the entity
        self.entity_data = {}
        self.alpha = None

    def set_pos(self, x, y):
        """Set the position of the entity

        :param x: X position to set entity to
        :param y: Y position to set entity to
        """

        self.x = x
        self.y = y
        self.obj.x = x
        self.obj.y = y
        self.obj.rect.x = x
        self.obj.rect.y = y

    def move(self, momentum):
        """Move entity in a given direction provided by `movement`

        :param momentum: The momentum as a list with elements (integers) that dictate the direction.
        Example of what `momentum` might look like: [1, -2] 1 is the x (positive) and -2 is the y (negative)
        So moving forwards 1 in the x direction is the same as moving right, and moving -2 in the y directoin is the same as moving up.
        """

        self.obj.move(momentum)

    def collide(self, platforms, ramps=[]):
        """
        :param platforms: A list of platforms (as a list) to detect collision with.
        :param ramps: Any ramps (sprites with diagonal sides) that need to be mentioned (default=[])
        """

        ramps = ramps

        collisions = self.obj.collide(platforms, ramps)
        self.x = self.obj.x
        self.y = self.obj.y
        return collisions

    @property
    def rect(self):
        """The rect property of the sprite/entity"""
        return pygame.Rect(self.x, self.y, self.size_x, self.size_y)

    @property
    def flip(self):
        """Boolean value returns if the sprite is flipped"""
        return self._flip

    @flip.setter
    def flip(self, flipped=False):
        self._flip = flipped

    @property
    def tags(self):
        """Entity tags that dictate the physics movement and so forth"""
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Give the animation tags so that properties can be applied dependant on said tags

        :param tags: Tags as a  list of strings
        """

        self._tags = tags

    def set_animation(self, sequence: list[pygame.SurfaceType]):
        """
        # Short description
        Set animation sequence to a different animation

        ## About
        This is commonly used when the player or any other entity needs to change the
        current active animation that they are doing for

        ### Example
        if the player is moving
        and needs to then transform their animation into the idle animation because their
        velocity has reached 0 then the set_animatoin function would be called.
        This would set the animation frame to 0 (meaning that the animation would start from
        the very beginning) and also sets the self.animation to sequence so that all the
        other functions know what the entity is currently doing as an animation.

        :param `sequence`: The sequence of images to set the animation to as a list of surfaces
        """

        self.animation = sequence  # pyright: ignore
        self.animation_frame = 0

    def set_action(self, action_id, force=False):
        """Set the current action of the entity.

        :param action_id: The id of the action as a real/integer
        :param force: Whether the action should be imposed on the entity (bool)
        """

        if (self.action == action_id) and (force == False):
            return
        else:
            self.action = action_id
            anim = animation_higher_database[self.type][action_id]
            self.animation = anim[0]
            self.tags(anim[1])
            self.animation_frame = 0

    def get_entity_angle(self, entity_2):
        """Returns the angle of the entity in relation to `entity_2`

        :param `entity_2`: The second entity to compare the angle between (as a sprite)
        :return: Angle in degrees
        :rtype: float
        """

        x1, y1 = self.x + int(self.size_x / 2), self.y + int(self.size_y / 2)
        x2, y2 = entity_2.x + int(entity_2.size_x / 2), entity_2.y + int(
            entity_2.size_y / 2
        )
        angle = math.atan((y2 - y1) / (x2 - x1))

        if x2 < x1:
            angle += math.pi

        return angle

    def get_center(self):
        """Returns the center of the current sprite.

        :return: center of sprite as a list
        :rtype: list[int, int]
        """

        x = self.x + int(self.size_x / 2)
        y = self.y + int(self.size_y / 2)
        return [x, y]

    def clear_animation(self):
        """Sets the animation property to None"""

        self.animation = None

    def set_image(self, image):
        """Sets the current entity image to `image`

        :param `image`: Image as a pygame Surface type
        """

        self.image = image

    def set_offset(self, offset):
        """Sets the sprite offset when rendering (relative to `scroll`)

        :param offset: Offset as a list of integers
        -------
        ### example:
        >>> # this is normally done in pixels
        >>> [2, 5]
        """

        self.offset = offset

    def set_frame(self, amount: int):
        """Sets the current frame of the animation

        :param `amount`: frame of the animation to goto
        """

        self.animation_frame = amount

    def handle(self):
        """Increments the action timer and sets the frame to 1"""
        self.action_timer += 1
        self.change_frame(1)

    def change_frame(self, amount: int):
        """Changes the frame to a given amount

        :param amount: The amount of frames to set
        :type amount: int
        :rtype: None
        """

        self.animation_frame += amount
        if self.animation != None:
            while self.animation_frame < 0:
                if "loop" in self.animation_tags:
                    self.animation_frame += len(self.animation)  # pyright: ignore
                else:
                    self.animation = 0
            while self.animation_frame >= len(self.animation):  # pyright: ignore
                if "loop" in self.animation_tags:
                    self.animation_frame -= len(self.animation)  # pyright: ignore
                else:
                    self.animation_frame = len(self.animation) - 1  # pyright: ignore

    def get_current_img(self):
        if self.animation == None:
            if self.image != None:
                return flip(self.image, self.flip)
            else:
                return None
        else:
            return flip(
                animation_database[
                    self.animation[self.animation_frame]  # pyright: ignore
                ],  # pyright: ignore
                self.flip,  # pyright: ignore
            )

    def get_drawn_img(self):
        """Returns the current active image of the entity (currently shown)"""
        image_to_render = None
        if self.animation == None:
            if self.image != None:
                image_to_render = flip(self.image, self.flip).copy()
        else:
            image_to_render = flip(
                animation_database[
                    self.animation[self.animation_frame]  # pyright: ignore
                ],  # pyright: ignore
                self.flip,  # pyright: ignore
            ).copy()
        if image_to_render != None:
            center_x = image_to_render.get_width() / 2
            center_y = image_to_render.get_height() / 2
            image_to_render = pygame.transform.rotate(image_to_render, self.rotation)
            if self.alpha != None:
                image_to_render.set_alpha(self.alpha)
            return image_to_render, center_x, center_y

    def display(self, surface, scroll):
        image_to_render = None
        if self.animation == None:
            if self.image != None:
                image_to_render = flip(self.image, self.flip).copy()
        else:
            image_to_render = flip(
                animation_database[
                    self.animation[self.animation_frame]  # pyright: ignore
                ],  # pyright: ignore
                self.flip,  # pyright: ignore
            ).copy()
        if image_to_render != None:
            center_x = image_to_render.get_width() / 2
            center_y = image_to_render.get_height() / 2
            image_to_render = pygame.transform.rotate(image_to_render, self.rotation)
            if self.alpha != None:
                image_to_render.set_alpha(self.alpha)
            blit_center(
                surface,
                image_to_render,
                (
                    int(self.x) - scroll[0] + self.offset[0] + center_x,
                    int(self.y) - scroll[1] + self.offset[1] + center_y,
                ),
            )


# animation stuff

global animation_database  # pyright: ignore
animation_database = {}

global animation_higher_database  # pyright: ignore
animation_higher_database = {}


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

<<<<<<< Updated upstream
        animation_higher_database[entity_type][animation_id] = [anim.copy(), tags]


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


global particle_images
particle_images = {}


def load_particle_images(path):
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
            img_list = particle_file_sort(img_list)
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
    surf.set_colorkey(e_colorkey)

    return surf
=======
        animation_higher_database[entity_type][animation_id] = [
            anim.copy(), tags]
>>>>>>> Stashed changes

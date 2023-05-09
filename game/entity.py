import math
import pygame


import game.engine
import game.physics_object


class Entity(object):
    """Entity object with rotation, speed, animation and various other actions"""

    animation_database = {}
    animation_higher_database = {}

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
        self.obj = game.physics_object.PhysicsObject(x, y, size_x, size_y)
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

        self.animation = sequence
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
            anim = Entity.animation_higher_database[self.type][action_id]
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
                    self.animation_frame += len(self.animation)
                else:
                    self.animation = 0
            while self.animation_frame >= len(self.animation):
                if "loop" in self.animation_tags:
                    self.animation_frame -= len(self.animation)
                else:
                    self.animation_frame = len(self.animation) - 1

    def get_current_img(self):
        if self.animation == None:
            if self.image != None:
                return game.engine.flip(self.image, self.flip)
            else:
                return None
        else:
            return game.engine.flip(
                Entity.animation_database[
                    self.animation[self.animation_frame]
                ],
                self.flip,
            )

    def get_drawn_img(self):
        """Returns the current active image of the entity (currently shown)"""
        image_to_render = None
        if self.animation == None:
            if self.image != None:
                image_to_render = game.engine.flip(self.image, self.flip).copy()
        else:
            image_to_render = game.engine.flip(
                Entity.animation_database[
                    self.animation[self.animation_frame]
                ],
                self.flip,
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
                image_to_render = game.engine.flip(self.image, self.flip).copy()
        else:
            image_to_render = game.engine.flip(
                Entity.animation_database[
                    self.animation[self.animation_frame]
                ],
                self.flip,
            ).copy()
        if image_to_render != None:
            center_x = image_to_render.get_width() / 2
            center_y = image_to_render.get_height() / 2
            image_to_render = pygame.transform.rotate(image_to_render, self.rotation)
            if self.alpha != None:
                image_to_render.set_alpha(self.alpha)
            game.engine.blit_center(
                surface,
                image_to_render,
                (
                    int(self.x) - scroll[0] + self.offset[0] + center_x,
                    int(self.y) - scroll[1] + self.offset[1] + center_y,
                ),
            )

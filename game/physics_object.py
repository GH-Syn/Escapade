import pygame


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



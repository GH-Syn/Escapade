
import os
import sys

sys.path.insert(0, os.getcwd())

from game.engine import *


import unittest


class TestPhysicsObject(unittest.TestCase):
    def setUp(self) -> None:

        self.physics_object = PhysicsObject(10, 10, 10, 10)

        return super().setUp()

    def tearDown(self) -> None:
        self.physics_object.vel.x = 0
        self.physics_object.vel.y = 0
        self.physics_object.rect.x = 10
        self.physics_object.rect.y = 10

        return super().tearDown()
    def test_movement_object(self):
        self.physics_object.move([53, -33])

        self.assertTrue(self.physics_object.vel.x, 53)
        self.assertTrue(self.physics_object.vel.y, -33)
        
    def test_collision_rect_on_movement(self):
        self.physics_object.move([-10, -20])
        self.assertTrue(self.physics_object.rect.x,
                        int(self.physics_object.vel.x))
        self.assertTrue(self.physics_object.rect.y,
                        int(self.physics_object.vel.y))

    def test_collision_object(self):
        self.physics_object.collide

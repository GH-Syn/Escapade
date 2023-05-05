import os
import sys

sys.path.insert(0, os.getcwd())

from game.engine import *


import unittest


class TestEngine(unittest.TestCase):
    def setUp(self) -> None:
        animation_higher_database["rock"] = {}
        animation_higher_database["boulder"] = {}
        animation_higher_database["enemy"] = {}
        animation_higher_database["player"] = {}
        animation_higher_database["idle"] = {}

        return super().setUp()

    def test_global_colorkey(self):
        colorkey = (0, 0, 0)
        set_global_colorkey(colorkey)
        self.assertTrue(e_colorkey, colorkey)

    def test_collision(self):
        objects = [simple_entity(10, 10, "rock"), simple_entity(50, 50, "boulder")]

        player_entity = simple_entity(10, 10, "player")

        self.assertTrue(collision_test(player_entity, objects))


class TestPhysicsObject(unittest.TestCase):
    def setUp(self) -> None:
        self.physics_object = PhysicsObject(10, 10, 10, 10)

        return super().setUp()

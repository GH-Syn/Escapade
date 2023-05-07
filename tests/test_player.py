import unittest

import entities.player
from game.screen_size import height, width



class TestPlayer(unittest.TestCase):
    """ Tests player methods and properties """
    def setUp(self) -> None:
        self.player = entities.player.Player(position=(10, 10))
        return super().setUp()
    
    def test_fail_on_invalid_position_spawn(self):
        """This test should fail to spawn the player if spawned off-screen.
        """

        # TODO account for player size in px
        assert self.player.position.x >= 0 <= width
        assert self.player.position.y >= 0 <= height

    def test_attack_property(self):
        """ Test that the attack property functions as it should.

        Ensures that:
         - getter, setter, default property methods work
         - data type for setter property is valid
        """

        self.player.attacking = True
        self.player.current_animation = "idle"

        self.assertFalse(self.player.attacking == True)

        self.player.attacking = False
        self.player.current_animation = "attack"

        # Ensures property value via setter `value` parameter
        if self.player.current_animation == "attack":
            pass

        self.assertTrue(self.player.attacking)

    def test_moving_property(self):
        """ Test that the moving property works """

        self.player.velocity.xy = Vector2(5.0, 5.0)

        self.player.moving = False

        if self.player.moving:
            pass

        self.assertTrue(self.player.moving)

    def test_animation_property(self):
        """ Test that the animation property works """

        self.player.current_animation = "attack"

        self.assertTrue(self.player.animation == self.player.current_animation)

        self.player.current_animation = "heal"

        self.assertTrue(self.player.animation == "heal")

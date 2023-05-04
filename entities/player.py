import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self,
                 position: tuple[int | float, int | float],
                 *groups) -> None:
        super().__init__(*groups)

        self.position = pygame.Vector2(*position)

        self.accel = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(0, 0)

        self.images = pygame.image.load

        self.frame = 0
        self.tick = 0
        self.max_tick = 8

        self.current_animation: str = "idle"

    def animate(self):
        pass

    def move(self):
        pass
    
    def draw(self):
        pass

    def update(self):
        pass

    def place(self):
        pass

    def attack(self):
        pass

    @property
    def animation(self):
        """ Current player animation """
        return self._animation

    @animation.setter
    def animation(self, value: str):
        self._animation = value

    @animation.getter
    def animation(self):
        return self.current_animation

    @property
    def moving(self):
        """ Returns true if velocity is greater than 0 """
        return self._moving

    @moving.setter
    def moving(self, value: bool):
        self._moving = value

    @moving.getter
    def moving(self):
        return self.velocity.magnitude().__gt__(0)
    
    @property
    def attacking(self):
        """ Returns true if the player is in attacking animation/mode """
        return self._attacking
    
    @attacking.setter
    def attacking(self, value: bool):
        self._attacking = value

    @attacking.getter
    def attacking(self):
        return self.current_animation.__eq__("attack")

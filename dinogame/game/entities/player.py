import os
from typing import Tuple

import pygame

PLAYER_FILE = "../../assets/player.png"
COLOR_KEY = (0, 0, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self, position: Tuple[float, float], gravity: float = 1, jump_velocity: float = 14):
        super(Player, self).__init__()

        sprite = pygame.image.load(os.path.join(os.path.dirname(__file__), PLAYER_FILE))

        sprite.set_colorkey(COLOR_KEY)

        self._images = {
            "still": sprite.subsurface((0, 0, 44, 47)).convert(),
            "run": [
                sprite.subsurface((44, 0, 44, 47)).convert(),
                sprite.subsurface((88, 0, 44, 47)).convert()
            ],
            "dead": sprite.subsurface((132, 0, 44, 47)).convert(),
            "crouched": [
                sprite.subsurface((176, 17, 59, 30)).convert(),
                sprite.subsurface((235, 17, 59, 30)).convert()
            ]
        }

        self.image = self._images["still"]
        self.rect = self.image.get_rect()

        self.rect.left = position[0]
        self.rect.bottom = position[1]

        self._gravity = gravity
        self._jump_velocity = jump_velocity
        self._still_y = position[1]
        self._ddy = 0

    def die(self):
        self.image = self._images["dead"]

    def jump(self):
        if self._ddy == 0:
            self._ddy = -self._jump_velocity

    def crouch(self):
        pass

    def update(self):
        self.rect.bottom += self._ddy
        self._ddy += self._gravity

        if self.rect.bottom >= self._still_y:
            self.rect.bottom = self._still_y
            self._ddy = 0

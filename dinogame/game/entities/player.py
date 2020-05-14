import math
import os
from enum import Enum
from typing import Tuple

import pygame

_COLOR_KEY = (0, 0, 0)


class Player(pygame.sprite.Sprite):
    _SPRITE_FILE = "../../assets/player.png"

    class State(Enum):
        STILL = 0
        RUNNING = 1
        JUMPING = 2
        CROUCHED = 3
        DEAD = 4

    def __init__(self, position: Tuple[float, float], gravity: float = 1, jump_velocity: float = 14):
        super(Player, self).__init__()

        sprite = pygame.image.load(os.path.join(os.path.dirname(__file__), Player._SPRITE_FILE))

        sprite.set_colorkey(_COLOR_KEY)

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
        self._still_x = position[0]
        self._still_y = position[1]
        self._ddy = 0

        self._animation_count = 0

        self._try_to = Player.State.STILL
        self._state = Player.State.STILL

    def run(self):
        self._try_to = Player.State.RUNNING

    def jump(self):
        self._try_to = Player.State.JUMPING

    def crouch(self):
        self._try_to = Player.State.CROUCHED

    def stand_up(self):
        self._try_to = Player.State.RUNNING

    def die(self):
        self._state = Player.State.DEAD

        y = self.rect.bottom
        self.image = self._images["dead"]
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.left = self._still_x

    def update(self):
        # fast return to soil
        if self._state == Player.State.JUMPING and self._try_to == Player.State.CROUCHED:
            self._ddy = self._jump_velocity

        # start jump
        if self._state == Player.State.RUNNING and self._try_to == Player.State.JUMPING:
            self._state = Player.State.JUMPING
            self._ddy = -self._jump_velocity

        # handle velocity during jump
        if self._state == Player.State.JUMPING:
            if self._try_to == Player.State.JUMPING:
                self._try_to = Player.State.RUNNING

            self.rect.bottom += self._ddy
            self._ddy += self._gravity

            if self.rect.bottom >= self._still_y and self._ddy > 0:
                self._state = Player.State.RUNNING
                self.rect.bottom = self._still_y
                self._ddy = 0

        # go to crouched state
        if self._state == Player.State.RUNNING and self._try_to == Player.State.CROUCHED:
            self._state = Player.State.CROUCHED

            y = self.rect.bottom
            self.image = self._images["crouched"][0]
            self.rect = self.image.get_rect()
            self.rect.bottom = y
            self.rect.left = self._still_x - 5

        # go to running state
        if self._state == Player.State.CROUCHED and self._try_to == Player.State.RUNNING or \
                self._state == Player.State.STILL and self._try_to == Player.State.RUNNING:
            self._state = Player.State.RUNNING

            y = self.rect.bottom
            self.image = self._images["run"][0]
            self.rect = self.image.get_rect()
            self.rect.bottom = y
            self.rect.left = self._still_x

        # run animation
        self._animation_count = 0 if self._animation_count >= 9 else self._animation_count + 1
        frame = math.trunc(self._animation_count / 5)
        if self._state == Player.State.RUNNING:
            self.image = self._images["run"][frame]

        elif self._state == Player.State.CROUCHED:
            self.image = self._images["crouched"][frame]

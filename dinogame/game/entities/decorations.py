import os
import random
from typing import Tuple

import pygame

from .moving_object import MovingObject

_COLOR_KEY = (0, 0, 0)


class Decorations(pygame.sprite.Group):
    def __init__(self,
                 stage_width: float,
                 clouds_vertical_position: Tuple[float, float],
                 cloud_spawn_rate: float = 0.005):
        super(Decorations, self).__init__()

        self._stage_width = stage_width

        self._clouds_y = clouds_vertical_position

        self._cloud_spawn_rate = cloud_spawn_rate

    def update(self, dx: float = 0.7):
        if random.random() < self._cloud_spawn_rate:
            self.add(Cloud((self._stage_width + 20, random.uniform(*self._clouds_y))))

        super(Decorations, self).update(dx)


class Cloud(MovingObject):
    _SPRITE_FILE = "../../assets/cloud.png"

    def __init__(self, position: Tuple[float, float]):
        super(Cloud, self).__init__()

        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), Cloud._SPRITE_FILE)).convert()

        self.image.set_colorkey(_COLOR_KEY)

        self.rect = self.image.get_rect()

        self.rect.center = position


    def _on_out_of_screen(self):
        self.kill()

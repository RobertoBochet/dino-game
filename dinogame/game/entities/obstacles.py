import math
import os
import random
from typing import Tuple

import pygame

FLYER_FILE = "../../assets/flyer.png"
COLOR_KEY = (0, 0, 0)


class Obstacles(pygame.sprite.Group):
    def __init__(self, stage_width: float):
        super(Obstacles, self).__init__()

        self._stage_width = stage_width

        self._flyer_vertical_spawn = [40, 70, 100]

    def update(self, dx: int = 5, flyers_spawn_rate: float = 0.001):
        if random.random() < flyers_spawn_rate:
            self.add(Flyer((self._stage_width + 20, random.choice(self._flyer_vertical_spawn))))

        super(Obstacles, self).update()


class Flyer(pygame.sprite.Sprite):
    def __init__(self, position: Tuple[float, float]):
        super(Flyer, self).__init__()

        sprite = pygame.image.load(os.path.join(os.path.dirname(__file__), FLYER_FILE))
        sprite.set_colorkey(COLOR_KEY)

        _, _, w, h = sprite.get_rect()

        self._images = [
            sprite.subsurface((0, 0, w / 2, h)).convert(),
            sprite.subsurface((w / 2, 0, w / 2, h)).convert()
        ]

        self.image = self._images[0]

        self.rect = self.image.get_rect()

        self.rect.center = position

        self._animation_count = 0

    def update(self, dx: int = 5):
        self.rect.right -= dx

        if self.rect.right < 0:
            self.kill()

        # run animation
        self._animation_count = 0 if self._animation_count >= 59 else self._animation_count + 1
        frame = math.trunc(self._animation_count / 30)
        self.image = self._images[frame]

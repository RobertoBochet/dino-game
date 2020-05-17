import logging
import math
import os
import random

import pygame
from pygame.surface import Surface

from .moving_object import MovingObject

_COLOR_KEY = (0, 0, 0)

_LOGGER = logging.getLogger(__package__)


class Obstacles(pygame.sprite.Group):
    def __init__(self, stage_width: float):
        super(Obstacles, self).__init__()

        Cactus._STAGE_WIDTH = stage_width
        Flyer._STAGE_WIDTH = stage_width

        Cactus._GROUND_POSITION = 130
        Flyer._VERTICAL_SPAWN = [40, 70, 100]

        Cactus.create_sprites()


class Obstacle(MovingObject):
    _STAGE_WIDTH: int

    def _set_sprite(self, sprite: Surface):
        self.image = sprite

        self.rect = self.image.get_rect()

        self.rect.left = self._STAGE_WIDTH

    def _on_out_of_screen(self):
        self.kill()


class Flyer(Obstacle):
    _SPRITE_FILE = "../../assets/flyer.png"
    _VERTICAL_SPAWN = []

    def __init__(self):
        super(Flyer, self).__init__()

        sprite = pygame.image.load(os.path.join(os.path.dirname(__file__), Flyer._SPRITE_FILE))
        sprite.set_colorkey(_COLOR_KEY)

        _, _, w, h = sprite.get_rect()

        self._images = [
            sprite.subsurface((0, 0, w / 2, h)).convert(),
            sprite.subsurface((w / 2, 0, w / 2, h)).convert()
        ]

        self._set_sprite(self._images[0])

        self.rect.y = random.choice(Flyer._VERTICAL_SPAWN)-h/2

        self._animation_count = 0

        _LOGGER.info("Created a new flyer")

    def update(self, dx: float):
        super(Flyer, self).update(dx)

        # run animation
        self._animation_count = 0 if self._animation_count >= 59 else self._animation_count + 1
        frame = math.trunc(self._animation_count / 30)
        self.image = self._images[frame]


class Cactus(Obstacle):
    _SPRITE_FILE = "../../assets/cactus.png"
    _SPRITES = []

    _GROUND_POSITION: int

    def __init__(self, max_size: float):
        super(Cactus, self).__init__()

        possible_sprites = list(filter(lambda x: x[0] <= max_size, Cactus._SPRITES))

        if len(possible_sprites) == 0:
            possible_sprites = [Cactus._SPRITES[0]]

        self._set_sprite(random.choice(possible_sprites)[1])

        self.rect.bottom = Cactus._GROUND_POSITION

        _LOGGER.info("Created a new cactus with size of {}".format(self.image.get_width()))

    @staticmethod
    def create_sprites():
        sprite = pygame.image.load(os.path.join(os.path.dirname(__file__), Cactus._SPRITE_FILE))

        images = [
            sprite.subsurface((0, 0, 17, 35)),
            sprite.subsurface((17, 0, 17, 35)),
            sprite.subsurface((34, 0, 17, 35)),
            sprite.subsurface((51, 0, 17, 35)),
            sprite.subsurface((68, 0, 17, 35)),
            sprite.subsurface((85, 0, 17, 35)),
            sprite.subsurface((102, 0, 25, 50)),
            sprite.subsurface((127, 0, 24, 50)),
            sprite.subsurface((151, 0, 25, 50)),
            sprite.subsurface((176, 0, 75, 50))
        ]

        Cactus._SPRITES = []

        widths = [17, 34, 55]

        for i, j in zip([0, *widths], [*widths, 1000]):
            for _ in range(5):
                cw = 0
                c = []
                while cw <= i:
                    v = random.choice(images)
                    w = v.get_width()

                    if cw + w > j:
                        continue

                    c.append((cw, v))
                    cw += w
                s = pygame.Surface((cw, 50))

                for x, v in c:
                    s.blit(v, (x, 50 - v.get_height()))

                s.set_colorkey(_COLOR_KEY)

                Cactus._SPRITES.append((cw, s.convert()))

        Cactus._SPRITES.sort(key=lambda t: t[0])

        Cactus._sprites_min_width = Cactus._SPRITES[0][0]
        Cactus._sprites_max_width = Cactus._SPRITES[-1][0]

        Cactus._SPRITES = list(map(lambda i: (
            (i[0] - Cactus._sprites_min_width) / (Cactus._sprites_max_width - Cactus._sprites_min_width),
            i[1]
        ), Cactus._SPRITES))

        _LOGGER.info("Generate cactus' sprites")

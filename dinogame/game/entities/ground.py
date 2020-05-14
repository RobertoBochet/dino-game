import logging
import os

import pygame

GROUND_FILE = "../../assets/ground.png"
COLOR_KEY = (0, 0, 0)

_LOGGER = logging.getLogger(__package__)


class Ground(pygame.sprite.Group):
    def __init__(self, ground_position: float):
        super(Ground, self).__init__()

        self.add(GroundPiece(ground_position, 0, 2))
        self.add(GroundPiece(ground_position, 1, 2))

    def update(self, dx: int):
        super(Ground, self).update(dx)


class GroundPiece(pygame.sprite.Sprite):
    def __init__(self, ground_position: float, piece: int, pieces: int):
        super(GroundPiece, self).__init__()

        sprite = pygame.image.load(os.path.join(os.path.dirname(__file__), GROUND_FILE))

        sprite.set_colorkey(COLOR_KEY)

        w, h = sprite.get_size()

        self._dw = w

        self.image = sprite.subsurface((piece * w / pieces, 0, w / pieces, h)).convert()
        self.rect = self.image.get_rect()

        self.rect.top = ground_position
        self.rect.left = piece * w / pieces

    def update(self, dx: int):
        self.rect.x -= int(dx)

        if self.rect.right < 0:
            self.rect.left += self._dw

import os

import pygame

from .moving_object import MovingObject

_GROUND_FILE = "../../assets/ground.png"
_COLOR_KEY = (0, 0, 0)


class Ground(pygame.sprite.Group):
    def __init__(self, ground_position: float):
        super(Ground, self).__init__()

        self.add(GroundPiece(ground_position, 0, 2))
        self.add(GroundPiece(ground_position, 1, 2))

    def update(self, dx: float):
        super(Ground, self).update(dx)


class GroundPiece(MovingObject):
    def __init__(self, ground_position: float, piece: int, pieces: int):
        super(GroundPiece, self).__init__()

        sprite = pygame.image.load(os.path.join(os.path.dirname(__file__), _GROUND_FILE))

        sprite.set_colorkey(_COLOR_KEY)

        w, h = sprite.get_size()

        self.image = sprite.subsurface((piece * w / pieces, 0, w / pieces, h)).convert()

        self.rect = self.image.get_rect()

        self.rect.top = ground_position
        self.rect.left = piece * w / pieces

        self._dw = w

    def _on_out_of_screen(self):
        self._x += self._dw

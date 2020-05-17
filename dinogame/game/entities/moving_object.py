import pygame


class MovingObject(pygame.sprite.Sprite):
    _x: float = None

    def update(self, dx: float):
        if self._x is None:
            self._x = self.rect.x

        self._x -= dx
        self.rect.x = int(self._x)

        if self.rect.right < 0:
            self._on_out_of_screen()

    def _on_out_of_screen(self):
        pass

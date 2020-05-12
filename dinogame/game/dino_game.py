import pygame
from dinogame.callback import Callback
from .status import Status


class DinoGame:
    loop_callback = Callback()
    fail_callback = Callback()

    def __init__(self, fps: int = 60):
        successes, failures = pygame.init()

        self._screen = pygame.display.set_mode((470, 150))
        self._clock = pygame.time.Clock()

        self._fps = fps

    def start(self):
        while True:
            self._loop()

    def get_status(self) -> Status:
        return Status()

    def _loop(self):
        dt = self._clock.tick(self._fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass

        self.loop_callback.on(self.get_status())

        self._screen.fill((255, 255, 255))
        pygame.display.update()

import time

import pygame

from .entities import Decorations, Ground, Player, Obstacles
from ..callback import Callback
from ..tictoc import TicToc


class DinoGame:
    WIDTH = 600
    HEIGHT = 150
    GROUND_POSITION = 120

    is_alive: bool
    is_running: bool

    loop_callback = Callback()
    gameover_callback = Callback()

    def __init__(self, fps: int = 60):
        successes, failures = pygame.init()

        self._screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self._clock = pygame.time.Clock()

        self._font = pygame.font.SysFont("droidsansmononerdfontmono", 13)

        self._fps = fps

        self._tt = TicToc()

        self._starting_time = 0

        self._ground = None
        self._decorations = None
        self._obstacles = None
        self._player = None
        self._entities = None

        self.reset()

    def reset(self) -> None:
        self.is_alive = True
        self.is_running = False

        self._starting_time = 0

        self._ground = Ground(self.GROUND_POSITION)
        self._decorations = Decorations(self.WIDTH, (10, self.GROUND_POSITION - 20), 0.005)
        self._obstacles = Obstacles(self.WIDTH)

        self._player = Player((20, self.GROUND_POSITION + 10))
        self._entities = pygame.sprite.Group(self._player)

    def start(self):
        while True:
            self._loop()

    def _loop(self):
        dt = self._clock.tick(self._fps)

        self._tt.tic()

        self.loop_callback.on(self)

        self._handle_events()

        self._update_state()

        self._check_collision()

        self._draw()

        print("load {}".format(self._tt.toc() * self._fps))

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if not self.is_running:
                    if not self.is_alive:
                        self.reset()
                    self.start_running()
                else:
                    self._player.jump()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                if self.is_running and self.is_alive:
                    self._player.crouch()

            elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                if self.is_running and self.is_alive:
                    self._player.stand_up()

    def _update_state(self):
        if self.is_alive and self.is_running:
            self._ground.update(5)
            self._decorations.update()
            self._obstacles.update(5)
            self._player.update()

    def _check_collision(self):
        if len(pygame.sprite.spritecollide(self._player, self._obstacles, False, pygame.sprite.collide_mask)):
            self._starting_time = self.time_alive

            self.is_alive = False
            self.is_running = False

            self._player.die()

            self.gameover_callback.on(self)

    def _draw(self):
        self._screen.fill((255, 255, 255))

        self._ground.draw(self._screen)
        self._decorations.draw(self._screen)
        self._obstacles.draw(self._screen)
        self._entities.draw(self._screen)

        self._screen.blit(self._font.render("SCORE {0:08d}".format(self.score), True, (0, 0, 0)), (470, 10))

        pygame.display.update()

    def start_running(self) -> None:
        if not self.is_running and self.is_alive:
            self.is_running = True
            self._player.run()

            self._starting_time = time.time()

    @property
    def time_alive(self) -> float:
        return time.time() - self._starting_time if self.is_running else self._starting_time

    @property
    def score(self) -> int:
        return int(self.time_alive * 10)

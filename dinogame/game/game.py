import logging
import math
import random
import time

import numpy as np
import pygame

from .entities import Decorations, Ground, Player, Obstacles, Flyer, Cactus
from ..callback import Callback
from ..tictoc import TicToc

_LOGGER = logging.getLogger(__package__)


class DinoGame:
    WIDTH = 600
    HEIGHT = 150
    GROUND_POSITION = 120

    is_alive: bool
    is_running: bool

    _starting_time: float
    _last_cactus_spawn: float
    _last_flyer_spawn: float

    _ground: Ground
    _decorations: Decorations
    _obstacles: Obstacles
    _player: Player
    _entities: pygame.sprite.Group

    loop_callback = Callback()
    gameover_callback = Callback()

    def __init__(self, fps: int = 60):
        pygame.init()

        pygame.surfarray.use_arraytype("numpy")

        self._screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self._clock = pygame.time.Clock()

        self._font = pygame.font.SysFont("DejaVuSansMono, monospace", 13)

        self._fps = fps

        self._load = 0

        self._tt = TicToc()

        self.reset()

    def reset(self) -> None:
        self.is_alive = True
        self.is_running = False

        self._tt.reset()

        self._starting_time = 0

        self._last_cactus_spawn = 0
        self._last_flyer_spawn = 0

        self._ground = Ground(self.GROUND_POSITION)
        self._decorations = Decorations(self.WIDTH, (10, self.GROUND_POSITION - 20), 0.005)
        self._obstacles = Obstacles(self.WIDTH)

        self._player = Player((20, self.GROUND_POSITION + 10))
        self._entities = pygame.sprite.Group(self._player)

    def start(self):
        while True:
            self._loop()

    def _loop(self):
        self._clock.tick(self._fps)

        self._tt.tic()

        self.loop_callback.on(self)

        self._handle_events()

        if self.is_alive and self.is_running:
            self._update_state()

            self._check_collision()

        self._draw()

        self._load = self._tt.toc() * self._fps

        _LOGGER.debug("load {:0.4f}".format(self.load))

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
        if random.random() < self.cactus_spawn_probability:
            self._obstacles.add(Cactus(self.cactus_max_size))
            self._last_cactus_spawn = self.time_alive

        if random.random() < self.flyer_spawn_probability:
            self._obstacles.add(Flyer())
            self._last_flyer_spawn = self.time_alive

        dx = self.dx

        self._ground.update(dx)
        self._decorations.update()
        self._obstacles.update(dx)
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

    def stand_up(self) -> None:
        self._player.stand_up()

    def jump(self) -> None:
        self._player.jump()

    def crouch(self) -> None:
        self._player.crouch()

    @property
    def load(self) -> float:
        return self._load

    @property
    def time_alive(self) -> float:
        return time.time() - self._starting_time if self.is_running else self._starting_time

    @property
    def score(self) -> int:
        return int(self.time_alive * 10)

    @property
    def speed(self) -> float:
        return 300 + 3 * self.time_alive

    @property
    def dx(self) -> float:
        return self.speed / self._fps

    @property
    def cactus_max_size(self) -> float:
        return 1 - math.exp(- self.time_alive / 15)

    @property
    def cactus_spawn_probability(self) -> float:
        max_speed = 0.10
        exp_speed = 0.01
        spawn_reset = 0.2
        start_delay = -5

        p = max_speed * (1 - math.exp(-exp_speed * (self.time_alive - start_delay))) * (
                1 - math.exp(-spawn_reset * (self.time_alive - self._last_cactus_spawn)))
        return max(0, min(1, p))

    @property
    def flyer_spawn_probability(self) -> float:
        max_speed = 0.02
        exp_speed = 0.01
        spawn_reset = 0.2
        start_delay = 20

        p = max_speed * (1 - math.exp(-exp_speed * (self.time_alive - start_delay))) * (
                1 - math.exp(-spawn_reset * (self.time_alive - self._last_flyer_spawn)))
        return max(0, min(1, p))

    @property
    def frame(self) -> np.array:
        return pygame.surfarray.array3d(self._screen)

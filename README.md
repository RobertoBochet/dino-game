# Dino Game

[![GitHub](https://img.shields.io/github/license/RobertoBochet/dino-game)](https://github.com/RobertoBochet/dino-game/)
[![PyPI](https://img.shields.io/pypi/v/dino-game)](https://pypi.org/project/dino-game/)
[![PyPI - Status](https://img.shields.io/pypi/status/dino-game)](https://pypi.org/project/dino-game/)
[![GitHub last commit](https://img.shields.io/github/last-commit/robertobochet/dino-game)](https://github.com/RobertoBochet/dino-game/)
![gluten free](https://img.shields.io/badge/gluten%20free-100%25-success)

A Python reimplementation of the famous dino game, thought for autonomous control

## Installation

You can install it from [pypi](https://pypi.org/project/dino-game/).

```bash
pip install dino-game
```

## Usage

### Try the game

To try the game without any automation

```bash
python -m dinogame
```

You can use `spacebar` to start running, jump, reset when dino dies, and `key_down` to crouch.

### Library usage

This initializes the game

```python
from dinogame import DinoGame

game = DinoGame()
```

To start the game's loop you can use `play` method

```python
game.play()
```

#### Callbacks

The library provides some callbacks to feed back the game

- `loop_callback`       is called at each new frame
- `gameover_callback`   is called when a gameover occurs

To subscribe to callback you can use callback's `set` method.

The current instance of `DinoGame` is given to the callback as argument.

```python
def lp_cb(game: GameDino):
    # do something

game.loop_callback.set(lp_cb)
```

#### Actions

The following actions are provided as methods:

- `jump`            to jump
- `crouch`          to crouch
- `stand_up`        to stand up
- `start_running`   to start to run
- `reset`           to reset the game

```python
if the_cake_is_ready():
    game.jump()
```

#### Useful properties

`DinoGame` exposes the following useful properties:

- `load`        the current load of the application. If it is more than `1` it is a problem.
- `score`       the current score or that of the last session if the player dies.
- `time_alive`  the lifetime of the player.
- `frame`       the last game frame as `numpy.ndarray`.

```python
if the_game_is_over():
    print("My score is {}".format(game.score))
```

## Credits

This project is realized with the following python's packages:

- [`pygame`](https://pypi.org/project/pygame/)
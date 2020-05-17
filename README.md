# Dino Game

[![PyPI - License](https://img.shields.io/pypi/l/dino-game)](https://pypi.org/project/dino-game/)
[![PyPI](https://img.shields.io/pypi/v/dino-game)](https://pypi.org/project/dino-game/)
[![PyPI - Status](https://img.shields.io/pypi/status/dino-game)](https://pypi.org/project/dino-game/)
![GitHub last commit](https://img.shields.io/github/last-commit/robertobochet/dino-game)
![gluten free](https://img.shields.io/badge/gluten%20free-100%25-success)

A Python reimplementation of the famous dino game, thought for autonomous control

## Installation

You can install it from pypi

```bash
pip install dino-game
```

## Usage

### Try the game

To try the game without any automation

```bash
python -m dinogame
```

You can use `spacebar` to start running, jump, reset when dino die, and `key_down` to crouch.

### Library usage

This initialize the game

```python
from dinogame import DinoGame

game = DinoGame()
```

To start the game's loop you can use `play` method

```python
game.play()
```

#### Callback

The library provide some callback to feedback the game

- `loop_callback` is called each frame
- `gameover_callback` is called when a gameover occurs

To subscribe to callback you can use callback's `set` method. To the callbacks are given the current instance of `DinoGame` as argument.

```python
def lp_cb(game: GameDino):
    # do something

game.loop_callback.set(lp_cb)
```

## Credits

This project is realized with the following python's packages:

- `pygame`
- `numpy`
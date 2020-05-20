#!/usr/bin/env python3
import logging

from dinogame import DinoGame

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    #logging.getLogger("dinogame.game").setLevel(logging.WARNING)

    game = DinoGame(fps=60)

    game.start()

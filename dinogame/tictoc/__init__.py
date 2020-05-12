import time


class TicToc:
    _tic: float = 0
    _toc: float = 0
    _dt: float = 0

    def tic(self):
        self._tic = time.time()

    def toc(self):
        self._toc = time.time()
        self._dt = self._toc - self._tic
        return self._dt

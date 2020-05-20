import time


class TicToc:
    _tic: float = 0
    _toc: float = 0
    _dt: float = 0

    def tic(self):
        self._tic = time.time()

    def toc(self):
        if self._tic == 0:
            return 0

        self._toc = time.time()
        self._dt = self._toc - self._tic
        return self._dt

    def reset(self):
        self._tic = 0
        self._toc = 0
        self._dt = 0

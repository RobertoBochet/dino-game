from typing import Callable


class Callback:
    def __init__(self):
        self._callback = None

    def set(self, callback: Callable) -> None:
        self._callback = callback

    def on(self, *args, **kwargs) -> None:
        if self._callback is None:
            return

        self._callback(*args, **kwargs)

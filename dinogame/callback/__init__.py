class Callback:
    def __init__(self):
        self._callback = None

    def set(self, value):
        self._callback = value

    def on(self, *args, **kwargs):
        if self._callback is None:
            return

        self._callback(*args, **kwargs)

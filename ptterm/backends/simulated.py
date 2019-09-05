"""Module implementing a "Fake Terminal" Backend, which can be used to display
    any custom text, in the same format as a regular Terminal.

Trying to aim for the same level of compatibility as the rest of the library,
    but cannot guarantee it.
"""

from .base import Terminal


class SimTerminal(Terminal):
    def __init__(self):
        self.instream = ""

        self.name = "Simulated Terminal"
        self.size = 80, 25

        self._closed = False
        self._input_ready_callbacks = []
        self._reader_connected = False

    def add_input_ready_callback(self, callback):
        self._input_ready_callbacks.append(callback)

    def kill(self):
        pass

    @property
    def closed(self):
        return self._closed

    def read_text(self, amount=1024):
        full = self.instream[:amount]
        c = len(full)
        self.instream = self.instream[c:]
        return full

    def write_text(self, *text):
        for line in text:
            self.instream += line

    def ready(self):
        for cb in self._input_ready_callbacks:
            cb()

    def connect_reader(self):
        # if self.master is not None and not self._reader_connected:
        #     self.loop.add_reader(self.master, self.ready)
        #     self._reader_connected = True
        pass

    def disconnect_reader(self):
        # if self.master is not None and self._reader_connected:
        #     self.loop.remove_reader(self.master)
        #     self._reader_connected = False
        pass

    def set_size(self, width, height):
        assert isinstance(width, int)
        assert isinstance(height, int)

        self.size = width, height

    def start(self):
        pass

    def get_name(self):
        return self.name

    def get_cwd(self):
        return "/"

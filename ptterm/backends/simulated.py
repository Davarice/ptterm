"""Module implementing a "Fake Terminal" Backend, which can be used to display
    any custom text, in the same format as a regular Terminal.

Trying to aim for the same level of compatibility as the rest of the library,
    but cannot guarantee it.
"""

from .base import Terminal


class SimTerminal(Terminal):
    def __init__(self):
        raise NotImplementedError

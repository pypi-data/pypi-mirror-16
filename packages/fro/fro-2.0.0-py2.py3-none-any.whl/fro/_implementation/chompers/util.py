from fro._implementation.chompers import abstract
from fro._implementation.chompers.box import Box


class ChainChomper(abstract.AbstractChomper):
    def __init__(self, func, significant=True, name=None):
        abstract.AbstractChomper.__init__(self, significant=significant, name=name)
        self._generation_func = func
        self._chomper = None

    def _chomp(self, state, tracker):
        if self._chomper is None:
            lazier = ChainChomper(self._generation_func, significant=self._significant, name=self._name)
            self._chomper = self._generation_func(lazier)
        return self._chomper.chomp(state, tracker)


class OptionalChomper(abstract.AbstractChomper):
    def __init__(self, child, default=None, significant=True, name=None):
        abstract.AbstractChomper.__init__(self, significant, name)
        self._child = child
        self._default = default

    def _chomp(self, state, tracker):
        line = state.line()
        col = state.column()
        box = self._child.chomp(state, tracker)
        if box is not None:
            return box
        elif state.line() != line:
            self._failed_lookahead(state, tracker)
        state.reset_to(col)
        return Box(self._default)


class StubChomper(abstract.AbstractChomper):
    def __init__(self, significant=True, name=None):
        abstract.AbstractChomper.__init__(self, significant, name)
        self._delegate = None

    def set_delegate(self, delegate):
        if self._delegate is not None:
            raise AssertionError("Cannot set a stub's delegate twice")
        self._delegate = delegate

    def _chomp(self, state, tracker):
        if self._delegate is None:
            raise ValueError("Stub chomper has no delegate")
        return self._delegate.chomp(state, tracker)


class ThunkChomper(abstract.AbstractChomper):
    def __init__(self, thunk, significant=True, name=None):
        abstract.AbstractChomper.__init__(self, significant=significant, name=name)
        self._thunk = thunk

    def _chomp(self, state, tracker):
        return self._thunk().chomp(state, tracker)

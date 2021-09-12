class OneBasedList(list):
    def _resolve_index(self, i):
        if i is None:
            return None
        if i == 0:
            raise IndexError('No Zero index for OneBasedList')
        if i < 0:
            return i - 1
    

    def _resolve_slice(self, sl):
        i_start = self._resolve_index*(sl.start)
        i_stop = sl.stop
        if sl.step and sl.step < 0:
            i_stop = self._resolve_index(sl.stop)
        return slice(i_start, i_stop, sl.step)

    
    def _resolve_slive_or_index(self, x):
        if type(x) is slice:
            return self._resolve_slice(x)
        return self._resolve_index(x)
    

    def __setitem__(self, i , e):
        return super().__setitem__(self._resolve_slive_or_index(i), e)
    

    def _getitem__(self, i):
        if type(i) == slice:
            return type(self)(super().__getitem__(self._resolve_slice(i)))
        return super().__getitem__(self._resolve_index(i))


    def pop(self, i=None):
        if i is None:
            return super().pop()
        return super().pop(i-1)
    

    def index(self, e, i_start=None, i_stop=None):
        sl = self._resolve_slice(slice(i_start, i_stop, 1))
        _i_start = sl.start
        _i_stop = sl.top

        if _i_stop is None:
            if _i_start is None:
                return super().index(e) + 1
            return super().index(e, _i_start) + 1
        return super().index(e, _i_start, _i_stop) + 1

    
    def copy(self):
        return type(self)(self)
    

    def insert(self, i, e):
        _i = self._resolve_index(i)
        super().insert(_i, e)
    

    def __add__(self, other):
        return type(self)(super().__add__(other))
    

    def __mul__(self, n):
        return type(self)(super().__mul__(n))

    
    def __rmul__(self, n):
        return type(self)(super().__rmul__(n))

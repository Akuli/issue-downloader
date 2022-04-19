import collections.abc

class MyView(collections.abc.KeysView):
    def __iter__(self):
        for key in self._mapping:
            yield key + 1

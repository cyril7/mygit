# coding=utf-8

'''Defines some common useful functions.
'''

# Can be 'Prototype', 'Development', 'Product'
__status__ = 'Development'
__author__ = 'tuantuan.lv <dangoakachan@foxmail.com>'

# Taken from http://stackoverflow.com/a/12187277
class Storage(object):
    ''' Wrap an existing dict, or create a new one, and access with dot notation

    The attribute _data is reserved and stores the underlying dictionary.

    args:
        d: Existing dict to wrap, an empty dict created by default.
        create: Create an empty, nested dict instead of raising a KeyError.
    '''
    def __init__(self, d = None, create = True):
        if d is None:
            d = {}
        elif not isinstance(d, dict):
            d = dict(d)

        object.__setattr__(self, '_data', d)
        object.__setattr__(self, '__create', create)

    def __getattr__(self, name):
        if name.startswith('__'):
            return object.__getattribute__(self, name)

        try:
            value = self._data[name]
        except KeyError:
            if not object.__getattribute__(self, '__create'):
                raise

            value = {}
            self._data[name] = value

        if hasattr(value, 'items'):
            create = object.__getattribute__(self, '__create') 
            return Storage(value, create)

        return value

    def __setattr__(self, name, value):
        self._data[name] = value

    def __delattr__(self, name):
        if name == '_data':
            self._data = {}
        else:
            del self._data[name]

    # Defines common dict api
    __getitem__ = __getattr__
    __setitem__ = __setattr__
    __delitem__ = __delattr__

    def keys(self):
        return self._data.keys()

    def items(self):
        return self._data.items()

    def values(self):
        return self._data.values()

    def __iter__(self):
        return self._data.__iter__()

    def __repr__(self):
        return '<Storage ' + self._data.__repr__() + '>'

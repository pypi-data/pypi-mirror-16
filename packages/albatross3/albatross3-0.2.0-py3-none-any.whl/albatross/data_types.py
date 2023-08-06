from albatross.http_error import HTTPError
from albatross.status_codes import HTTP_400


def caseless_pairs(seq):
    for k, v in seq:
        yield k.lower(), v


class Immutable:
    def __setitem__(self, k, v):
        raise TypeError('Cannot set item on %s' % self.__class__)

    def update(self, E=None, **F):
        raise TypeError('Cannot update on %s' % self.__class__)


class ImmutableMultiDict(Immutable, dict):
    def __getitem__(self, k):
        if k in self:
            return super(ImmutableMultiDict, self).__getitem__(k)[0]
        raise HTTPError(HTTP_400, 'Must provide parameter \'%s\'.' % k)

    def get(self, k, d=None):
        if k in self:
            return super(ImmutableMultiDict, self).__getitem__(k)[0]
        return d

    def get_all(self, k, d=None):
        if k in self:
            return super(ImmutableMultiDict, self).__getitem__(k)
        return d


class CaselessDict(dict):
    def __init__(self, *args, **kwargs):
        if args:
            args = caseless_pairs(args)
        if kwargs:
            kwargs = {k.lower(): v for k, v in kwargs.items()}
        super(CaselessDict, self).__init__(args, **kwargs)

    def __getitem__(self, k):
        k = k.lower()
        return super(CaselessDict, self).__getitem__(k)

    def __iter__(self):
        for k, v in iter(self):
            yield k.lower(), v

    def __setitem__(self, k, v):
        super(CaselessDict, self).__setitem__(k.lower(), v)

    def get(self, k, d=None):
        k = k.lower()
        if k in self:
            return super(CaselessDict, self).__getitem__(k)
        return d

    def update(self, other=None, **kwargs):
        updates = {k.lower(): v for k, v in kwargs.items()}
        if other:
            updates.update(caseless_pairs(other))
        return super(CaselessDict, self).update(updates)


class ImmutableCaselessDict(Immutable, CaselessDict):
    pass

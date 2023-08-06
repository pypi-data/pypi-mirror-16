# -*- coding: utf-8 -*-

from collections import OrderedDict, MutableMapping, Mapping

class CaseInsensitiveDict(MutableMapping):
    """
    A case-insensitive ``dict``-like object.

    Implements all methods and operations of
    ``MutableMapping`` as well as dict's ``copy``. Also
    provides ``lower_items``.

    All keys are expected to be strings. The structure remembers the
    case of the last key to be set, and ``iter(instance)``,
    ``keys()``, ``items()``, ``iterkeys()``, and ``iteritems()``
    will contain case-sensitive keys. However, querying and contains
    testing is case insensitive::

        cid = CaseInsensitiveDict()
        cid['Accept'] = 'application/json'
        cid['aCCEPT'] == 'application/json'  # True
        list(cid) == ['Accept']  # True

    For example, ``headers['content-encoding']`` will return the
    value of a ``'Content-Encoding'`` response header, regardless
    of how the header name was originally stored.

    If the constructor, ``.update``, or equality comparison
    operations are given keys that have equal ``.lower()``s, the
    behavior is undefined.

    """
    def __init__(self, data=None, **kwargs):
        self._d = OrderedDict()
        if data is None:
            data = {}
        self.update(data, **kwargs)

    def __repr__(self):
        return str(dict(self.items()))

    def __setitem__(self, key, value):
        # Use the lowercased key for lookups, but store the actual
        # key alongside the value.
        self._d[key.lower()] = (key, value)

    def __getitem__(self, key):
        return self._d[key.lower()][1]

    def __delitem__(self, key):
        del self._d[key.lower()]

    def __iter__(self):
        return (k for k, v in self._d.values())

    def __len__(self):
        return len(self._d)

    def __eq__(self, other):
        if isinstance(other, Mapping):
            other = CaseInsensitiveDict(other)
        else:
            return NotImplemented
        # Compare insensitively
        return dict(self.lower_items()) == dict(other.lower_items())

    # Copy is required
    def copy(self):
        return CaseInsensitiveDict(self._d.values())

    def lower_items(self):
        """
        Like iteritems(), but with all lowercase keys
        """
        return ((k, v[1]) for (k, v) in self._d.items())


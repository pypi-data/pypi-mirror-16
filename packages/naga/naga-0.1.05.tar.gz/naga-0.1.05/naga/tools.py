import itertools
import types
from functools import reduce, partial

seq_types = list, tuple, str


def rreduce(fn, seq, default=None):
    """'readable reduce' - More readable version of reduce with arrity-based dispatch; passes keyword arguments
    to functools.reduce"""

    # if two arguments
    if default is None:
        return reduce(fn, seq)

    # if three arguments
    return reduce(fn, seq, default)


def get_in(d, ks, not_found=None):
    return reduce(lambda x, y: x.get(y, {}), ks, d) or not_found


def apply(fn, x):
    return fn(*x)


def first(iterable):
    return next(iter(iterable))


def dec(n):
    return n - 1


def inc(n):
    return n + 1


def nth(seq, idx):
    return first(compose([rest] * dec(idx), iter(seq)))


def second(seq): return nth(seq, 2)


def third(seq): return nth(seq, 3)


def fourth(seq): return nth(seq, 4)


def fifth(seq): return nth(seq, 5)


def sixth(seq): return nth(seq, 6)


def seventh(seq): return nth(seq, 7)


def eigth(seq): return nth(seq, 8)


def ninth(seq): return nth(seq, 9)


def tenth(seq): return nth(seq, 10)


def compose(fns, x):
    return rreduce(fn=lambda a, b: b(a),
                   seq=fns,
                   default=x)


def last(iterable):
    a, b = itertools.tee(iterable)
    iter_len = reduce(lambda n, x: n + 1, enumerate(b), 0)
    return next(itertools.islice(a, iter_len - 1, iter_len))


def rest(iterable):
    return itertools.islice(iterable, 1, None)


def iterate(fn, x):
    val = x
    while True:
        yield val
        val = fn(x)


def take(n, seq):
    _seq = iter(seq)
    return rreduce(fn=lambda lst, _: lst + [next(_seq)],
                   seq=range(n),
                   default=[])


def explode(*ds):
    return itertools.chain(*map(lambda d: d.items(), ds))


def merge(*seqs):
    if isinstance(seqs[0], seq_types):
        return conj(*seqs)

    return dict(rreduce(fn=lambda l, _: apply(lambda k, v: l + [(k, v)], _),
                        seq=explode(*seqs),
                        default=[]))


def assoc(m, k, v):
    str_ = seq_types
    if isinstance(m, str_):
        return append(m[:k] + [v] + m[k + 1:])
    return merge(m, {k: v})


def dissoc(d, *ks):
    return keyfilter(lambda x: x not in ks, d)


def merge_with(fn, *ds):
    return rreduce(fn=lambda d, x: apply(lambda k, v:
                                         assoc(d, k, fn(d[k], v)) if k in d else
                                         assoc(d, k, v), x),
                   seq=explode(*ds),
                   default={})


def merge_with_default(fn, default=None, *dicts):
    _fn, _default = fn, default
    return merge_with(_fn, rreduce(fn=lambda d, _: apply(lambda k, v: assoc(d, k, _default), _),
                                   seq=explode(*dicts),
                                   default={}),
                      *dicts)


class LazySeq(object):
    def __init__(self, seq):
        self.seq = iter(seq)
        self.cache = {}
        self.idx = -1

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            return self.__getslice__(idx.start, idx.stop, idx.step)

        elif idx in self.cache:
            return self.cache[idx]
        else:
            while self.idx < idx:
                self.cache[self.idx + 1] = next(self.seq)
                self.idx += 1
            return self[idx]

    def __iter__(self):
        idx = 0
        while True:
            try:
                yield self[idx]
                idx += 1
            except StopIteration:
                raise StopIteration

    def __add__(self, other):
        return LazySeq(itertools.chain(self, other))

    def __eq__(self, other):
        return id(self) == id(other)

    def __getslice__(self, start, stop=None, step=None):
        if not stop:
            stop = start
            return list(itertools.islice(self, stop))
        else:
            return list(itertools.islice(self, start, stop, step))

    def append(self, item):
        return self + [item]

    def __contains__(self, item):
        return item in list(self)

    def __reversed__(self):
        return reversed(list(self))

    def __rmul__(self, other):
        return list(self) * other

    def __setitem__(self, idx, value):
        return list(self).__setitem__(idx, value)

    def __setslice__(self, i, j, sequence):
        return list(self).__setslice__(i, j, sequence)

    def __str__(self):
        return 'LazySequence({})'.format(repr(self.seq))

    def __repr__(self):
        return self.__str__()

    def count(self, item):
        return list(self).count(item)

    def extend(self, other):
        return self + other

    def index(self, item):

        for n, _item in enumerate(self):
            if item == _item:
                return n

    def insert(self, idx, item):
        base_list = list(self)
        return base_list[:idx] + [item] + [base_list[idx + 1:]]

    def pop(self, idx=None):
        base_list = list(self)
        if idx is None:
            return base_list[:-1]
        return base_list[:idx] + base_list[idx + 1:]


        #  'index',
        #  'insert',
        #  'pop',
        #  'remove',
        #  'reverse',
        #  'sort']


def assoc_in(d, key_list, val):
    d1 = keys2dict(val, *key_list)
    return recursive_dict_merge(d, d1)


def terminal_dict(*ds):
    return not (are_dicts(*ds) and all(map(lambda x: are_dicts(*x.values()), ds)))


def terminal_dicts(*ds):
    return all(map(terminal_dict, ds))


def update_in(d, key_list, v):
    d1 = keys2dict(v, *key_list)
    return merge_with(lambda a, b: recursive_dict_merge(a, b) if not are_dicts(a, b) else b, d, d1)


def recursive_dict_merge(*ds):
    return merge_with(lambda a, b: recursive_dict_merge(a, b) if not terminal_dicts(a, b) else merge(a, b), *ds)


def keys2dict(val, *ks):
    v_in = reduce(lambda x, y: {y: x}, (list(ks) + [val])[::-1])
    return v_in


def are_instances(items, types):
    return all(map(lambda x: isinstance(x, types), items))


def are_dicts(*ds):
    return are_instances(ds, dict)


def supassoc_in(d, val, k, *ks):
    return merge_with(lambda x, y: merge(x, y) if are_dicts(x.values() + y.values()) else x.values() + y.values(), d,
                      reduce(lambda x, y: {y: x}, ([k] + list(ks) + [val])[::-1]))


def keyfilter(fn, d):
    return reduce(lambda _d, _: apply(lambda k, v: assoc(_d, k, v) if fn(k) else _d, _), d.items(), {})


def valfilter(fn, d):
    return reduce(lambda _d, _: apply(lambda k, v: assoc(_d, k, v) if fn(v) else _d, _), d.items(), {})


def itemfilter(fn, d):
    return reduce(lambda _d, _: apply(lambda k, v: assoc(_d, k, v) if fn(k, v) else _d, _), d.items(), {})


def valmap(fn, d):
    return rreduce(fn=lambda _d, _: apply(lambda k, v: assoc(_d, k, fn(v)), _),
                   seq=d.items(),
                   default={})


def keymap(fn, d):
    return rreduce(fn=lambda _d, _: apply(lambda k, v: assoc(_d, fn(k), v), _),
                   seq=d.items(),
                   default={})


def itemmap(fn, d):
    return rreduce(fn=lambda _d, _: apply(lambda k, v: assoc(_d, *fn(k, v)), _),
                   seq=d.items(),
                   default={})


def nary(fn):
    def _nary(*x):
        if len(x) == 2:
            return fn(*x)
        if len(x) == 1:
            return fn(first(x))
        else:
            return fn(first(x), _nary(*rest(x)))

    return _nary


def append(*seqs):
    return rreduce(fn=lambda x, y: x + y,
                   seq=seqs)


def windows(n, seq):
    return rreduce(
        fn=lambda groups, nxt: (append(groups[:-1],
                                       [append(groups[-1], [nxt])]) if (groups and len(groups[-1]) < n) else
                                append(groups, [[nxt]]) if groups
                                else [[nxt]]),
        seq=seq,
        default=[])


def conj(seq, *items):
    return append(seq, items)


def main():
    g = LazySeq((x for x in range(10)))
    print(g[0])
    print(g[3])
    print(g.pop(5))
    print(g[3:5])
    # print(len(g))
    print(list(g))
    print(list(g))

    print(second(g))
    print(next(iter(g)))
    g2 = g + g

    print(next(iterate(inc, 1)))

    print(take(5, g))
    print(tenth(g))
    # print(list(g2))
    # print(list(g))


if __name__ == '__main__':
    main()

def memory(n):
    def asshole(f):
        nonlocal n
        n = f(n)
        return n
    return asshole
    
def mystery(p, q):
    p[1].extend([q])
    q.append(p[1:])

def group_by(s, fn):
    grouped = {}
    for e in s:
        key = fn(e)
        if key in grouped:
            grouped[key] += [e]
        else:
            grouped[key] = [e]
    return grouped

def add_this_many(x, el, s):
    n = 0
    for i in s:
        if i == x:
            n += 1
    this_many = n * [el]
    s.extend(this_many)

def filter(iterable, fn):
    yield from [i for i in iterable if fn(i)]

def merge(a, b):
    first_a, first_b = next(a), next(b)
    if first_a == first_b:
        yield first_a
        first_a, first_b = next(a), next(b)
    elif first_a < first_b:
        yield first_a
        first_a = next(a)
    else:
        yield first_b
        first_a = next(b)
    
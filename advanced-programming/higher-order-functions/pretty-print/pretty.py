"""
[1, 2, 3, ['a', 'b', ['c'], "foo"], 4]
"""

def fmt(lst, depth=1):
    parts = []
    for x in lst:
        if type(x) is type([]):
            parts.append(fmt(x, depth + 1))
        else:
            parts.append(repr(x))
    return '[' + (',\n' + ' ' * depth).join(parts) + ']'


if __name__ == '__main__':
    print(fmt([1, ['a', 'b', 'c', ['foo', 'bar']], 2, 3, []]))

    assert fmt([]) == '[]'
    assert fmt([1, 2, 3]) == '[1,\n 2,\n 3]'
    assert fmt([1, ['a', 'b']]) == "[1,\n ['a',\n 'b']]"

    print("ok")

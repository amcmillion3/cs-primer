"""
Implement the following functions, using recursion.

If you find it easier to use iteration, do that first! Then, rewrite it recursively :)

If the recursive approach seems obvious, try to also write it iteratively. Seeing
the connection between the two is highly worthwhile.

This is just for practice. In reality, most or all of these would be solved well enough
or better with iteration. But by getting some extra reps on easier problems, we'll
be better prepared for harder problems where recursion is a good fit.
"""


def factorial(n):
    """
    Calculate the product of the first n integers

    >>> factorial(3)  # 1 * 2 * 3
    6
    >>> factorial(10)  # 1 * 2 * ... * 10
    3628800
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def palindrome(letters):
    """
    Determine if the given phrase is a palindrome. As a stretch goal, support phrases
    such as "A man, a plan, a canal — Panama!"

    >>> palindrome("racecar")
    True

    >>> palindrome("hello")
    False

    >>> palindrome("A man, a plan, a canal - Panama!")
    True

    """
    s = "".join(filter(str.isalnum, letters)).lower()
    if len(s) <= 1:
        return True
    
    return s[0] == s[-1] and palindrome(s[1:-1])



def gcd(a, b):
    """
    Determine the greatest common divisor of two integers a and b. One approach is
    described in Euclid's Elements roughly as:

    - Repeatedly subtract the smaller number from the larger one, until no longer possible
    - If the remainder is zero, then the smaller number must be the GCD
    - Otherwise, repeat the process, using the number you were subtracting as the new "larger"
        number, and the remainder as the new "smaller" number

    For example if a = 1071 and b = 462 (taken from Wikipedia):

    - Subtracting 462 twice from 1071 leaves a remainder of 147
    - Subtracting 147 three times from 462 leaves a remainder of 21
    - Subtracting 21 seven ties from 147 leaves a remainder of 0

    So, 21 divides both 147 and 462, and is the greatest number to do this.

    >>> gcd(1071, 462)
    21

    >>> gcd(15, 9)
    3

    >>> gcd(9, 15)
    3

    >>> gcd(3, 5)
    1
    """
    if a < b:
        return gcd(b, a)

    rem = a % b
    if rem == 0:
        return b
    else:
        return gcd(b, rem)
         

def filter_recursive(f, xs):
    """
    Given a predicate function f (a function which returns True or False) and a list
    xs, return a new list with only the items of xs where f(x) is True.

    Below is an iterative approach. See if you can convert it to recursive, for practice.

    def filter_iter(f, xs):
        out = []
        for x in xs:
            if f(x):
                out.append(x)
        return out

    >>> filter_recursive(lambda x: x > 0, [-1, 3, -2, 5])
    [3, 5]
    >>> filter_recursive(lambda x: False, [1, 2])
    []
    """
    if len(xs) == 0:
        return []
    sub = filter_recursive(f, xs[:-1])
    final_x = xs[-1]
    if f(final_x):
        sub.append(final_x)
    return sub


def reduce(f, xs, init=None):
    """
    Apply the function f cumulatively to the items of xs, reducing to a single value.

    If initializer is provided, use it as the first value. Otherwise, use only the
    values in xs.

    Below is an iterative approach. See if you can convert it to recursive, for practice.

    def reduce_iter(f, xs, init=None):
        xs = iter(xs)
        out = next(xs) if init is None else init
        for x in xs:
            out = f(out, x)
        return out

    >>> reduce(lambda acc, x: acc + x, [1, 2, 3, 4])
    10
    >>> def mirror(d, x):
    ...     d[x] = x
    ...     return d
    >>> reduce(mirror, ['foo', 'bar'], {})
    {'foo': 'foo', 'bar': 'bar'}
    """
    def inner(f, xs, acc):
        if len(xs) == 0:
            return acc
        return inner(f ,xs[1:], f(acc, xs[0]))

    if init is None:
        return inner(f, xs[1:], xs[0])
    return inner(f, xs, init)


def rabbit_pairs(n):
    """
    A newly born breeding pair of rabbits are placed in a field. At the age of one month,
    the pair produces another breeding pair of rabbits. All pairs will breed every month,
    and somehow never die. How many pairs will exist at month n?

    >>> rabbit_pairs(1)
    1

    >>> rabbit_pairs(2)  # first pair have mated, but not yet had babies
    1

    >>> rabbit_pairs(3)  # first babies are born, but not yet mated
    2

    >>> rabbit_pairs(4)  # original pair have another pair, so 1 is added to existing population of 2
    3

    >>> rabbit_pairs(5)  # two pairs have had babies, so 2 is added to existing population of 3
    5

    >>> rabbit_pairs(6)  # three pairs have babies, so 3 is added to existing population of 5
    8

    >>> rabbit_pairs(20)
    6765
    """
    if n <= 2:
        return 1
    return rabbit_pairs(n - 1) + rabbit_pairs(n - 2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print('ok')

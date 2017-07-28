import functools
import operator
import sys

import math

prod = functools.partial(functools.reduce, operator.mul)


def permutations(n, r):
    return math.factorial(n) // math.factorial(n - r)


@functools.lru_cache(maxsize=2 ** 8)
def PT(*t):
    if sum(t) != 10:
        return 0
    return math.factorial(10) / prod(math.factorial(ti) for ti in t) * (1 / 6) ** 10


def main():
    h = {(10, 0, 0, 0, 0, 0): permutations(6, 1),
         (9, 1, 0, 0, 0, 0): permutations(6, 2),
         (8, 2, 0, 0, 0, 0): permutations(6, 2),
         (8, 1, 1, 0, 0, 0): permutations(6, 3) // math.factorial(2),
         (7, 3, 0, 0, 0, 0): permutations(6, 2),
         (6, 4, 0, 0, 0, 0): permutations(6, 2),
         (5, 5, 0, 0, 0, 0): permutations(6, 2) // math.factorial(2),
         (7, 2, 1, 0, 0, 0): permutations(6, 3),
         (7, 1, 1, 1, 0, 0): permutations(6, 4) // math.factorial(3),
         (6, 3, 1, 0, 0, 0): permutations(6, 3),
         (5, 4, 1, 0, 0, 0): permutations(6, 3),
         (6, 2, 2, 0, 0, 0): permutations(6, 3) // math.factorial(2),
         (5, 3, 2, 0, 0, 0): permutations(6, 3),
         (6, 2, 1, 1, 0, 0): permutations(6, 4) // math.factorial(2),
         (4, 4, 2, 0, 0, 0): permutations(6, 3) // math.factorial(2),
         (4, 3, 3, 0, 0, 0): permutations(6, 3) // math.factorial(2),
         (5, 3, 1, 1, 0, 0): permutations(6, 4) // math.factorial(2),
         (6, 1, 1, 1, 1, 0): permutations(6, 5) // math.factorial(4),
         (4, 4, 1, 1, 0, 0): permutations(6, 4) // math.factorial(2) // math.factorial(2),
         (5, 2, 2, 1, 0, 0): permutations(6, 4) // math.factorial(2),
         (4, 3, 2, 1, 0, 0): permutations(6, 4),
         (5, 2, 1, 1, 1, 0): permutations(6, 5) // math.factorial(3),
         (3, 3, 3, 1, 0, 0): permutations(6, 4) // math.factorial(3),
         (4, 2, 2, 2, 0, 0): permutations(6, 4) // math.factorial(3),
         (3, 3, 2, 2, 0, 0): permutations(6, 4) // math.factorial(2) // math.factorial(2),
         (4, 3, 1, 1, 1, 0): permutations(6, 5) // math.factorial(3),
         (5, 1, 1, 1, 1, 1): permutations(6, 6) // math.factorial(5),
         (4, 2, 2, 1, 1, 0): permutations(6, 5) // math.factorial(2) // math.factorial(2),
         (3, 3, 2, 1, 1, 0): permutations(6, 5) // math.factorial(2) // math.factorial(2),
         (3, 2, 2, 2, 1, 0): permutations(6, 5) // math.factorial(3),
         (4, 2, 1, 1, 1, 1): permutations(6, 6) // math.factorial(4),
         (3, 3, 1, 1, 1, 1): permutations(6, 6) // math.factorial(2) // math.factorial(4),
         (2, 2, 2, 2, 2, 0): permutations(6, 5) // math.factorial(5),
         (3, 2, 2, 1, 1, 1): permutations(6, 6) // math.factorial(2) // math.factorial(3),
         (2, 2, 2, 2, 1, 1): permutations(6, 6) // math.factorial(4) // math.factorial(2),
         (2, 2, 2, 2, 2, 1): math.inf}

    H1 = 0
    for t, count in h.items():
        if PT(*t) != 0:
            H1 -= count * PT(*t) * math.log2(PT(*t))

    print(H1)

    return 0


if __name__ == '__main__':
    sys.exit(main())

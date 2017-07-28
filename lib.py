import functools
import math
import operator
import itertools
import copy

import numpy as np

prod = functools.partial(functools.reduce, operator.mul)


def permutations(n, r):
    """
    順列の数 nPr を返す
    """
    return math.factorial(n) // math.factorial(n - r)


def combinations(n, r):
    """
    組み合わせの数 nCr を返す
    """
    return permutations(n, r) / math.factorial(r)


def D(X):
    """
    確率変数 X の実現値の集合を返す
    """
    return X.keys()


def P(v, X):
    """
    確率変数 X が X = v となる確率を返す
    """
    return X[v]


def H1(X):
    """
    確率変数 X の一次エントロピーを求める

    >>> X = { 0: 1/8, 1: 3/8, 2: 3/8, 3: 1/8 }
    >>> H1(X)
    1.811278124459133
    """
    assert abs(sum(X) - 1.0) < 1e-9
    return -sum(P(v, X) * math.log2(P(v, X)) if P(v, X) != 0 else 0 for v in D(X))


def H(*P):
    """
    一次エントロピーを求める関数の簡易版

    >>> H(1/8, 2/8, 1/8, 1/8, 2/8, 1/8)
    2.5
    """
    assert abs(sum(P) - 1.0) < 1e-9
    return -sum(p * math.log2(p) if p != 0 else 0 for p in P)


def w(x):
    """
    ハミング重みを求める

    >>> w(0b110)
    2
    """
    return bin(x).count('1')


def d(x, y):
    """
    ハミング距離を求める

    >>> d(0b110, 0b001)
    3
    """
    return w(x ^ y)


def d_min(*X):
    """
    最小ハミング距離を求める

    >>> d_min(0b110, 0b011, 0b101)
    2
    """
    return min(d(x, y) for x, y in itertools.combinations(X, 2))


def solve(A, b):
    """
    連立方程式 Ax = b を解く

    >>> A = np.array([[0.1, -0.4], [1.0, 1.0]])
    >>> b = np.array([0.0, 1.0])
    >>> solve(A, b)
    array([ 0.8,  0.2])
    """
    return np.linalg.solve(A, b)


def huffman(X, Σ={'0', '1'}):
    """
    Huffman 符号を生成する

    >>> X = { 'A': 1/4, 'B': 1/8, 'C': 1/8, 'D': 1/8, 'E': 1/4, 'F': 1/8 }
    >>> huffman(X)
    { 'A': '00', 'B': '100', 'C': '101', 'D': '110', 'E': '01', 'F': '111' }
    """
    codes = dict.fromkeys(X, str())
    probs = copy.deepcopy(X)
    while True:
        if len(probs) == 1:
            break
        targets = sorted(probs.keys(), key=lambda v: probs[v])[:len(Σ)]
        p = 0.0
        for target, c in zip(targets, Σ):
            for s in target:
                codes[s] = c + codes[s]
            p += probs[target]
            del probs[target]
        probs[''.join(targets)] = p

    return codes


def L(C, X):
    """
    平均符号長を返す

    >>> X = { 'A': 1/4, 'B': 1/8, 'C': 1/8, 'D': 1/8, 'E': 1/4, 'F': 1/8 }
    >>> C = huffman(X)
    >>> L(C, X)
    2.5
    """
    return sum(len(C[key]) * X[key] for key in C.keys())

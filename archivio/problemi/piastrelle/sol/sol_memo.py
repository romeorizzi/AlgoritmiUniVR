#!/usr/bin/env python3
from sys import stderr, setrecursionlimit
from functools import lru_cache

setrecursionlimit(10**9) # good enough for n up to 10.000

@lru_cache(maxsize=None)
def f(n):
    """returns the number of tilings for a 1xn-grid with 1x1 ad 1x2 tiles."""
    #print(f"function f called with argument {n=}", file=stderr)
    assert n >= 0
    if n <= 1:
        return 1
    return f(n-1) + f(n-2)

def rank(T, n):
    """returns the rank of tiling T among the tilings of the 1xn-grid."""
    #print(f"function rank called with arguments {T=}, {n=}", file=stderr)
    assert n >= 0
    if n <= 1:
        return 0
    if T[1] == "]":
        return rank(T[2:], n-1)
    return rank(T[4:], n-2) + f(n-1)    

def unrank(n, rank):
    #print(f"function unrank called with arguments {n=}, {rank=}", file=stderr)
    assert n >= 0
    if n == 0:
        return ""
    if rank < f(n-1):
        return "[]" + unrank(n-1, rank)
    return "[--]" + unrank(n-2, rank-f(n-1))



if __name__ == "__main__":
    T = int(input())
    for t in range(1, 1+T):
        print(f"#\n# Testcase {t}:", file=stderr)
        n, c, r, u = map(int, input().strip().split())
        assert 0 <= c <= 1
        if c == 1:
            print(f(n))
            #print(f(n), file=stderr)
        for i in range(r):
            T = input().strip()
            print(rank(T, n))
            #print(rank(T, n), file=stderr)
        for i in range(u):
            rnk = int(input())
            print(unrank(n, rnk))
            #print(unrank(n, rnk), file=stderr)

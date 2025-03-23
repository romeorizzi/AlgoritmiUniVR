#!/usr/bin/env python3
from sys import stderr,stdout, argv


def f(n):
    assert(n >= 0)
    if n <= 1:
        return 1
    return f(n-1) + f(n-2)


def f2(n):
    return -1
    assert(n >= 0)
    if n == 0:
        return 1
    if n == 1:
        return 2
    ans = f(n)*f(n)
    for len2 in range(n):
        ans += f(len2)*f(len2) * f2(n-len2-1)
    return ans
    

if __name__ == "__main__":
    for n in range(100):
        print(f"{n=}, {f(n)=}, {f2(n)=}")

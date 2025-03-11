#!/usr/bin/env python3
from sys import stderr, stdout, argv

DEBUG_LEVEL = 2

def solve(n,m,d,x):
    # TODO: write here your solution!
    # what follows will be just good enough to respect the intended communication protocol with the server
    c = ['T'] * n
    falling_times = [-1] * n
    first_time = -1
    last_time = -1
    return c, falling_times, first_time, last_time

              
if __name__ == "__main__":
    if len(argv) == 2:
        DEBUG_LEVEL = int(argv[1])
    T = int(input())
    for t in range(1, 1 + T):
        if DEBUG_LEVEL > 0:
            print(f"#\n# Testcase {t}:", file=stderr)
        n, m = list(map(int, input().strip().split()))
        d = input().strip().split()
        x = list(map(int, input().strip().split()))
        if DEBUG_LEVEL > 1:
            print(f"# {n=}, {m=}\n# {d=}\n# {x=}", file=stderr)
        c, falling_times, first_time, last_time = solve(n,m,d,x)
        fouts = [stderr, stdout] if DEBUG_LEVEL > 1 else [stdout]
        for fout in fouts:
            print(" ".join(map(str,c)), file=fout)
            print(first_time, file=fout)
            print(last_time, file=fout)
            print(" ".join(map(str,falling_times)), file=fout)

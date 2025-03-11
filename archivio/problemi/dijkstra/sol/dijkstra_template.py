#!/usr/bin/env python3
from sys import stderr, stdout, argv


MOD = 10**9 + 7

def solve(n,out_nei):
    # TODO: write here your solution!
    # what follows will be just good enough to respect the intended communication protocol with the server
    dist = [n+1] * n
    dad = [0] * n
    num_minpathstrees = 0
    return dist, dad, num_minpathstrees

              
if __name__ == "__main__":
    debug_level = 0
    if len(argv) == 2:
        debug_level = int(argv[1])
    T = int(input())
    for t in range(1, 1 + T):
        if debug_level > 0:
            print(f"#\n# Testcase {t}:", file=stderr)
        n, m = map(int, input().strip().split())
        out_nei = [ [] for _ in range(n) ]
        for _ in range(m):
            a, b, w = map(int, input().strip().split())
            out_nei[a].append( (b, w) )
        if debug_level > 1:
            print(f"# {n=}, {m=}, {out_nei=}", file=stderr)
        dist, dad, num_minpathstrees = solve(n,out_nei)
        if debug_level > 2:
            print(f"# {dist=}\n# {dad=}\n# {num_minpathstrees=}", flush=True, file=stderr)
        print(" ".join(map(str,dist)))
        print(" ".join(map(str,dad)))
        print(num_minpathstrees)

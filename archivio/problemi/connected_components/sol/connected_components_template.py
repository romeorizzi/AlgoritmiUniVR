#!/usr/bin/env python3
from sys import stderr, stdout, argv


MOD = 10**9 + 7

def solve(n,nei):
    # TODO: write here your solution!
    # this should return the list of the connected components of the graph (in any order). In turn, every connected component is the list of its nodes (again in any order).
    
    CC = [ [v] for v in range(n) ] # this is just good enough to respect the intended communication protocol with the server (and would be correct only if the graph had no edges)
    
    return CC

              
if __name__ == "__main__":
    debug_level = 0
    if len(argv) == 2:
        debug_level = int(argv[1])
    T = int(input())
    for t in range(1, 1 + T):
        if debug_level > 0:
            print(f"#\n# Testcase {t}:", file=stderr)
        n, m = map(int, input().strip().split())
        nei = [ [] for _ in range(n) ]
        for _ in range(m):
            a, b = map(int, input().strip().split())
            nei[a].append(b)
            nei[b].append(a)
        if debug_level > 1:
            print(f"# {n=}, {m=}, {nei=}", file=stderr)
        CC = solve(n,nei)
        if debug_level > 2:
            print(f"# {CC=}", flush=True, file=stderr)
        print(len(CC))
        for C in CC:
            print(" ".join(str(v) for v in C))

#!/usr/bin/env python3
from sys import stderr, stdout, argv

def solve(n, out_nei, in_nei):
    """
    returns a quasi-kernel
    """
    # To do: compute and return the list of nodes of a 2-set
    fake_answer = []
    return fake_answer

              
if __name__ == "__main__":
    debug_level = 0
    if len(argv) == 2:
        debug_level = int(argv[1])
    T = int(input())
    for t in range(1, 1 + T):
        if debug_level > 0:
            print(f"#\n# Testcase {t}:", file=stderr)
        n, m = map(int, input().strip().split()); assert(n>=1)
        in_nei = [ [] for _ in range(n) ]
        out_nei = [ [] for _ in range(n) ]
        for _ in range(m):
            a, b = map(int, input().strip().split()); assert(0<=a<n); assert(0<=b<n)
            out_nei[a].append(b)
            in_nei[b].append(a)
        if debug_level > 1:
            print(f"# {n=}\n# {m=}\n# {out_nei=}\n# {in_nei=}", file=stderr)
        S2 = solver[0](n, out_nei, in_nei)
        if debug_level > 2:
            print(f"# {len(S2)=}\n# {S2=}", file=stderr)
        print(len(S2))
        print(" ".join(map(str, S2)))

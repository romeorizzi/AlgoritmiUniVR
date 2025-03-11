#!/usr/bin/env python3
from sys import stderr,stdout, argv

DEBUG_LEVEL = 0

if __name__ == "__main__":
    if len(argv) == 2:
        DEBUG_LEVEL = int(argv[1])
    T = int(input())
    for t in range(1, 1 + T):
        if DEBUG_LEVEL > 0:
            print(f"#\n# Testcase {t}:", file=stderr)
        n,m = map(int, input().strip().split())
        V = list(map(int, input().strip().split()))
        G = list(map(int, input().strip().split()))
        if DEBUG_LEVEL > 1:
            print(f"# {n=}, {m=}\n# {V=}\n# {G=}\n", file=stderr)

        opt_val = 42
        optS = ["1"] * m; optT = ["1"] * n
        num_opt_sols = 69
        num_opt_sets = 666
        
        fouts = [stdout]
        if DEBUG_LEVEL > 0:
            fouts.append(stderr)
        for fout in fouts:
            print(opt_val, file=fout)
            print(" ".join(optT), file=fout)
            print(" ".join(optS), file=fout)
            print(num_opt_sols, file=fout)
            print(num_opt_sets, file=fout)

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
        n,q = map(int, input().strip().split())
        L = list(map(int, input().strip().split()))
        if DEBUG_LEVEL > 1:
            print(f"# {n=}, {q=}\n# {L=}\n", file=stderr)

        # SOLVE (ToDo):    
        opts = []
        num_exposed = 42 
        num_exposed_unconstrained = 666
        num_exposed_sort = 128
        
        fouts = [stdout]
        if DEBUG_LEVEL > 0:
            fouts.append(stderr)
        for fout in fouts:
            print(f"{num_exposed_unconstrained} {num_exposed_sort} {num_exposed}", file=fout)
            print(" ".join(map(str,opts)), file=fout)

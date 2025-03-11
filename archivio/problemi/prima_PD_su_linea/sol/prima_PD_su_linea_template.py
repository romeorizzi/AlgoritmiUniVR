#!/usr/bin/env python3
from sys import stderr, stdout, argv


MOD = 10**9 + 7

def num_feasible_solutions(n):
    """returns the number of feasible solutions for an input array A of n cells."""
    assert n >= 0
    # TODO: write here your solution!
    # what follows will be just good enough to respect the intended communication protocol with the server
    risp = 1 % MOD
    return risp


def optimize(n,A):
    """returns the triple (optval,optsol,num_optsols) where optsol is the list of indexes of any optimal solution for the instance comprising of the first n cells of array A. A first inefficient but essential solution might take inspiration from a minimal recursive implementation of the function num_feasible_solutions above"""
    assert n >= 0
    assert n == len(A)
    # TODO: write here your solution!
    # what follows will be just good enough to respect the intended communication protocol with the server
    optval,optsol,num_optsols = 0,[],1 % MOD
    return optval,optsol,num_optsols

              
if __name__ == "__main__":
    debug_level = 0
    if len(argv) == 2:
        debug_level = int(argv[1])
    T = int(input())
    for t in range(1, 1 + T):
        if debug_level > 0:
            print(f"#\n# Testcase {t}:", file=stderr)
        n = int(input())
        if debug_level > 1:
            print(f"{n=}", file=stderr)
        A = list(map(int, input().strip().split()))
        if debug_level > 1:
            print(f"{A=}", file=stderr)
        optval, optsol, num_optsols = optimize(n,A)
        num_feas_sols = num_feasible_solutions(n)
        if debug_level > 2:
            print(f"{num_optsols=},{optval=},{optsol=},{num_feas_sols=}", flush=True, file=stderr)
        fouts = [stderr, stdout] if debug_level > 3 else [stdout]
        for fout in fouts:
            print(num_feas_sols, file=fout)
            print(optval, file=fout)
            print(" ".join(map(str,optsol)), file=fout)
            print(num_optsols, file=fout)
            fout.flush()

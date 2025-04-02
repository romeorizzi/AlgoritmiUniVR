#!/usr/bin/env python3
from sys import stderr, stdout, argv

pieces = [1,2,5,10,20,50,100,200,500,1000]

def solve(S):
    # TODO: write here your solution!
    optsol = [0] * len(pieces) # this will be good enough to respect the intended communication protocol with the server
    optval = sum(optsol)
    return optval, optsol

if __name__ == "__main__":
    debug_level = 0
    if len(argv) == 2:
        debug_level = int(argv[1])
    T = int(input())
    for t in range(1, 1 + T):
        S = int(input())
        if debug_level > 0:
            print(f"#\n# Testcase {t} ({S=}):", file=stderr)
        optval, optsol = solve(S)
        if debug_level > 1:
            print(f"# {optval=}\n# {optsol=}", flush=True, file=stderr)
        print(optval)
        print(" ".join(map(str,optsol)))

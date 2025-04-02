#!/usr/bin/env python3
from sys import stderr, stdout, argv

def solve(n,h):
    """
    INPUT: n (the number of dominos), h (the array with the heights of the dominos)
    OUTPUT: single_rise_val, single_rise_index, distributed_rise_tot, distributed_rise_new_h (array)
    """

    # TODO: write here your solution!
    # what follows will be just good enough to respect the intended communication protocol with the server
    distributed_rise_new_h = h[:]
    single_rise_val = 0
    single_rise_index = 0
    return single_rise_val, single_rise_index, distributed_rise_new_h

              
if __name__ == "__main__":
    debug_level = 0
    if len(argv) == 2:
        debug_level = int(argv[1])
    T = int(input())
    for t in range(1, 1 + T):
        if debug_level > 0:
            print(f"#\n# Testcase {t}:", file=stderr)
        n = int(input()); assert(1 <= n); assert(n <= 10**6)
        h = list(map(int, input().strip().split())); assert(len(h)==n); assert(all([_ > 0 for _ in h]))
        if debug_level > 1:
            print(f"# {n=}\n# {h=}", file=stderr)
        single_rise_val, single_rise_index, distributed_rise_new_h = solve(n,h)
        if debug_level > 2:
            print(f"# {single_rise_val=} {single_rise_index=}\n# {distributed_rise_new_h=}", file=stderr)
        print(single_rise_val, single_rise_index)
        print(" ".join(map(str, distributed_rise_new_h)))

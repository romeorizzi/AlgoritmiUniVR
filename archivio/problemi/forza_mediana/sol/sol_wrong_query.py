#!/usr/bin/env python3
from sys import stdout, stderr
    
def get_med_of_3(a, b, c):
    print(a, b, c, flush=True)
    #print(a, b, c, file=stderr)
    return int(input())

if __name__ == "__main__":
    T = int(input())
    for t in range(1, 1+T):
        print(f"#\n# Testcase {t}:", file=stderr)
        n = int(input())
        print(f"{n=}", file=stderr)
        assert n % 2
        get_med_of_3(0, 1, n)

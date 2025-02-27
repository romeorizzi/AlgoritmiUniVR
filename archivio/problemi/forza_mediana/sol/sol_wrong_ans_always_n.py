#!/usr/bin/env python3
from sys import stdout, stderr

if __name__ == "__main__":
    T = int(input())
    for t in range(1, 1+T):
        print(f"#\n# Testcase {t}:", file=stderr)
        n = int(input())
        print(f"{n=}", file=stderr)
        assert n % 2
        print(n, flush=True)

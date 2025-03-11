#!/usr/bin/env python3
from sys import stderr,stdout, argv

DEBUG_LEVEL = 2

def get_doomed(c):
    # TODO: write here your solution!
    # what follows will be just good enough to respect the intended communication protocol with the server
    
    doomed = [1] * len(c)
    return doomed
    
def save_Ryan(c,y):
    # TODO: write here your solution!
    # what follows will be just good enough to respect the intended communication protocol with the server
    
    my_save_Ryan_plan = [0 if colore_guelfo == "D" else -1 for colore_guelfo in c]
    return my_save_Ryan_plan


if __name__ == "__main__":
    if len(argv) == 2:
        DEBUG_LEVEL = int(argv[1])
    T = int(input())
    for t in range(1, 1 + T):
        if DEBUG_LEVEL > 0:
            print(f"#\n# Testcase {t}:", file=stderr)
        n = int(input())
        c = input().strip().split(); assert(len(c)==n); assert(all([_ in {"B","N","D"} for _ in c]))
        y = int(input())
        if DEBUG_LEVEL > 1:
            print(f"# {n=}, {y=}\n# {c=}", file=stderr)
        doomed = get_doomed(c)
        plan4Ryan = save_Ryan(c,y)
        fouts = [stderr, stdout] if DEBUG_LEVEL > 1 else [stdout]
        width = 1 + max(len(str(_)) for _ in plan4Ryan)
        for fout in fouts:
            print(" ".join(str(_).rjust(width) for _ in doomed), file=fout)
            print(" ".join(str(_).rjust(width) for _ in c), file=fout)
            print(" ".join(str(_).rjust(width) for _ in plan4Ryan), file=fout)

#!/usr/bin/env python3
from sys import stderr,stdout, argv

DEBUG_LEVEL = 0

def pianifica(lista_corsi):
    n = len(lista_corsi)
    """ogni corso della lista è una quadrupla:
        - i: nome del corso (first 1 a n)
        - first: primo giorno del corso
        - last: ultimo giorno del corso
        - val: numero crediti del corso
    """
    opt_val = 42
    opt_sol = [i + 1 for i in range(n)]
    return opt_val, opt_sol


T = int(input())
for t in range(1, 1 + T):
    if DEBUG_LEVEL > 0:
        print(f"#\n# Testcase {t}:", file=stderr)
    n = int(input())
    lista_corsi = []
    for i in range(n):
        da, a, crediti = map(int, input().strip().split())
        lista_corsi.append({"name": i+1, "first": da, "last": a, "val": crediti})
    if DEBUG_LEVEL > 1:
        print(f"# {n=}\n# {lista_corsi=}\n\n", file=stderr)
    opt_val, opt_sol = pianifica(lista_corsi)
    fouts = [stdout]
    if DEBUG_LEVEL > 0:
        fouts.append(stderr)
    for fout in fouts:
        print(opt_val, file=fout)
        print(" ".join(map(str,opt_sol)), file=fout)


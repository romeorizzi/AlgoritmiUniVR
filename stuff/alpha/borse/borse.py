#!/usr/bin/python3

from sys import stdin, stdout, stderr, setrecursionlimit

# setrecursionlimit(1500)

MAXN=10**3
risp = [[1] * (MAXN + 1)] + [[None] * (MAXN + 1) for _ in range(MAXN)]
# risp[bb][tt] = numero di soluzioni se badget=<bb> e tetto=<tt>


#versione 3: programmazione dinamica
def count_sols(b):
    """ritorna il numero di soluzioni se badget=<b>"""
    assert b >= 0
    for bb in range(1,b+1):
        for tt in range(1,bb+1):
            risp[bb][tt] = 0
            for first in range(1, 1 + min(bb,tt)):
                risp[bb][tt] += risp[bb-first][min(first,bb-first)]
    return risp[b][b]


b = int(input("Inserire b, l'ammontare del budget da distribuire in premi: "))
#print(f"ver 1- #soluzioni: {count_sols_v1(b, b)}")
#print(f"ver 2- #soluzioni: {count_sols_v2(b, b)}")
print(f"ver 3- #soluzioni: {count_sols(b)}")


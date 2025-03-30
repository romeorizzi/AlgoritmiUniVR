#!/usr/bin/python
from sys import stdin, stdout, stderr

# 3 versioni a confronto (per il solo counting)

#versione 1: ricorsione pura
def count_sols_v1(b,t):
    """ritorna il numero di soluzioni se badget=<b> e tetto=<t>"""
    assert b >= 0
    assert t > 0
    if b == 0:
        return 1
    risp = 0
    for first in range(1, 1 + min(b,t)):
        risp += count_sols_v1(b-first, first)
    return risp

#versione 2: ricorsione con memoizzazione
MAXN=10**3
memo = [[1] * (MAXN + 1)] + [[None] * (MAXN + 1) for _ in range(MAXN)]
def count_sols_v2(b,t):
    """ritorna il numero di soluzioni se badget=<b> e tetto=<t>"""
    assert b >= 0
    assert t > 0 or b == 0
    if memo[b][t] is None:
        memo[b][t] = 0
        for first in range(1, 1 + min(b,t)):
            memo[b][t] += count_sols_v2(b-first, first)
    return memo[b][t]

#versione 3: programmazione dinamica (in altro file, e poi la useremo anche per il ranking e l'unranking)

b = int(input("Inserire b, l'ammontare del budget da distribuire in premi: "))
#print(f"ver 1- #soluzioni: {count_sols_v1(b, b)}")
print(f"ver 2- #soluzioni: {count_sols_v2(b, b)}")

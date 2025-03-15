#!/usr/bin/python
from sys import stdin, stdout, stderr

from functools import cache

@cache
def count_sols(b,t):
    """ritorna il numero di soluzioni se badget=<b> e tetto=<t>"""
    assert b >= 0
    assert t > 0 or b == 0
    if b == 0:
        return 1
    risp = 0
    for first in range(1, 1 + min(b,t)):
        risp += count_sols(b-first, min(first, b-first))
    return risp

def unrank(b,t,r):
    """restituisce la soluzione di rango <r> tra quelle per badget=<b> e tetto=<t>"""
    assert b >= 0
    assert t > 0 or b == 0
    assert r < count_sols(b,t)
    if b == 0:
        return []
    #for first in range(min(b,t), 0, -1):    
    for first in range(1, 1 + min(b,t)):
        if r >= count_sols(b-first, first):
            r -= count_sols(b-first, first)
        else:
            return [first] + unrank(b-first, first, r)

def rank(sol):
    """restituisce il rango della soluzione <sol> tra quelle per il suo stesso badget"""
    t = b = sum(sol)
    risp = 0
    for pos in range(len(sol)):
        #for first in range(min(b,t), sol[pos], -1):    
        for first in range(1, sol[pos]):
            risp += count_sols(b-first, first)
        b -= sol[pos]
        t = min(b, sol[pos])
    return risp


b = int(input("Inserire b, l'ammontare del budget da distribuire in premi: "))
print(f"#soluzioni: {count_sols(b, b)}")
r = int(input(f"\nInserire il rango della soluzione intesa ([0-{count_sols(b, b) - 1}]): "))
sol = unrank(b,b,r)
print(" ".join(map(str,sol)))
sol = list(map(int, input("\nInserire una ripartizione valida di premi agli studenti:\n").strip().split()))
curr=sol[0]
for nxt in sol[1:]:
    assert curr > 0, "I do not accept values smaller than 1 in your sequence of prizes."
    assert curr >= nxt, "Warning: Your sequence of prizes decreases! This is against the rules."
print(rank(sol))


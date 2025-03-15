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

b = int(input("Inserire b, l'ammontare del budget da distribuire in premi: "))
print(f"#soluzioni: {count_sols(b, b)}")

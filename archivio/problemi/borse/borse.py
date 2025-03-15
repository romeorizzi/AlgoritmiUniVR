#!/usr/bin/python
from sys import stdin, stdout, stderr

def count_sols(b,t):
    """ritorna il numero di soluzioni se badget=<b> e tetto=<t>"""
    assert b >= 0
    assert t > 0 or b == 0
    if b == 0:
        return 1
    risp = 0
    for first in range(1, 1 + min(b,t)):
        risp += count_sols(b-first, first)
    return risp

def stampa_sols(b,t, history):
    """stampa le soluzioni per badget=<b> e tetto=<t>, ciascuna prefissata con <history>"""
    assert b >= 0
    assert t > 0 or b == 0
    if b == 0:
        print(history)
    #for first in range(min(b,t), 0, -1):    
    for first in range(1, 1 + min(b,t)):
        stampa_sols(b-first, first, history + f" {first} ")




b = int(input("Inserire b, l'ammontare del budget da distribuire in premi: "))
print(f"Ecco le {count_sols(b, b)} soluzioni:")
stampa_sols(b,b, "")



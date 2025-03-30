#!/usr/bin/python
from sys import stdin, stdout, stderr

"""La programmazione dinamica:
     la programmazione dinamica è un'importante e generale tecnica algoritmica e di problem solving.
     Possiamo considerarla come un'implementazione della ricorsione all'insegna dell'efficienza.
     E' parente strettissima della ricorsione con memoizzazione, ma, a seconda dei casi, può essere essenziale avvalersi dell'una piuttosto che dell'altra. (In ogni caso è bene conoscerle e provare a praticarle entrambe, offrono punti di vista complementari.)
""" 

#versione 3: programmazione dinamica
def count_sols(b):
    """ritorna il numero di soluzioni se badget=<b>"""
    assert b >= 0
    risp = [[1] * (b + 1)] + [[None] * (b + 1) for _ in range(b)]
    # risp[bb][tt] = numero di soluzioni se badget=<bb> e tetto=<tt>
    for bb in range(1,b+1):
        for tt in range(1,bb+1):
            risp[bb][tt] = 0
            for first in range(1, 1 + min(bb,tt)):
                risp[bb][tt] += risp[bb-first][min(first,bb-first)]
    return risp[b][b]


b = int(input("Inserire b, l'ammontare del budget da distribuire in premi: "))
print(f"ver 3- #soluzioni: {count_sols(b)}")



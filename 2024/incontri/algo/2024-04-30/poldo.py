#!/usr/bin/python
from sys import stdin, stdout, stderr

def opt_val(i,j):
    assert j <= i
    """ritorna il massimo numero di pannini (=massima lunghezza di una sotto-sequenza crescente) della sequenza suffisso pannino[i:] sotto il vincolo di non includere nessun pannino di colesterolo < pannino[j]"""
    if i >= len(pannino):
        return 0
    if pannino[j] > pannino[i]:
        return opt_val(i+1,j)
    return max( opt_val(i+1,j), 1 + opt_val(i+1,i) )

def opt_val2(i):
    """ritorna il massimo numero di panini (=massima lunghezza di una sotto-sequenza crescente) che riesco a mangiare se comincio la scorpacciata partendo col panino panino[i]"""
    assert 0 <= i < len(panino)
    if i == len(panino) - 1:
        return 1
    best = 1 # mangio solo il panino i
    for j in range(i+1,len(panino)): # se mangio un secondo panino, sia esso j
        if panino[j] > panino[i]: # ok, posso mangiare j dopo i -filtro-
           best = max(best, 1 + opt_val2(j))
    return best


    
n = int(input())
panino = list(map(int, input().strip().split()))

pannino = [-1] + panino
print(f"{n=}\n{panino=}\n", file=stderr)

print(f"{opt_val(1,0)=}\n", file=stderr)

for i in range(len(panino)):
   print(f"{i=}, {opt_val2(i)=}\n", file=stderr)


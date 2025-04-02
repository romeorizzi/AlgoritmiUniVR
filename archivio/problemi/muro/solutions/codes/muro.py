#!/usr/bin/env python3
from sys import stderr,stdout, argv

"""politica greedy implementata:
  i: 1  2  3  4  5  6  7  8
L_i  3, 2, 5, 3, 2, 7, 4, 4
Snapshots:
1 1 1
1 2 2
1 2 3 3 3 3 3
1 2 3 4 4 4 3
1 2 3 4 5 5 3   
1 6 6 6 6 6 6
1 6 7 7 7 7 6
1 6 7 8 8 8 8

iplementata come un automa che colloca il singolo pezzo in funzione dello stato corrente <num_exposed> (=numero di diversi colori esposti - invariante: sono tutti esposti entro il prefisso di lunghezza <num_exposed>) e del numero L_i in ingresso. Nota: ci basta che l'automa ritorni il nuova valore di gain!

"""

def next_num_exposed(num_exposed, L_i):
    if num_exposed + L_i <= n:
        return num_exposed + 1
    else:
        return n - L_i + 1

def opt_unconstrained(n, q):
    return min(n,q)

def opt_sort(n, L):
    count_lengths = [0] * (n+1)
    for L_i in L:
        count_lengths[L_i] += 1 
    num_exposed = 0
    for length in range(n,-1,-1):
        for _ in range(count_lengths[length]): 
            if num_exposed + length <= n:
                num_exposed += 1 
    return num_exposed

T = int(input())
for t in range(1, 1 + T):
    n,q = map(int, input().strip().split())
    L = list(map(int, input().strip().split()))
    opts = []
    num_exposed = 0
    for L_i in L:
        num_exposed = next_num_exposed(num_exposed, L_i)
        opts.append(num_exposed)
    print(f"{opt_unconstrained(n, q)} {opt_sort(n, L)} {opts[-1]}")
    print(" ".join(map(str,opts)))

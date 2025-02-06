#!/usr/bin/python
from sys import stdin, stdout, stderr

def min_fogli(left,right):
    """ritorna il minimo numero di fogli necessario per costruire l'arcobalemo A[left,right]"""
    assert 0 <= left <= right <= n - 1
    print(f"called min_fogli({left=},{right=})", file=stderr)
    if right <= left + 1:
        return 0
    best_val = 1 + min_fogli(left + 1,right) # il primo colore è servito da un foglio privato
    for next_app_first in range(left+1,right):
        if A[left] == A[next_app_first]:
            best_val = min(best_val, min_fogli(left,next_app_first) + min_fogli(next_app_first,right) - 1 )
    return best_val
    
    

n = int(input())
A = list(map(int, input().strip().split()))


print(f"Received instance: {n=}, {A=}", file=stderr)
print(min_fogli(0,n-1))

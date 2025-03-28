#!/usr/bin/python
from sys import stdin, stdout, stderr

def min_fogli(left,right):
    """ritorna il minimo numero di fogli necessario per costruire l'arcobalemo A[left,right]"""
    assert 0 <= left <= right + 1 <= n
    #print(f"called min_fogli({left=},{right=})", file=stderr)
    if right == left:
        return 1
    elif right < left:
        return 0
    best_val = 1 + min_fogli(left + 1,right) # il primo colore è servito da un foglio privato
    for next_app_first in range(left+1,right+1):
        if A[left] == A[next_app_first]:
            best_val = min(best_val, min_fogli(left+1,next_app_first-1) + min_fogli(next_app_first,right) )
    return best_val
    
    

n = int(input())
A = list(map(int, input().strip().split()))


print(f"Received instance: {n=}, {A=}", file=stderr)
print(min_fogli(0,n-1))

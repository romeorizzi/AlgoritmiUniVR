#!/usr/bin/python
from sys import stderr

MAXN = 10
MAXU = 10
"""
PROBLEM: for each one of the N floors of a building we want to know whether an egg lounched from that floor would breake (to help us, it is assumed that if an egg would breake from floor i then it would breake also from floor i+1).

 risp[U][N] = the minimum integer x such that there exists a strategy to acquire full knowledge (would an egg brake from floor i, for each i=1,...,N) within at most x experiments (whatever their outcome), assuming we are given U intact eggs to conduct them.
"""

def my_format(num):
    return format(num, '03d')

#risp = [ [int('9'*3) for _ in range(MAXN + 1)] for u in range(MAXU + 1)]
risp = [ [int('9'*3) for _ in range(MAXN + 1)] for u in range(2)]
risp[0][0] = 0
for U in range(MAXU + 1):
    if U > 1:
        risp[U%2][0] = 0
        risp[U%2][1] = 1
        for N in range(2, MAXN + 1):
            risp[U%2][N] = N
            for first_test in range(1,N+1):
                opt_if_bounch = 1 + risp[U%2][N - first_test]
                opt_if_crash = 1 + risp[(U-1)%2][first_test - 1]
                risp[U%2][N] = min(risp[U%2][N], max(opt_if_bounch, opt_if_crash))
    print(" ".join(map(my_format, risp[U%2])))
   

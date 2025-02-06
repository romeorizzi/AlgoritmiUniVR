#!/usr/bin/python
from sys import stderr

MAXN = 28
MAXU = 10
"""
PROBLEM: for each one of the N floors of a building we want to know whether an egg lounched from that floor would breake (to help us, it is assumed that if an egg would breake from floor i then it would breake also from floor i+1).

 risp[U][N] = the minimum integer x such that there exists a strategy to acquire full knowledge (would an egg brake from floor i, for each i=1,...,N) within at most x experiments (whatever their outcome), assuming we are given U intact eggs to conduct them.
"""

def my_format(num):
    return format(num, '03d')

risp = [ [0] + [-1]*MAXN, [N for N in range(MAXN + 1)] ]
highest_floor_for_opt_first_move = [ [-1]*(MAXN + 1), [-1] + [1]*MAXN]
for U in range(MAXU + 1):
    if U > 1:
        risp[U%2][0] = 0; highest_floor_for_opt_first_move[U%2][0] = -1 
        risp[U%2][1] = 1; highest_floor_for_opt_first_move[U%2][1] = 1
        top_floor_4_opt_fm = 1
        #breakpoint()
        for N in range(2, MAXN + 1):
            opt_if_bounch = 1 + risp[U%2][N - top_floor_4_opt_fm]
            if opt_if_bounch <= risp[U%2][N-1]:
                risp[U%2][N] = risp[U%2][N-1]
                highest_floor_for_opt_first_move[U%2][N] = top_floor_4_opt_fm
                assert top_floor_4_opt_fm == highest_floor_for_opt_first_move[U%2][N-1]
            else:
                risp[U%2][N] = risp[U%2][N-1] + 1
                top_floor_4_opt_fm += 1
                assert 1 + risp[(U-1)%2][top_floor_4_opt_fm - 1] <= risp[U%2][N], f"{U=}, {N=}, {top_floor_4_opt_fm=}, {risp[(U-1)%2][top_floor_4_opt_fm - 1]=}, {risp[U%2][N]=}"
                while 1 + risp[(U-1)%2][top_floor_4_opt_fm] <= risp[U%2][N]:
                    top_floor_4_opt_fm += 1
                highest_floor_for_opt_first_move[U%2][N] = top_floor_4_opt_fm
    print(" ".join(map(my_format, risp[U%2])))
    print(" ".join(map(my_format, highest_floor_for_opt_first_move[U%2])), file=stderr)
    print(file=stderr)
   

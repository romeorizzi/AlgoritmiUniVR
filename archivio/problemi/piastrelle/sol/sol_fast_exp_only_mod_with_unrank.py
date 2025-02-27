#!/usr/bin/env python3
from sys import stderr, set_int_max_str_digits

set_int_max_str_digits(10**6)

MOD = 1000000007

def mod_sum(val1, val2):
    if val1[0] + val2[0] >= MOD:
        return ( (val1[0] + val2[0])%MOD, True)
    return (val1[0] + val2[0], val1[1] or val2[1])

def mod_prod(val1, val2):
    if val1[0] * val2[0] >= MOD:
        return ( (val1[0] * val2[0])%MOD, True)
    return (val1[0] * val2[0], val1[1] or val2[1])

F= [ [(1,False), (1,False)],
     [(1,False), (0,False)] ]

""" [f(n),f(n-1)]' = F*[f(n-1),f(n-2)]' = F^(n-1) * [f(1),f(0)]'
                                        = F^(n-1)*[1,1]'
    f(n) = F^(n-1)[0][1] + F^(n-1)[0][0]
    F^n = (F^(n//2)^2 * F)
"""

def matrix_product(A, B):
    return [ [mod_sum(mod_prod(A[0][0],B[0][0]), mod_prod(A[0][1],B[1][0])),  mod_sum(mod_prod(A[0][0],B[0][1]), mod_prod(A[0][1],B[1][1])) ],
             [mod_sum(mod_prod(A[1][0],B[0][0]), mod_prod(A[1][1],B[1][0])),  mod_sum(mod_prod(A[1][0],B[0][1]), mod_prod(A[1][1],B[1][1])) ] ]
             
def square(M):
    return [ [mod_sum(mod_prod(M[0][0],M[0][0]), mod_prod(M[0][1],M[1][0])),  mod_sum(mod_prod(M[0][0],M[0][1]), mod_prod(M[0][1],M[1][1])) ],
             [mod_sum(mod_prod(M[1][0],M[0][0]), mod_prod(M[1][1],M[1][0])),  mod_sum(mod_prod(M[1][0],M[0][1]), mod_prod(M[1][1],M[1][1])) ] ]

def timesF(M):
    return [ [mod_sum(mod_prod(M[0][0],F[0][0]), mod_prod(M[0][1],F[1][0])),  mod_sum(mod_prod(M[0][0],F[0][1]), mod_prod(M[0][1],F[1][1])) ],
             [mod_sum(mod_prod(M[1][0],F[0][0]), mod_prod(M[1][1],F[1][0])),  mod_sum(mod_prod(M[1][0],F[0][1]), mod_prod(M[1][1],F[1][1])) ] ]

def F_to_the(n):
    assert n >= 0
    if n == 0:
        return [[(1,False),(0,False)],[(0,False),(1,False)]]
    elif n % 2 == 1:
        return timesF(F_to_the(n-1))
    return square(F_to_the(n//2))
             
             
def f_fast_exp(n):
    """returns the number of tilings for a 1xn-grid with 1x1 ad 1x2 tiles."""
    #print(f"function f called with argument {n=}", file=stderr)
    assert n >= 0
    if n <= 1:
        return (1,False)
    F_to_n_minus_1 = F_to_the(n-1)
    return mod_sum(F_to_n_minus_1[0][1], F_to_n_minus_1[0][0])


def rank(T, n):
    """returns the rank of tiling T among the tilings of the 1xn-grid."""
    #print(f"function rank called with arguments {T=}, {n=}", file=stderr)
    assert n >= 0
    risp = 0
    pos_in_T = 0
    while n > 1:
        if T[pos_in_T + 1] == "]":
            n -= 1
            pos_in_T += 2
        else:
            risp += f_fast_exp(n-1)[0]
            n -= 2
            pos_in_T += 4
    return risp    

def unrank(n, rank):
    #print(f"function unrank called with arguments {n=}, {rank=}", file=stderr)
    assert n >= 0
    risp = ""
    while n > 0:
        f_val, f_overflow = f_fast_exp(n-1)
        if rank < f_val or f_overflow:
            risp += "[]"
            n -= 1
        else:
            risp += "[--]"
            rank -= f_val
            n -= 2
    return risp


if __name__ == "__main__":
    T = int(input())
    for t in range(1, 1+T):
        print(f"#\n# Testcase {t}:", file=stderr)
        n, c, r, u = map(int, input().strip().split())
        assert 0 <= c <= 1
        if c == 1:
            print(f_fast_exp(n)[0])
            #print(f_fast_exp(n), file=stderr)
        for i in range(r):
            T = input().strip()
            print(rank(T, n))
            #print(rank(T, n), file=stderr)
        for i in range(u):
            rnk = int(input())
            print(unrank(n, rnk))
            #print(unrank(n, rnk), file=stderr)

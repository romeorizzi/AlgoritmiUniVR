#!/usr/bin/env python3

from sys import stdout, stderr

def get_med_of_3(a, b, c):
    print(a, b, c, flush=True)
    print(a, b, c, file=stderr)
    med = int(input())
    print(f"{med=}", file=stderr)
    return med

MY_MIN = None
def is_smaller_assuming_min_is_MY_MIN(a, b):
    # a is smaller than b iff a is inbetween MY_MIN and b
    return (a == get_med_of_3(a, b, MY_MIN) )

def display_vector(v, n):
    # return
    for i in range(n):
        print(str(v[i]), end=" ", file=stderr)
    print(file=stderr)

def binary_search(val, v, n):
    # vector v, of length n, is assumed to be sorted in strictly increasing. Returns the smallest index j in [0,n) such that v[j] >= val
    # returns n if no such index exists.
    # the values stored in vector v are actually names of objects that get compared via oracle call.
    assert n >= 1
    display_vector(v, n)
    left = 0; right = n
    while right > left:
        med = (left + right) // 2
        if is_smaller_assuming_min_is_MY_MIN(val, v[med]):
            right = med
        else:
            left = med + 1
    return right


if __name__ == "__main__":
    T = int(input())
    for t in range(1, 1+T):
        print(f"#\n# Testcase {t}:", file=stderr)
        n = int(input())
        print(f"{n=}", file=stderr)
        assert n % 2
        if n == 1:
            print(0, flush=True)
        else:
            extA = 0
            extB = 1
            for i in range(2, n):
                med = get_med_of_3(i, extA, extB)
                if med == extA:
                    extA = i
                if med == extB:
                    extB = i
            MY_MIN = extA;
            candidates = []
            for i in range(n):
                if i != extA and i != extB:
                    candidates.append(i)
            display_vector(candidates, n-2)
            for i in range(1, n - 2):
                display_vector(candidates, i+1)
                name_to_be_inserted = candidates[i]
                pos_ins = binary_search(name_to_be_inserted, candidates, i)
                for j in range(i, pos_ins, -1):
                    candidates[j] = candidates[j - 1]
                candidates[pos_ins] = name_to_be_inserted
            display_vector(candidates, n-2)
            print(candidates[n // 2 - 1], flush=True)

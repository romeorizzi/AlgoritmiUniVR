#!/usr/bin/env python3

from sys import stdout, stderr
import random

def get_med_of_3(a, b, c):
    print(a, b, c, flush=True)
    print(f"get_med_of_3({a}, {b}, {c}) = ?", file=stderr)
    med = int(input())
    print(f"get_med_of_3({a}, {b}, {c}) = {med}", file=stderr)
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

    
def randomized_select(v, n, rank):
    # v is an array of length n all of whose elements have different values.
    # where rank in [0,n), returns the element of this rank within v (the smallest element of v has rank 0)
    print(f"called randomized_select on a vector of length {n}", file=stderr)
    display_vector(v, n)
    assert n > 0
    if n == 1:
        assert rank == 0
        return v[0]
    if n == 2:
        if (rank == 0) == is_smaller_assuming_min_is_MY_MIN(v[0], v[1]):
            return v[0]
        else:
            return v[1]
    if n == 3:
        if rank == 1:
            return get_med_of_3(v[0], v[1], v[2])
        mid = get_med_of_3(v[0], v[1], v[2])
        if v[2] == mid:
            return randomized_select(v, 2, rank)
        if v[0] == mid:
            return randomized_select(v[1:], 2, rank)
        v[1] = v[2]
        return randomized_select(v, 2, rank)
    
    pivot_pos = random.randint(0, n-1)
    pivot = v[pivot_pos]
    v[pivot_pos] = v[n-1]
    v[n-1] = pivot
    
    left = 0
    right = n-2
    while left <= right:
        print(f"{left=}, {v[right]=}", file=stderr)
        print(f"{right=}, {v[right]=}", file=stderr)
        display_vector(v, n)
        while left <= right and is_smaller_assuming_min_is_MY_MIN(v[left], pivot):
            left += 1
        if left > right:
            break
        elif left == right:
            v[right+1] = v[right]
            right -= 1
            break
        while left < right and is_smaller_assuming_min_is_MY_MIN(pivot, v[right]):
            if left == right - 1:
                v[right+1] = v[left]
                right -= 2
                break
            else:
                v[right+1] = v[right]
                right -= 1
        if left == right + 1:
            break
        if left == right:
            v[right+1] = v[left]
            right -= 1
            break
        v[right+1] = v[left]
        v[left] = v[right]
        left += 1
        right -= 1
    print(f"{left=}, {right=}", file=stderr)
    assert left == right+1
    v[left] = pivot
    display_vector(v, n)
    if left == rank:
        return pivot
    if left > rank:
        return randomized_select(v, left, rank)
    return randomized_select(v[left+1:], n-left-1, rank-left-1)

if __name__ == "__main__":
    random.seed()
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
            print(randomized_select(candidates, n-2, n//2 - 1), flush=True)

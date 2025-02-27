#!/usr/bin/env python3

from sys import stdout, stderr

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

def display_vector(v, left, right_x):
    # return
    for i in range(left, right_x):
        print(str(v[i]), end=" ", file=stderr)
    print(file=stderr)

def merge_sort(v, left, right_x):
    # sorts v[left, right_x) in increasing value of weights
    n = right_x - left
    assert n >= 0
    print(f"called merge_sort ({left=}, {right_x=}, {v=}) over the following sub-vector of length {n}", file=stderr)
    display_vector(v, left, right_x)
    if n <= 1:
        return
    merge_sort(v, left, left + n // 2)
    print(f"Display of the global (n-2)-vector, just sorted over [{left},{left + n // 2}), AFTER EXITING:", file=stderr)
    display_vector(v, 0, len(v))
    merge_sort(v, left + n // 2, right_x)
    print(f"Display of the global (n-2)-vector, just sorted over [{left + n // 2},{right_x}), AFTER EXITING:", file=stderr)
    display_vector(v, 0, len(v))
    bottle = [0] * n
    pos1 = left
    pos2 = left + n // 2
    for i in range(n):
        print(f"{pos1=}, {pos2=}", file=stderr, end="")
        print(f", {v[pos1]=}, {v[pos2]=}", file=stderr)
        if pos1 == left + n // 2:
            print("Case: pos1 == left + n // 2", file=stderr)
            bottle[i] = v[pos2]
            pos2 += 1
        elif pos2 == right_x:
            print("Case: pos2 == right_x", file=stderr)
            bottle[i] = v[pos1]
            pos1 += 1
        elif is_smaller_assuming_min_is_MY_MIN(v[pos1], v[pos2]):
            print("Case: v[pos1] == smaller", file=stderr)
            bottle[i] = v[pos1]
            pos1 += 1
        else:
            print("Case: else", file=stderr)
            bottle[i] = v[pos2]
            pos2 += 1
    assert pos1 == left + n // 2
    assert pos2 == right_x
    print("Now merging", file=stderr)
    display_vector(v, left, left + n // 2)
    print("and", file=stderr)
    display_vector(v, left + n // 2, right_x)
    print("within the global (n-2)-vector", file=stderr)
    display_vector(v, 0, len(v))
    for i in range(n):
        v[i+left] = bottle[i]
    print(f"Display of the global (n-2)-vector, just sorted over [{left},{right_x}), BEFORE EXITING:", file=stderr)
    display_vector(v, 0, len(v))

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
            candidates.append(-1) # this cork is useful when debugging
            display_vector(candidates, 0, n-2)
            merge_sort(candidates, 0, n-2)
            display_vector(candidates, 0, n-2)
            print(candidates[n // 2 - 1])

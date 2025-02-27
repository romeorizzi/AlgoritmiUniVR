#!/usr/bin/env python3
from sys import stdout, stderr

def get_med_of_3(a, b, c):
    print(a, b, c, flush=True)
    print(a, b, c, file=stderr)
    med = int(input())
    print(f"{med=}", file=stderr)
    return med

def display_vector(n, v):
    # return
    for i in range(n):
        print(str(v[i]), end=" ", file=stderr)
    print(file=stderr)

    
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
            name = list(range(n))
            while n > 1:
                extA = 0
                extB = 1
                for i in range(2, n):
                    med_name = get_med_of_3(name[i], name[extA], name[extB])
                    if med_name == name[extA]:
                        extA = i
                    if med_name == name[extB]:
                        extB = i
                if   extA >= n-2 and extB < n-2:
                    name[extB] = name[2*n-3 - extA]
                elif extB >= n-2 and extA < n-2:
                    name[extA] = name[2*n-3 - extB]
                else:
                    name[extA] = name[n-1]
                    name[extB] = name[n-2]
                n -= 2
            print(name[0], flush=True)

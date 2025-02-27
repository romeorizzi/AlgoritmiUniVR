#!/usr/bin/env python3
from sys import stderr, setrecursionlimit
setrecursionlimit(10**9)
import random

if __name__ == "__main__":
    T = int(input())
    for t in range(1, 1 + T):
        print(f"#\n# Testcase {t}:", file=stderr)
        n, m = map(int, input().strip().split())
        nei = [ [] for _ in range(n) ]
        for _ in range(m):
            a, b = map(int, input().strip().split())
            nei[a].append(b)
            nei[b].append(a)
        #print(f"{n=}, {m=}, {nei=}", file=stderr)
        sex = [None] * n
        def dfs_is_bipartite(u, C, sex_for_u):
            global sex
            is_bipartite = True
            if sex[u] is not None:
                if sex[u] != sex_for_u:
                    is_bipartite = False
            else:
                sex[u] = sex_for_u
                C.append(u)
                for v in nei[u]:
                    if not dfs_is_bipartite(v, C, 1-sex_for_u):
                        is_bipartite = False
            return is_bipartite
        
        S = []
        CC = []
        for v in range(n):
            if sex[v] is None:
                CC.append([])
                if not dfs_is_bipartite(v, CC[-1], 0):
                    S += CC[-1]
        print(len(S) + 1)
        for v in S:
            print(v, end=" ")
        print(S[random.randrange(len(S))])

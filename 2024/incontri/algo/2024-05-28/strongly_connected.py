#!/usr/bin/python
from sys import stdin, stdout, stderr

n,m = map(int, input().strip().split())
E = []
out_nei = [[] for u in range(n)]
in_nei = [[] for v in range(n)]

for _ in range(m):
    u,v = map(int, input().strip().split())
    assert 0 <= u < n
    assert 0 <= v < n
    E.append([u,v])
    out_nei[u].append(v)
    in_nei[v].append(u)

print(f"{n=}\n{m=}\n{E=}\n{out_nei=}\n{in_nei=}", file=stderr)

order = []
open = [False] * n
def dfs1(v):
    open[v] = True
    for u in in_nei[v]:
        if not open[u]:
            dfs1(u)
    order.append(v)

for v in range(n):
    if not open[v]:
        dfs1(v)

print(f"{open=}\n{order=}", file=stderr)
        
open = [False] * n
C = []
def dfs2(v):
    #print(f"called dfs2({v=})", file=stderr)
    open[v] = True
    C[-1].append(v)
    for u in out_nei[v]:
        if not open[u]:
            dfs2(u)

while len(order) > 0:
    v = order.pop()
    if not open[v]:
        C.append([])
        dfs2(v)

print(f"{open=}\n{C=}", file=stderr)

for c in C:
    print(" ".join(map(str, c)))

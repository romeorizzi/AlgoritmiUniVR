#!/usr/bin/python
from sys import stdin, stdout, stderr

"""
n = int(input())
cost = list(map(int, input().strip().split()))
for _ in range(n-1):
    a,b = map(int, input().strip().split())
    nei[a-1].append(b-1)
    nei[b-1].append(a-1)
"""
with open("input.txt", "r") as fr:
    n = int(fr.readline())
    cost = list(map(int,fr.readline().split()))
    nei = [ [] for _ in range(n) ]
    for _ in range(n-1):
        a,b = map(int,fr.readline().split())
        nei[a-1].append(b-1)
        nei[b-1].append(a-1)

#print(f"{n=}, {cost=}, {nei=}", file = stderr)

def dfs(v,papi):
    """returns Pv, Qv where
          Pv = the minimum cost of a min-cover of the subtree Tv rooted at v
          Qv = the minimum cost of a min-cover of the subtree Tv rooted at v among those min-covers that are required to include node v
       but also an optimal P-solution SPv and an optimal Q-solution SQv
    """
    #print(f" - called dfs({v=}, {papi=})", file = stderr)
    Pv = 0; SPv = []
    Qv = cost[v]; SQv = [v]
    for u in nei[v]:
        if u != papi:
            #print(f"ora esploro il figlio {u=} di {v}", file = stderr)
            pu,qu, spu,squ = dfs(u, v)
            Qv += pu; SQv += spu
            Pv += qu; SPv += squ
    if Pv > Qv:
        Pv = Qv
        SPv = SQv
    return Pv,Qv, SPv,SQv

_,_,SP,_ = dfs(0,0)
"""
print(len(SP))
print(" ".join(map(lambda x : str(x + 1),SP)))
"""
with open("output.txt", "w") as fw:
    fw.write(str(len(SP)) + "\n")
    fw.write(" ".join(map(lambda x : str(x + 1),SP)) + "\n")

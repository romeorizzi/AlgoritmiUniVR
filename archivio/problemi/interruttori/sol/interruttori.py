#!/usr/bin/env python3
from sys import stderr,stdout, argv

def sol_linear_smart(n,S,E):
    vicini = [ [] for _ in range(n) ]    
    for u,v in E:
        vicini[u].append(v)
        vicini[v].append(u)
    INFTY = n + 1; cost = [INFTY] * n; dad = [None] * n
    FIFOq = [None] * n; posR = posW = 0
    for v in S:
        cost[v] = 1; dad[v] = v; FIFOq[posW] = v; posW += 1
    while posW > posR:
        v = FIFOq[posR]; posR += 1
        for u in vicini[v]:
            if cost[u] > cost[v] + 1:
                cost[u] = cost[v] + 1
                dad[u] = v
                FIFOq[posW] = u; posW += 1
    cost_v_max = 0; v_max = None
    for v,c in enumerate(cost):
        if c > cost_v_max:
            cost_v_max = c
            v_max = v
    def path_to(v):
        if dad[v] == v:
            return [v]
        ans = path_to(dad[v])
        ans.append([dad[v], v])
        return ans
        
    return cost[0], path_to(0), v_max, cost_v_max, path_to(v_max), cost


def print_path(path):
    print(path[0])
    for t2_switch in path[1:]:
        print(f"{t2_switch[0]} {t2_switch[1]}")


####################
T = int(input())
for t in range(1, 1 + T):
    n,typ1, typ2 = map(int, input().strip().split())
    S = []
    for _ in range(typ1):
        S.append(int(input()))
    E = []
    for _ in range(typ2):
        E.append(list(map(int, input().strip().split())))
    cost_0, path_to_0, v_max, cost_v_max, path_to_v_max, _ = sol_linear_smart(n,S,E)
    print(cost_0)
    print_path(path_to_0)
    print(f"{v_max} {cost_v_max}")
    print_path(path_to_v_max)

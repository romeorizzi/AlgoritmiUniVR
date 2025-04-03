#!/usr/bin/python
from sys import stdin, stdout, stderr

# DFS su grafo undirected: il codice scritto insieme su https://www.onlinegdb.com/

vicini = {
 "A": ["B","L","D"],
 "B": ["A","D","F","C"],
 "C": ["B","D"],
 "D": ["A","B","C","E"],
 "E": ["D"],
 "F": ["H","B","G"],
 "G": ["I","F","H"],
 "H": ["F","G","O","P"],
 "I": ["G"],
 "L": ["A","N","M"],
 "M": ["N","L"],
 "N": ["M","L"],
 "O": ["H","P"],
 "P": ["O","H"]
}

for v,v_vicini in vicini.items():
    for u in v_vicini:
        print(f"{u=}, {v=}, {v_vicini=}")
        assert (v in vicini[u])

open = {}
close = {} # non necessario ai nostri fini
dad = {}
back_val = {}

time = 0
def dfs(v,v_dad):
    global time
    dad[v] = v_dad
    open[v] = time; time += 1
    back_val[v] = open[v]
    for x in vicini[v]:
        if x in open:
            back_val[v] = min(back_val[v], open[x])
        else:
            back_val[v] = min(back_val[v], dfs(x,v))
    close[v] = time; time += 1
    return back_val[v]
    
dfs("A","A")
print(f"{open=}")
print(f"{close=}")
print(f"{dad=}")
print(f"{back_val=}")

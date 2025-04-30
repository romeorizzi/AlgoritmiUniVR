from queue import Queue 


N = int(input())

L = []
F = []

FI = [[] for _ in range(N)]
E = [0 for _ in range(N)]

for i in range(N):
    _m, l = [int(x) for x in input().split()]
    f = [int(x) for x in input().split()]
    L.append(l)
    F.append(f)

    for fi in f:
        FI[fi].append(i)

activated = 0

queue = Queue()
for i in range(N):
    if L[i] == 0:
        queue.put(i)

while not queue.empty():
    el = queue.get()

    activated += 1
    for fi in FI[el]:
        E[fi] += 1
        if E[fi] == L[fi]:
            queue.put(fi)

print(activated)
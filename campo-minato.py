m,n = map(int,input().strip().split())
M = [] # 1 se è una mina, 0 altrimenti
for i in range(m):
    M.append(list(map(int,input().strip().split())))
    print(f"{M=}")
pd = [[0] * (n+1) for _ in range(m+1) ]

pd[m-1][n-1] = 1 # big bang
for j in range(n-2, -1, -1):
    pd[m-1][j] = 0 if M[m-1][j] else pd[m-1][j+1]

for i in range(m-2,-1,-1):
    for j in range(n-1, -1, -1):
        if not M[i][j]:
            pd[i][j] = pd[i+1][j] + pd[i][j+1]
            
print(f"{pd=}")
print(pd[0][0])


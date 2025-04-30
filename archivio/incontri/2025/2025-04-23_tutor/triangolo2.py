
N = int(input())

T = []
M = []

for i in range(N):
    T.append([int(x) for x in input().split()])

M.append(T[-1])

for i in reversed(range(N-1)):
    Mr = [0 for _ in range(i+1)]
    for j in range(len(Mr)):
        left_idx = j
        right_idx = j + 1
        sol_ij = max(M[-1][left_idx], M[-1][right_idx])
        Mr[j] = sol_ij + T[i][j]
    M.append(Mr)

print(M[-1][0])
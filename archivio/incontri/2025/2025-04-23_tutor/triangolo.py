
N = int(input())

T = []
M = []

for i in range(N):
    T.append([int(x) for x in input().split()])

M.append(T[0])

for i in range(1, N):
    Mr = [0 for _ in range(i+1)]
    for j in range(len(Mr)):
        left_idx = j - 1
        right_idx = j
        sol_ij = 0
        if left_idx >= 0:
            sol_ij = max(sol_ij, M[i - 1][left_idx])
        if right_idx < len(M[i - 1]):
            sol_ij = max(sol_ij, M[i - 1][right_idx])
        Mr[j] = sol_ij + T[i][j]
    M.append(Mr)

print(max(M[-1]))
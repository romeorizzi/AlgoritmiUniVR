
N = int(input())

T = []


for i in range(N):
    T.append([int(x) for x in input().split()])

M = {}

def solve(i, j):
    if i == N - 1:
        return T[i][j]

    if (i, j) in M:
        return M[(i, j)]
    
    left = j
    right = j + 1

    M[(i, j)] = max(solve(i+1, left), solve(i+1, right)) + T[i][j]
    return M[(i, j)]


print(solve(0, 0))
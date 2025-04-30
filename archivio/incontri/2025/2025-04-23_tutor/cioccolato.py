
T = int(input())

for t in range(T):

    input()
    N, M, K = [int(x) for x in input().split()]

    # Convenzione: N >= M
    if N < M:
        N, M = M, N

    D = N - M

    if K <= D:
        sol = M * (N - K)
    else:
        K -= D
        N -= D

        # M = N
        # K > 0
        # Supponiamo che K sia pari
        if K % 2 == 0:
            N -= K // 2
            sol = N * N
        else:
            # K = 1, N = 6, M = 5
            M -= (K // 2) + 1
            N -= K // 2
            sol = N * M
    print(f"Case #{(t+1)}: {sol}")
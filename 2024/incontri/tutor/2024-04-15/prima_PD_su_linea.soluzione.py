

T = int(input())
for t in range(1, 1 + T):
    N = int(input())
    A = list(map(int, input().strip().split()))

    sol = [0 for _ in range(N + 1)]
    sol[N] = 1

    MOD = 1000000007

    # Calcolo il numero di sequenze ammissibili
    for i in reversed(range(N)):
        se_prendo_i = sol[i + 3] if i + 3 <= N else 1
        se_non_prendo_i = sol[i + 1]
        sol[i] = (se_prendo_i + se_non_prendo_i) % MOD
    print(sol[0])

    # Calcolo il valore di una soluzione ottima
    sol = [0 for _ in range(N + 1)]
    sol[N] = 0

    scelta = [None for _ in range(N)]

    num_sol = [0 for _ in range(N + 1)]
    num_sol[N] = 1

    for i in reversed(range(N)):
        se_prendo_i = (sol[i + 3] if i + 3 <= N else 0) + A[i]
        se_non_prendo_i = sol[i + 1]

        n_sol_se_prendo_i = num_sol[i + 3] if i + 3 <= N else 1
        n_sol_se_non_prendo_i = num_sol[i + 1] 

        if se_prendo_i > se_non_prendo_i:
            num_sol[i] = n_sol_se_prendo_i % MOD
        elif se_prendo_i < se_non_prendo_i:
            num_sol[i] = n_sol_se_non_prendo_i % MOD
        else:
            num_sol[i] = (n_sol_se_prendo_i + n_sol_se_non_prendo_i) % MOD

        if se_prendo_i > se_non_prendo_i:
            scelta[i] = "preso"
        else:
            scelta[i] = "non_preso"

        sol[i] = max(se_prendo_i, se_non_prendo_i)

    lista = []
    pos = 0
    while pos < N:
        if scelta[pos] == "preso":
            lista.append(pos)
            pos += 3
        elif scelta[pos] == "non_preso":
            pos += 1 

    print(sol[0])
    print(" ".join([str(idx) for idx in lista]))
    print(num_sol[0])


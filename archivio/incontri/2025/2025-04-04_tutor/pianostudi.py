
input = open("input.txt", "r")
output = open("output.txt", "w")


N = int(input.readline())

corsi = [(0, 0, 0)] * N


for i in range(N):
    da, a, crediti = map(int, input.readline().split())
    corsi[i] = (da, a, crediti)

corsi.sort()

max_crediti = [0] * (N + 1)

def ricerca_binaria_corsi(giorno_dopo_fine):
    low = 0 # corsi[low][0] < giorno_dopo_fine
    high = N # corsi[high][0] >= giorno_dopo_fine oppure la fine dell'array

    while high - low > 1:
        mid = (low + high) // 2
        f_val = corsi[mid][0] >= giorno_dopo_fine

        if f_val:
            high = mid
        else:
            low = mid
    
    return high

for i in reversed(range(N)):
    giorno = corsi[i][0]
    max_crediti_senza_intervallo = max_crediti[i + 1]
    indice_fine_intervallo = ricerca_binaria_corsi(corsi[i][1] + 1)
    max_crediti_con_intervallo = corsi[i][2] + max_crediti[indice_fine_intervallo]
    max_crediti[i] = max(max_crediti_senza_intervallo, max_crediti_con_intervallo)

# print(max_crediti[0])
print(max_crediti[0], file=output)
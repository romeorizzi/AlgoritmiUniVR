from random import randint

N = 100

print(N)

for i in range(N):
    print(" ".join([str(randint(0, 100)) for _ in range(i+1)]))

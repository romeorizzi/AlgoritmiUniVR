#!/usr/bin/python
from sys import stdin, stdout, stderr, argv
import random

n = int(argv[1])
m = int(argv[2])

E = random.sample([(u,v) for u in range(n) for v in range(n) if u != v],m)


print(f"{n} {m}")
for u,v in E:
    print(f"{u} {v}")

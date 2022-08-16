# 10974 모든 순열
from itertools import permutations
n = int(input())
lis = list(i for i in range(1, n+1))

per = permutations(lis, n)

for i in per:
    print(*i)

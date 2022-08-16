# 1182 부분수열의 합
from itertools import combinations

n, s = map(int, input().split())
lis = list(map(int, input().split()))

com_lis = []
for i in range(1, len(lis)+1):
    com_lis += combinations(lis, i)

cnt = 0
for temp in com_lis:
    if sum(temp) == s:
        cnt += 1

print(cnt)

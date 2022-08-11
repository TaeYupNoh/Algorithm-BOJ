# 2108 통계학
import sys
input = sys.stdin.readline

n = int(input())

lis_1 = []
dic = {}
for _ in range(n):
    temp = int(input())
    lis_1.append(temp)
    dic[temp] = dic.get(temp, 0) + 1

print(round(sum(lis_1)/n))
print(sorted(lis_1)[n//2])

freq = 0
for key in dic:
    if dic[key] > freq:
        lis_2 = []
        freq = dic[key]
        lis_2.append(key)
    elif dic[key] == freq:
        lis_2.append(key)

print(lis_2[0] if len(lis_2) == 1 else sorted(lis_2)[1])
print(max(lis_1)-min(lis_1))

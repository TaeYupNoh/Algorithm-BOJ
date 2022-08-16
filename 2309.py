# 2309 일곱 난쟁이
from itertools import combinations

lis = []
for _ in range(9):
    lis.append(int(input()))

com = list(combinations(lis, 7))

answer = []
for temp in com:
    if sum(temp) == 100:
        for x in temp:
            answer.append(x)
        break

answer.sort()
for i in range(len(answer)):
    print(answer[i])

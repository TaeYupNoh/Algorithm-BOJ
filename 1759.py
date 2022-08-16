# 1759 암호 만들기
from itertools import combinations

l, c = map(int, input().split())
lis = list(input().split())

com = list(combinations(lis, l))

com_lis = []
for temp in com:
    case = []
    for x in temp:
        case.append(x)
    case.sort()
    com_lis.append(case)

com_lis.sort()

answer = []
for temp in com_lis:
    a_cnt = 0
    b_cnt = 0
    for i in range(len(temp)):
        if temp[i] in 'aeiou':
            a_cnt += 1
        else:
            b_cnt += 1
    if a_cnt >= 1 and b_cnt >= 2 and temp not in answer:
        answer.append(temp)

for i in range(len(answer)):
    print(*answer[i], sep='')

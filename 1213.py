# 팰린드롬 만들기
from collections import deque
s_lis = list(map(str, input()))
s_dic = {}
for i in s_lis:
    s_dic[i] = s_dic.get(i, 0)+1

answer = deque()

odd_cnt = 0
for i in s_dic:
    if s_dic[i] % 2 == 1:
        odd_cnt += 1
        mid_answer = i
        answer.append(mid_answer)
        s_lis.remove(mid_answer)
    if odd_cnt > 1:
        print('I\'m Sorry Hansoo')
        quit()

s_lis.sort()

while s_lis:
    answer.append(s_lis.pop())
    answer.appendleft(s_lis.pop())

print(*answer, sep='')

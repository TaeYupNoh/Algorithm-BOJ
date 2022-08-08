# 절댓값 힙
# 18 1 -1 0 0 0 1 1 -1 -1 2 -2 0 0 0 0 0 0 0
# -1 1 0 -1 -1 1 1 -2 2 0
# 절댓값 기준으로 작은 값이 출력되는 것까지는 알겠음, 그러면 절댓값이 같을 때 어떻게 기존의 값이 작은 것이 먼저 출력되는 것일까?
# 구글링 결과, 튜플을 heap에 넣을 경우, 첫 번째 기준으로 정렬되고, 같을 경우 두 번째 것의 기준으로 정렬이 됨. (맞는 것 같음.)

import heapq
import sys
input = sys.stdin.readline
lis = []

n = int(input())

for i in range(n):
    temp = int(input())
    temp_tup = (abs(temp), temp)
    if temp == 0:
        if lis:
            print(heapq.heappop(lis)[1])
        else:
            print(0)

    else:
        heapq.heappush(lis, temp_tup)

# 최소 힙

import heapq
import sys
input = sys.stdin.readline
lis = []

n = int(input())

for i in range(n):
    temp = int(input())
    if temp == 0:
        if lis:
            print(heapq.heappop(lis))
        else:
            print(0)

    else:
        heapq.heappush(lis, temp)

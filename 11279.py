# 최대 힙
import heapq
import sys
input = sys.stdin.readline
lis = []

n = int(input())

for i in range(n):
    temp = int(input())
    temp_tup = (-temp, temp)
    if temp == 0:
        if lis:
            print(heapq.heappop(lis)[1])
        else:
            print(0)

    else:
        heapq.heappush(lis, temp_tup)

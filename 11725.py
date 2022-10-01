# 11725 트리의 부모 찾기
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
lis = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    lis[a].append(b)
    lis[b].append(a)

parent = [[] for _ in range(n+1)]


def bfs(a):
    queue = deque([a])
    while queue:
        x = queue.popleft()
        for pre_baby in lis[x]:
            if pre_baby != 1 and not parent[pre_baby]: 
                baby = pre_baby
                parent[baby] = x 
                queue.append(baby)


bfs(1)

for i in range(2,n+1):
    print(parent[i])
# 16928 뱀과 사다리 게임
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
special = [[] for _ in range(101)]

for _ in range(n):
    a,b = map(int,input().split())
    special[a].append(b)
for _ in range(m):
    a,b = map(int,input().split())
    special[a].append(b)

visited = [False for _ in range(101)]
dice = [6,5,4,3,2,1]


def bfs(a,cnt):
    queue = deque([(a,cnt)])
    while queue:
        x, cnt = queue.popleft()
        visited[x] = True
        if x == 100:
            return cnt
        for i in range(6):
            nx = x + dice[i]
            if nx <=100 and visited[nx] == False:
                if len(special[nx]) == 1:
                    visited[special[nx][0]] = True
                    queue.append((special[nx][0],cnt+1))
                else:
                    visited[nx] = True
                    queue.append((nx,cnt+1))


print(bfs(1,0))
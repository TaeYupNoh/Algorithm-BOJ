# 2606 바이러스
from collections import deque

n = int(input())
num = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(num):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n+1)]


def bfs(x):
    queue = deque([x])
    visited[x] = True
    cnt = 0
    while queue:
        a = queue.popleft()
        for temp in graph[a]:
            if visited[temp] == False:
                visited[temp] = True
                queue.append(temp)
                cnt += 1
    return cnt


print(bfs(1))

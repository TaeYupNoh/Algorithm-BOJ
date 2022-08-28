# 11724 연결 요소의 개수
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n+1)]


def bfs(x):
    queue = deque([x])
    visited[x] = True
    while queue:
        temp = queue.popleft()
        for i in graph[temp]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)

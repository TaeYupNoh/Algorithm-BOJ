# 7569 토마토
from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())

graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [0, 0, 0, 0, -1, 1]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, -1, 1, 0, 0]

queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))

day = -1
while queue:
    attempt = len(queue)

    for _ in range(attempt):
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = 2
                queue.append((nx, ny, nz))

    day += 1


for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                quit()
print(day)

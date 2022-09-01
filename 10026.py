# 10026 적록색약
from collections import deque

n = int(input())
lis = [input() for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b):
    if visited[a][b] == True:
        return 0

    else:
        temp = lis[a][b]
        queue = deque([(a, b)])
        visited[a][b] = True
        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and lis[nx][ny] == temp:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
        return 1


# 일반인
visited = [[False for _ in range(n)] for _ in range(n)]
cnt_1 = 0
for i in range(n):
    for j in range(n):
        cnt_1 += bfs(i, j)

# 적록색약
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    if 'G' in lis[i]:
        lis[i] = lis[i].replace('G', 'R')

cnt_2 = 0
for i in range(n):
    for j in range(n):
        cnt_2 += bfs(i, j)


print(cnt_1, cnt_2)

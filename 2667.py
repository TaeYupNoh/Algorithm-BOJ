# 2667 단지번호붙이기
from collections import deque

n = int(input())

graph = [input() for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []


def bfs(a, b):
    queue = deque([(a, b)])
    if graph[a][b] != '1' or visited[a][b] == True:
        return 0, 0
    else:
        visited[a][b] = True
        cnt = 1
        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == '1' and visited[nx][ny] == False:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
        return 1, cnt


num = 0
for i in range(n):
    for j in range(n):
        total, house_num = bfs(i, j)
        num += total
        if house_num > 0:
            answer.append(house_num)
answer.sort()

print(num)
for temp in answer:
    print(temp)

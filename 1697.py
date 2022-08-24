# 1697 숨바꼭질
from collections import deque
n, k = map(int, input().split())
visited = [False for _ in range(100001)]


def bfs(x, c):

    queue = deque([(x, c)])
    while queue:
        a, cnt = queue.popleft()
        if a == k:
            return cnt
        visited[a] = True

        for i in (a-1, a+1, a*2):
            if 0 <= i <= 100000 and visited[i] == False:
                queue.append((i, cnt+1))


print(bfs(n, 0))

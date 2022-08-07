from collections import deque
# 1966 프린터 큐


def printing(queue, m):
    cnt = 0
    while queue:
        pri = max(queue)
        if queue[0][0] == pri[0]:
            check = queue.popleft()
            cnt += 1
            if check[1] == m:
                return cnt
        else:
            queue.append(queue.popleft())


for i in range(int(input())):
    queue = deque()
    n, m = map(int, input().split())
    data = map(int, input().split())
    for i, v in enumerate(data):
        queue.append((v, i))

    print(printing(queue, m))

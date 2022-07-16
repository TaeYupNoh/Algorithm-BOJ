# 1021 회전하는 큐
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
loc = list(map(int, input().split()))
q = [i for i in range(1, n+1)]
cnt = 0

for i in range(len(loc)):
    # 앞으로 회전할 지 뒤로 회전할 지 정하는 if문
    if q.index(loc[i]) < len(q) - q.index(loc[i]):
        while True:
            if q[0] == loc[i]:
                del q[0]
                break
            else:
                q.append(q[0])
                del q[0]
                cnt += 1
    else:
        while True:
            if q[0] == loc[i]:
                del q[0]
                break
            else:
                q.insert(0, q[-1])
                del q[-1]
                cnt += 1

print(cnt)

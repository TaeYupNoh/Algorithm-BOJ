# 11050 이항 계수1
n, k = map(int, input().split())
up = 1
down = 1
for i in range(k):
    up *= n
    n -= 1
    down *= k
    k -= 1

print(up//down)

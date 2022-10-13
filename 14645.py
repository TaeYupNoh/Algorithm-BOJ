# 14645 와이버스 부릉부릉
n, k = map(int, input().split())
cnt = k
for _ in range(n):
    a, b = map(int, input().split())
    cnt += a
    cnt -= b

print('비와이')

# 11549 Identifying tea
find = int(input())
lis = list(map(int, input().split()))

cnt = 0
for temp in lis:
    if temp == find:
        cnt += 1

print(cnt)

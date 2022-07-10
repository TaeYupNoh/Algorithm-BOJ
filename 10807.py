# 10807 개수 세기
n = int(input())
lis = list(map(int, input().split()))
v = int(input())

cnt = 0
for i in lis:
    if i == v:
        cnt += 1

print(cnt)

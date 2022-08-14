# RGB거리
n = int(input())

lis = []
for _ in range(n):
    lis.append(list(map(int, input().split())))

for i in range(1, len(lis)):
    lis[i][0] += min(lis[i-1][1], lis[i-1][2])
    lis[i][1] += min(lis[i-1][0], lis[i-1][2])
    lis[i][2] += min(lis[i-1][0], lis[i-1][1])

print(min(lis[-1]))

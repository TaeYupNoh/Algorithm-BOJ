# 1932 정수 삼각형
n = int(input())

lis = []
for _ in range(n):
    lis.append(list(map(int, input().split())))

if len(lis) > 1:
    lis[1][0] += lis[0][0]
    lis[1][1] += lis[0][0]

for i in range(2, len(lis)):
    for j in range(len(lis[i])):
        if j == 0:
            lis[i][j] += lis[i-1][j]
        elif j == len(lis[i])-1:
            lis[i][j] += lis[i-1][-1]
        else:
            lis[i][j] += max(lis[i-1][j-1], lis[i-1][j])

print(max(lis[-1]))

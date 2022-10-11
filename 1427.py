# 1427 소트인사이드
n = int(input())

lis = []
for temp in str(n):
    lis.append(temp)

print(*sorted(lis, reverse=True), sep='')

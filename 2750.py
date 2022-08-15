# 2750 수 정렬하기
n = int(input())
lis = []
for i in range(n):
    lis.append(int(input()))

lis.sort()
for temp in lis:
    print(temp)

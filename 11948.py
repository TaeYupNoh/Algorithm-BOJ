# 11948 과목선택
import sys
input = sys.stdin.readline

lis = []
for _ in range(4):
    lis.append(int(input()))

lis.sort(reverse=True)
lis = lis[:3]

a = int(input())
b = int(input())

lis.append(max(a,b))

print(sum(lis))
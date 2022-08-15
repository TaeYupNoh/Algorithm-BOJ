# 2579 계단 오르기
n = int(input())
lis = [[]]
for _ in range(n):
    lis.append(int(input()))

d = [[]]

d.append(lis[1])
if len(lis) > 2:
    d.append(lis[1]+lis[2])
if len(lis) > 3:
    d.append(max(lis[1]+lis[3], lis[2]+lis[3]))

for i in range(4, len(lis)):
    d.append(max(lis[i]+d[i-2], lis[i]+lis[i-1]+d[i-3]))

print(d[-1])

# 1912 연속합
n = int(input())
lis = list(map(int, input().split()))

big = 0
temp = 0

for i in lis:
    temp += i
    if temp < 0:
        temp = 0

    big = max(temp, big)

if big == 0:
    print(max(lis))
else:
    print(big)

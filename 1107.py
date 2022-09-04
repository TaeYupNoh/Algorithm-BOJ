# 1107 리모컨
n = int(input())
m = int(input())
if m > 0:
    button = list(map(int, input().split()))
else:
    button = []

answer = abs(100-n)

for temp in range(1000001):
    temp = str(temp)
    for i in range(len(temp)):
        if int(temp[i]) in button:
            break
    else:
        answer = min(answer, abs(int(temp) - n) + len(temp))

print(answer)

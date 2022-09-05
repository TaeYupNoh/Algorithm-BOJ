# 2822 점수 계산
lis = [(int(input()), i+1) for i in range(8)]
lis.sort(reverse=True)

answer = 0
num = []
for temp, idx in lis[:5]:
    answer += temp
    num.append(idx)

num.sort()

print(answer)
print(*num)

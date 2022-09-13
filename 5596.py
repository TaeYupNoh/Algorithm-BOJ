# 5596 시험 점수
temp_1 = 0
temp_2 = 0
lis_1 = list(map(int, input().split()))
lis_2 = list(map(int, input().split()))
for temp in lis_1:
    temp_1 += temp

for temp in lis_2:
    temp_2 += temp

print(max(temp_1, temp_2))

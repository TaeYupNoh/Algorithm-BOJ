# 10039 평균 점수
answer = 0
for _ in range(5):
    temp = int(input())
    if temp < 40:
        temp = 40
    answer += temp

print(answer//5)

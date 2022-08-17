# 10819 차이를 최대로

n = int(input())
m = list(map(int, input().split()))

answer = []
temp = []


def back_tracking(x):
    if x == n:
        answer.append(sum(abs(m[temp[i+1]]-m[temp[i]]) for i in range(n-1)))
        return

    for i in range(n):
        if i not in temp:
            temp.append(i)
            back_tracking(x+1)
            temp.pop()


back_tracking(0)

print(max(answer))

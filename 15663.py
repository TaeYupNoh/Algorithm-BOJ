# 15663 n과 m(9)
import sys
input = sys.stdin.readline

n, m  = map(int,input().split())
lis = list(enumerate(map(int,input().split())))

make = []
answer = []


def backtracking(i):
    if i == m:
        temp = [make[i][1] for i in range(len(make))]
        answer.append(temp)
        return
    for tup in lis:
        if tup not in make:
            make.append(tup)
            backtracking(i+1)
            make.pop()

backtracking(0)

answer.sort()
print(*answer[0])
for i in range(1,len(answer)):
    if answer[i] != answer[i-1]:
        print(*answer[i])
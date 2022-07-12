# 3009 네 번째 점
import sys
input = sys.stdin.readline


x_inp = []
y_inp = []
for i in range(3):
    x, y = (map(int, input().split()))
    x_inp.append(x)
    y_inp.append(y)

for i in range(3):
    if x_inp.count(x_inp[i]) == 1:
        x_res = x_inp[i]
    if y_inp.count(y_inp[i]) == 1:
        y_res = y_inp[i]

print(x_res, y_res)

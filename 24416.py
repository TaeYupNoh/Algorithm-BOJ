# 24416 알고리즘 수업 - 피보나치수1
n = int(input())

# recursion
re_cnt = 0


def fibo(x):
    global re_cnt
    if x == 1 or x == 2:
        re_cnt += 1
        return 1

    else:
        return fibo(x-1) + fibo(x-2)


fibo(n)

# dp
dp_cnt = 0
d = [0] * 41
d[1] = 1
d[2] = 1

for i in range(3, n+1):
    dp_cnt += 1
    d[i] = d[i-1] + d[i-2]

print(re_cnt, dp_cnt)

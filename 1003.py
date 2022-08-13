# 1003 피보나치 함수
t = int(input())

for _ in range(t):
    zero = {0: 1, 1: 0}
    one = {0: 0, 1: 1}

    n = int(input())

    for i in range(2, n+1):
        zero[i] = zero.get(i, 0) + zero[i-1] + zero[i-2]
        one[i] = one.get(i, 0) + one[i-1] + one[i-2]

    print(zero[n], one[n])

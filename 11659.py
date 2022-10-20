# 11659 구간 합 구하기4
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lis = list(map(int, input().split()))
pre_sum = [0] * (n)
result = 0
for i in range(n):
    pre_sum[i] = result + lis[i]
    result += lis[i]
for _ in range(m):
    l_i, r_i = map(int, input().split())
    l_i, r_i = l_i-1, r_i-1
    print(pre_sum[r_i] - pre_sum[l_i] + lis[l_i])

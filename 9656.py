# 9656 돌 게임2
n = int(input())
dp = [0] * 1001

dp[1] = 0
dp[2] = 1
dp[3] = 0

for i in range(4, n+1):
    if dp[i-1] == 0 or dp[i-3] == 0:
        dp[i] = 1
    else:
        dp[i] = 0

print("SK" if dp[n] == 1 else "CY")

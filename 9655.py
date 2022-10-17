# 9655 돌 게임
n = int(input())
dp = [[0] for _ in range(n+1)]
dp[1] = 1
dp[2] = 0
dp[3] = 1
for i in range(4,n+1):
    if dp[i-1] == 1 or dp[i-3] == 1:
        print("CY")
    else:
        print("SG")
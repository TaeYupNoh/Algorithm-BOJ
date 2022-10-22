# 9658 돌 게임4
n = int(input())
dp = [0] * 1001
dp[1] = "CY"
dp[2] = "SK"
dp[3] = "CY"
dp[4] = "SK"
flag = [1,3,4]

for i in range(5,n+1):
    for j in flag:
        if dp[i-j] == 'CY':
            dp[i] = 'SK'
            break
        dp[i] = 'CY'

print(dp[n])
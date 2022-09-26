# 11053 가장 긴 증가하는 부분 수열
n = int(input())
lis = list(map(int,input().split()))
dp = [1 for _ in range(n)]

for temp in range(1,n):
    for compare in range(temp):
        if lis[temp] > lis[compare] and dp[temp] <= dp[compare]:
            dp[temp] = dp[compare] + 1
            
print(max(dp))
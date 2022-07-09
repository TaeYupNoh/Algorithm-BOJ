# 11047 동전0
n, k = map(int, input().split())
coins = []
cnt = 0

while n > 0:
    coins.append(int(input()))
    n -= 1

for coin in sorted(coins, reverse=True):
    cnt += k//coin
    k %= coin

print(cnt)

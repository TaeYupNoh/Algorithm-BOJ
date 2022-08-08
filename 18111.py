# 181111 마인크래프트
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
territory = []

for _ in range(n):
    territory += map(int, input().split())

big = max(territory)
small = min(territory)
_sum = sum(territory)

territory_dic = {}
for height in territory:
    territory_dic[height] = territory_dic.get(height, 0) + 1

time, height = 9999999999, 0
for temp in range(small, big+1):
    if _sum + b >= temp*n*m:
        temp_time = 0
        for key in territory_dic:
            if key < temp:
                temp_time += (temp-key)*territory_dic[key]
            elif key > temp:
                temp_time += (key-temp)*territory_dic[key]*2

        if temp_time <= time:
            time = temp_time
            height = temp

print(time, height)

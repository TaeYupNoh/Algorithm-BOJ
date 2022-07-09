# 11399 ATM
import sys
input = sys.stdin.readline

n = int(input())
time_people = list(map(int, input().split()))

sor_time_people = sorted(time_people)
min_sum = 0
for i in range(1, n+1):
    min_sum += sum(sor_time_people[0:i])

print(min_sum)

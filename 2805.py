# 2805 나무 자르기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lis = list(map(int, input().split()))

first = 1
end = max(lis)

answer = 0
while first <= end:
    mid = (first+end)//2
    take = 0
    for i in lis:
        if mid < i:
            take += i-mid
        if take >= m:
            break
    if take >= m:
        first = mid+1
        answer = mid
    else:
        end = mid-1


print(answer)

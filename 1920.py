# 1920 수 찾기
import sys
input = sys.stdin.readline

n = int(input())
n_lis = list(map(int, input().split()))
n_lis.sort()


def b_s(x):
    first = 0
    end = n-1
    while first <= end:
        mid = (first+end)//2
        if x > n_lis[mid]:
            first = mid+1
            continue
        if x < n_lis[mid]:
            end = mid-1
            continue
        if x == n_lis[mid]:
            return 1
    return 0


m = int(input())
m_lis = list(map(int, input().split()))

for test in m_lis:
    print(b_s(test))

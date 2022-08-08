# 10816 숫자 카드2
# get 예시로 사용 가능!
import sys
input = sys.stdin.readline

n = int(input())
n_lis = list(map(int, input().split()))
n_dic = {}
for temp in n_lis:
    n_dic[temp] = n_dic.get(temp, 0) + 1

n_tup = list((n_dic.items()))
n_tup.sort()


def b_s(x):
    first = 0
    end = len(n_tup)-1
    while first <= end:
        mid = (first+end)//2
        if n_tup[mid][0] == x:
            return n_tup[mid][1]
        elif n_tup[mid][0] < x:
            first = mid+1
            continue
        elif n_tup[mid][0] > x:
            end = mid-1
            continue
    return 0


m = int(input())
m_lis = list(map(int, input().split()))
for temp in m_lis:
    print(b_s(temp), end=' ')

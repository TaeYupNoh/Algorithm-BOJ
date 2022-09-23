# 9375 패션왕 신해빈
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    dic = {}
    m = int(input())
    for _ in range(m):
        a,b =input().split()
        dic[b] = dic.get(b,0) +1
    answer = 1
    for i in dic.values():
        answer *= i+1
    answer -= 1
    
    print(answer)
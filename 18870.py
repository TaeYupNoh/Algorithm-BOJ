# 18870 좌표 압축
import sys
input=sys.stdin.readline

n=int(input())
before_lis=list(map(int,input().split()))
after_lis=sorted(list(set(before_lis)))
dic={after_lis[i]:i for i in range(len(after_lis))}

Results = []
for dic_key in before_lis:
    print(dic[dic_key], end=' ')

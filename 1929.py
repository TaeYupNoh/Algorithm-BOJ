# 1929 소수 구하기
import sys
input=sys.stdin.readline

m,n=map(int,input().split())

def prime_num(x,y):
    for i in range(x,y+1):
        if i == 1:
            continue
        elif i == 2 or i == 3 or i==5:
            print(i)
            continue
        elif i%2 == 0 or i%3 == 0 or i%5==0:
            continue
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                break
        else:
            print(i)

prime_num(m,n)

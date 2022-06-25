# 직각삼각형
import sys

def right_tri_check(a,b,c):
    if a**2+b**2 == c**2:
        print("right") 
    else :
        print("wrong") 
        
lis=[]
while True:
    a,b,c=map(int,sys.stdin.readline().split())
    lis.append(sorted((a,b,c)))
    if [0,0,0] in lis:
        lis.remove([0,0,0])
        break

[right_tri_check(i[0],i[1],i[2]) for i in lis]


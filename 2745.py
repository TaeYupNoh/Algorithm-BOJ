# 2745 진법 변환
# int() 함수 사용 풀이
n,b=input().split()
print(int(n,int(b)))

################################
# 노가다 멍청 풀이
def alpha_changer(x):
    return ord(x)-55

n,b=input().split()
b=int(b)

length=len(n)
result=0
for i in n:
    if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        result += b**(length-1)*alpha_changer(i)
        length-=1
    else :
        result += b**(length-1)*int(i)
        length-=1
print(result)

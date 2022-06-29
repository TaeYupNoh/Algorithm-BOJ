# 더하기 사이클
n=int(input())

def func(x):
    global new_n
    a=x//10
    b=x%10
    c=a+b
    new_n=b*10+c%10
    return new_n

func(n)
cnt=1
while n != new_n:
    func(new_n)
    cnt+=1

print(cnt)

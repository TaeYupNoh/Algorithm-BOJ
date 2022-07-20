# 11005 진법 변환 2
n,b=map(int,(input().split()))

chunk = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result=[]
while True:
    result.append(chunk[n%b])
    n=n//b
    if n==0:
        break
print(''.join(result[::-1]))

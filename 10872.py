# 10872 팩토리얼
n=int(input())

def facto(x):
    if x == 0:
        return 1
    return x*facto(x-1)

print(facto(n))
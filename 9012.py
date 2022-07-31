# 9012 괄호
n = int(input())


def checker(x):
    if x[0] == ')' or x[-1] == '(':
        return 'NO'
    cnt = 0
    for s in x:
        if s == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                return 'NO'
    if cnt > 0:
        return 'NO'
    elif cnt == 0:
        return 'YES'


for _ in range(n):
    print(checker(input()))

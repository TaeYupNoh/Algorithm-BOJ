# 1874 스택 수열
n = int(input())

stack = []


cnt = 1
answer = []
for _ in range(n):
    _input = int(input())

    while _input >= cnt:
        stack.append(cnt)
        cnt += 1
        answer.append('+')

    if stack[-1] == _input:
        stack.pop()
        answer.append('-')
    else:
        answer.append('NO')

if 'NO' in answer:
    print('NO')
    quit()

for i in answer:
    print(i)

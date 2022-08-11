# 4949 균형잡힌 세상
while True:
    stack = []
    success = True
    _input = input()
    for temp in _input:
        if temp == '(' or temp == '[':
            stack.append(temp)

        elif temp == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                success = False
                break

        elif temp == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                success = False
                break

    if _input == '.':
        break

    if success and not stack:
        print('yes')
    else:
        print('no')

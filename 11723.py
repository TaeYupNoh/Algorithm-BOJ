# 11723 집합
import sys
input = sys.stdin.readline

m = int(input())

bit = 0
for _ in range(m):
    cmd = input().split()
    if len(cmd) == 2:
        num = int(cmd[1]) - 1

    if cmd[0] == 'add':
        bit |= (1 << num)

    elif cmd[0] == 'remove':
        bit &= ~(1 << num)

    elif cmd[0] == 'check':
        if bit & (1 << num) == 0:
            print(0)
        else:
            print(1)

    elif cmd[0] == 'toggle':
        bit = bit ^ (1 << num)

    elif cmd[0] == 'all':
        bit = (1 << 20) - 1

    elif cmd[0] == 'empty':
        bit = 0

# 15829 Hashing

alp = 'abcdefghijklmnopqrstuvwxyz'

alp_dic = {v: i+1 for i, v in enumerate(alp)}

l = int(input())
inp = input()

answer = 0
for i in range(l):
    for key in alp_dic:
        if key == inp[i]:
            answer += alp_dic[key]*31**i

print(answer % 1234567891)

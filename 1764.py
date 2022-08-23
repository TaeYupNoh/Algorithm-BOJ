# 1764 듣보잡
n, m = map(int, input().split())
listen = [input() for _ in range(n)]
look = [input() for _ in range(m)]

dic = {}
for person in listen:
    dic[person] = dic.get(person, 0) + 1
for person in look:
    dic[person] = dic.get(person, 0) + 1

answer = []

for key in dic.keys():
    if dic[key] == 2:
        answer.append(key)

print(len(answer))
answer.sort()
for person in answer:
    print(person)

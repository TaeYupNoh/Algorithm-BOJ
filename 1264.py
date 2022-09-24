# 1264 모음의 개수

word = ['a','e','i','o','u']
while True:
    cnt = 0
    words = input().lower()
    if words == '#':
        break
    for temp in words:
        if temp in word:
            cnt+=1

    print(cnt)

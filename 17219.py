# 17219 비밀번호 찾기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}

for i in range(n):
    temp = list(input().split())
    dic[temp[0]] = dic.get(temp[0], '') + temp[1]

for _ in range(m):
    print(dic[input().rstrip()])

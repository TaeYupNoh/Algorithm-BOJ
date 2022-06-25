# 나이순 정렬
import sys

n = int(sys.stdin.readline())

lis=[]
for i in range(n):
    age,name=sys.stdin.readline().split()
    age=int(age)
    lis.append((age,name))

[print(i[0],i[1]) for i in sorted(lis, key=lambda x:x[0])]


# 딕셔너리로 풀면 동명이인 처리가 안 됨..
# import sys

# n = int(sys.stdin.readline())

# dic={}
# for i in range(n):
#     a,b=sys.stdin.readline().split()
#     dic[b]=int(a)


# [print(key,"",value) for (value, key) in sorted(dic.items(), key=lambda x:x[1])]
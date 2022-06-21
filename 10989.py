import sys

a=int(sys.stdin.readline())
list=[0]*10001

for i in range(a): # input 대신 input 받은 것
    list[int(sys.stdin.readline())] += 1 
# 입력 받은 것이 리스트의 인덱스 값과 일치하면 1 더하기

for i in range(10001): # 리스트 0~10001 (0은 없으니 실질적으로 1부터)
    if list[i] != 0:
        for j in range(list[i]): # 리스트 그 인덱스의 값만큼 반복하도록
            print(i)



# 메모리 초과 난 풀이

#a=int(input())

#b=[]
#while a >0:
#    b.append(int(input()))
#    a=a-1
#for i in sorted(b):
#    print(i)
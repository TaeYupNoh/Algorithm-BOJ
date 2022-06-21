import sys

a=int(sys.stdin.readline())

queue=[]

for i in range(a):
    cmd=sys.stdin.readline().split()

    if cmd[0] == "push": 
        queue.insert(0,cmd[1])
        
    elif cmd[0] == "pop":
        if len(queue) != 0:
            print(queue.pop()) 
        else : print(-1)
# 선입선출 이므로, 들어온건 맨 앞에, 
# 나가는건 pop이용해 맨 뒤에 것 부터

    elif cmd[0] == "size":
        print(len(queue))

    elif cmd[0] == "empty":
        if len(queue) == 0:
            print(1)
        else : print(0)

    elif cmd[0] == "front":
        if len(queue) == 0:
            print(-1)
        else: 
            print(queue[len(queue)-1]) 
# 이 리스트 queue에서는 맨 뒤가 큐의 맨 앞

    elif cmd[0] == "back":
        if len(queue) == 0 :
            print(-1)
        else :
            print(queue[0])

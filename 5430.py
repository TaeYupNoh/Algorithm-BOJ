# 5430 AC
import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    p = list(sys.stdin.readline().rstrip())
    n= int(sys.stdin.readline())
    num_list = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    
    if n == 0:
        num_list = deque()

    error = False
    reverse = False
    for i in p:
        if i == "R":
            if reverse:
                reverse = False
            else:
                reverse = True

        else: 
            if num_list:
                if reverse:
                    num_list.pop()
                else:
                    num_list.popleft()
            else:
                error = True
                break
      
    if error:
        print("error")
    elif reverse:
        num_list.reverse()
        print("["+",".join(num_list)+"]")
    else:
        print("["+",".join(num_list)+"]")
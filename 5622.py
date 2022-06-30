s=input()

time=0
alp='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in s: 
    if i in alp[:3]:
        time+=3
    elif i in alp[3:6]:
        time+=4
    elif i in alp[6:9]:
        time+=5
    elif i in alp[9:12]:
        time+=6
    elif i in alp[12:15]:
        time+=7
    elif i in alp[15:19]:
        time+=8
    elif i in alp[19:22]:
        time+=9
    elif i in alp[22:26]:
        time+=10

print(time)
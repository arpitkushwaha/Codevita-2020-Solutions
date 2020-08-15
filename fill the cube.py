import math
t=int(input())
lt=[]
count=0
for i in range(t):
    lt.append(list(map(str,input().split())))
for j in range(t):
    for k in range(t):
        if lt[j][k]=='D':
            count+=1
 
print(math.floor(math.sqrt(count)))
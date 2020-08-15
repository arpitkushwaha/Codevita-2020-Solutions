import math
n_arpit=int(input())
l_arpit=[]
c_arpit=0
for i_arpit in range(n_arpit):
    l_arpit.append(list(map(str,input().split())))
for j_arpit in l_arpit:
    s = str(j_arpit)
    c_arpit+=s.count('D')
        
print(math.floor(math.sqrt(c_arpit)))
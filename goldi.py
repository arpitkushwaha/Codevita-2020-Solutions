no = int(input())
b, h = map(int, input().split())
l = list(map(int, input().split()))
max = 0
area = 0
for i in range(no):
    area += l[i]
    sum = 0
    j = i
    while(j >= 0):
        if(l[j] >= l[i]):
            sum += l[i]
        else:
            break
        j = j-1
    j = i+1
    while(j < no):
        if(l[j] >= l[i]):
            sum += l[i]
        else:
            break
        j = j+1
    if sum > max:
        max = sum
ans = ((area-max)*b*h) % 1000000007
print(ans)

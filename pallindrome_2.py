def pali(st):
    n = len(st)
    if n==1:
        return True
    for i in range(n//2):
        if st[i] != st[-i-1]:
            return False
    return True
st = input()
def ans(st):
    for a in range(1,len(st)-2):
        if pali(st[:a]):
            for b in range(a+1,len(st)):
                if pali(st[a:b]) and pali(st[b:]):
                    print(st[:a])
                    print(st[a:b])
                    print(st[b:])
                    return
    print("not possible")

ans(st)
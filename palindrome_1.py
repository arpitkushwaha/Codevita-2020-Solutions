def checkPalindrome(w):
    if(w == w[::-1]):
        return True
    else:
        return False


def CheckAnswer(a, b, c):
    ONE_1 = checkPalindrome(a)
    TWO_2 = checkPalindrome(b)
    THREE_3 = checkPalindrome(c)

    if(ONE_1 and TWO_2 and THREE_3):
        return True
    else:
        return False


def main():
    s = input()
    r = len(s)
    for i in range(r-2):
        for j in range(r-2-i):
            one = s[0:i+1]
            two = s[i+1:j+i+2]
            three = s[j+i+2:]
            if(CheckAnswer(one, two, three) == True):
                return(one, two, three)
    return(["Impossible"])

print(*main(), sep='\n')

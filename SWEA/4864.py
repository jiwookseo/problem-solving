# 4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교

# BF
for tc in range(1,int(input())+1):
        a=input()
        b=input()
        la=len(a)
        lb=len(b)
        for i in range(lb-la+1):
            for j in range(la):
                if a[j]==b[i+j]:
                    check=1
                else:
                    check=0
                    break
            if check==1:
                print(f"#{tc} 1")
                break
        if check==0:
            print(f"#{tc} 0")

"""
class pattern:
    def __init__(self, string):
        self.string=string
        self.lenStr=len(self.string)

    def shift(self, char):
        for i in range(self.lenStr)[::-1]:
            if char==self.string[i]:
                return self.lenStr-1-i
        return self.lenStr

for tc in range(1,int(input())+1):
    a=input()
    b=input()
    la=len(a)
    lb=len(b)
    patt=pattern(a)
    i=la-1
    while(i<=lb-1):
        result=1
        check=False
        for temp in range(la):
            if a[la-1-temp]!=b[i-temp]:
                result*=0
                break
            check=True
        if result==1:
            break
        if check:
            i+=la-1-temp
        else:
            result=0
            i+=patt.shift(b[i])
    print(f"#{tc} {result}")

"""
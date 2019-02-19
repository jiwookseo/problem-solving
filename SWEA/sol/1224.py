# 1224. [S/W 문제해결 기본] 6일차 - 계산기3 D4
class stack:
    def __init__(self, size, init=None):
        self.size=size
        self.top=-1
        self.storage=[init]*size

    def push(self, item):
        self.top+=1
        self.storage[self.top]=item

    def pop(self):
        temp=self.storage[self.top]
        self.top-=1
        return temp
    def toptem(self):
        return self.storage[self.top]

def step1(string):
    result=""
    for t in string:
        if t.isnumeric():
            result+=t
        elif t=="(":
            s.push(t)
        elif t==")":
            while(True):
                temp=s.pop()
                if temp=="(":
                    break
                else:
                    result+=temp
        elif t=="+" or t=="-":
            while s.toptem()!="(" and s.top!=-1:
                result+=s.pop()
            s.push(t)
        elif t=="*" or t=="/":
            while (s.toptem()=="*" or s.toptem()=="/") and s.top!=-1:
                result+=s.pop()
            s.push(t)
    while (s.top!=-1):
        result+=s.pop()
    return result

def step2(string):
    for t in string:
        if t.isnumeric():
            s.push(int(t))
        else:
            b=s.pop()
            a=s.pop()
            if t=="+":
                temp=a+b
            elif t=="-":
                temp=a-b
            elif t=="*":
                temp=a*b
            elif t=="/":
                temp=a/b
            s.push(temp)
    return s.pop()

for tc in range(1,11):
    n=int(input())
    string=input()
    s=stack(n)
    result=step1(string)
    s=stack(len(result))
    result=step2(result)
    print(f"#{tc} {result}")
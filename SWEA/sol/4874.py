# 4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth D2

class stack():
    def __init__(self, size, init=None):
        self.storage=[init]*size
        self.init=init
        self.top=-1
    def push(self,item):
        self.top+=1
        self.storage[self.top]=item
    def pop(self):
        temp=self.storage[self.top]
        self.storage[self.top]=self.init
        self.top-=1
        return temp

for tc in range(1,int(input())+1):
    str_list=input().split()
    s=stack(256)
    check=1
    for i in str_list:
        if i.isnumeric(): # 피연산자
            s.push(int(i))
        elif i!=".": # 연산자
            if s.top<1:
                check=0
                break
            else:
                b=s.pop()
                a=s.pop()
            if i=="+":    
                s.push(a+b)
            elif i=="-":
                s.push(a-b)
            elif i=="*":
                s.push(a*b)
            elif i=="/":
                s.push(a//b)
    if check and s.top==0:
        result=s.pop()
    else:
        result="error"
    print(f"#{tc} {result}")
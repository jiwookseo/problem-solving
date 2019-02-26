# 5097. [파이썬 S/W 문제해결 기본] 6일차 - 회전 D2

class Queue:
    def __init__(self,size,init=None):
        self.size=size
        self.init=init
        self.storage=[self.init]*self.size
        self.front=0
        self.rear=0
    def enQueue(self,item):
        self.rear=(self.rear+1)%self.size
        self.storage[self.rear]=item
    def deQueue(self):
        self.front=(self.front+1)%self.size
        return self.storage[self.front]

for tc in range(1,int(input())+1):
    a=input().split()
    n,m=int(a[0]),int(a[1])
    nl=input().split()
    q=Queue(n+1)
    for i in nl:
        q.enQueue(i)
    for i in range(m):
        q.enQueue(q.deQueue())
    print(f"#{tc} {q.deQueue()}")

# for tc in range(1,int(input())+1):
#     a=input().split()
#     n,m=int(a[0]),int(a[1])
#     nl=input().split()
#     print(f"#{tc} {nl[m%n]}")
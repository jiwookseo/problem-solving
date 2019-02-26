# 5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기 D3
class Queue:
    def __init__(self,size,init=None):
        self.front=0
        self.rear=0
        self.init=init
        self.size=size
        self.storage=[self.init]*self.size
    def isEmpty(self):
        return self.rear==self.front
    def enQueue(self,item):
        self.rear=(self.rear+1)%self.size
        self.storage[self.rear]=item
    def deQueue(self):
        if self.isEmpty():
            return False
        self.front=(self.front+1)%self.size
        return self.storage[self.front]

for tc in range(1,int(input())+1):
    i=input().split()
    n,m=int(i[0]),int(i[1])
    chz=input().split()
    piz=[[i+1,int(chz[i])] for i in range(m)][::-1]
    q=Queue(n+1)
    for i in range(n):
        q.enQueue(piz.pop())
    while(not q.isEmpty()):
        tp=q.deQueue()
        tp[1]=tp[1]//2
        if tp[1]==0:
            if len(piz)!=0:
                q.enQueue(piz.pop())
        else:
            q.enQueue(tp)
    print(f"#{tc} {tp[0]}")
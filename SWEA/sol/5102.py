# 5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리 D2

class Queue:
    def __init__(self,size,init=None):
        self.size=size
        self.init=init
        self.front=-1
        self.rear=-1
        self.storage=[self.init]*self.size
    def enQueue(self,item):
        self.rear+=1
        self.storage[self.rear]=item
    def deQueue(self):
        self.front+=1
        return self.storage[self.front]
    def isEmpty(self):
        return self.front==self.rear

def next(node,sum):
    global G,v,g,q
    for i in range(1,v+1):
        if G[node][i]:
            if i==g:
                return True
            q.enQueue((i,sum+1))
            G[node][i]=False
            G[i][node]=False
    return False

for tc in range(1,int(input())+1):
    i=input().split()
    v,e=int(i[0]),int(i[1])
    G=[[False]*(v+1) for _ in range(v+1)]
    for _ in range(e):
        i=list(map(int,input().split()))
        G[i[0]][i[1]],G[i[1]][i[0]]=True,True
    i=input().split()
    s,g=int(i[0]),int(i[1])
    q=Queue(e)
    q.enQueue((s,0))
    result=0
    while(not q.isEmpty()):
        tv=q.deQueue()
        if next(*tv):
            result=tv[1]
            break
    print(f"#{tc} {result}")
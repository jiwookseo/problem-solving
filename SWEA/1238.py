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

for tc in range(1,11):
    i=input().split()
    index,s=int(i[0])//2,int(i[1])
    data=list(map(int,input().split()))
    n=max(data)
    G=[[] for _ in range(n+1)]
    visited=[False]*(n+1)
    for _ in range(index):
        t=data.pop()
        f=data.pop()
        G[f].append(t)
    q=Queue(n+1)
    v=s
    count=0
    q.enQueue((count,v))
    result=[0]
    visited[v]=True
    while(not q.isEmpty()):
        count,v=q.deQueue()
        if result!=[] and result[0]!=count:
            result=[count,v]
        else:
            result.append(v)
        count+=1
        for i in G[v]:
            if not visited[i]:
                visited[i]=True
                q.enQueue((count,i))
    print(f"#{tc} {max(result[1:])}")
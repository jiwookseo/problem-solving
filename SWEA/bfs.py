class Queue:
    def __init__(self,size,init=None):
        self.init=init
        self.size=size
        self.storage=[self.init]*self.size
        self.front=-1
        self.rear=-1
    def enQueue(self,item):
        self.rear+=1
        self.storage[self.rear]=item
    def deQueue(self):
        self.front+=1
        return self.storage[self.front]
    def isEmpty(self):
        return self.front==self.rear
result=[]
def bfs(G,v):
    visited=[0]*n
    q=Queue(n**2)
    q.enQueue(v)
    while(not q.isEmpty()):
        t=q.deQueue()
        if not visited[t]:
            visited[t]=True
            result.append(str(t))
        for i in G[t]:
            if not visited[i]:
                q.enQueue(i)
# n=8
# G=[[0,1,2],[0,3,4],[0,5],[1],[1,6],[2,7],[4],[5]]
# ans : 0-1-2-3-4-5-6-7

# n=9
# G=[[1,2,3],[0,4,5],[0],[0,6,7,8],[1],[1],[3],[3],[3]]
# ans : 0-1-2-3-4-5-6-7-8

string="1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7".split(',')
i=0
ls=len(string)
n=8
G=[[] for _ in range(n)]
while(1):
    G[int(string[i])].append(int(string[i+1]))
    G[int(string[i+1])].append(int(string[i]))
    i+=2
    if i>=ls:
        break
# ans : 1-2-3-4-5-7-6

bfs(G,1)
print("-".join(result))
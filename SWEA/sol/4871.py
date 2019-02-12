class stack:
    def __init__(self, size, init=None):
        self.top_index=-1
        self.size=size
        self.init=init
        self.storage=[init]*size

    def push(self, item):
        if self.top_index==self.size-1:
            print("OverflowError")
            return
        self.top_index+=1
        self.storage[self.top_index]=item
        return True

    def pop(self):
        if self.top_index==-1:
            print("UnderflowError")
            return "UnderflowError"
        pop_item=self.storage[self.top_index]
        self.storage[self.top_index]=self.init
        self.top_index-=1
        return pop_item
    
    def isEmpty(self):
        return True if self.top_index==-1 else False
    
    def top(self):
        return self.storage[self.top_index] if self.isEmpty() else "EmptyStack"

class node:
    def __init__(self):
        self.near=[]
    def add(self,item):
        if not self.check(item):
            self.near.append(item)
    def check(self, item):
        for i in self.near:
            if i==item:
                return True
        return False

for tc in range(1,int(input())+1):
    i=input().split()
    maximum,lines=int(i[0]),int(i[1])
    nodes=[node() for _ in range(maximum+1)]
    temp1,temp2=0,0
    for _ in range(lines):
        i=input().split()
        s,e=int(i[0]),int(i[1])
        nodes[s].add(e)

    i=input().split()
    start,end=int(i[0]),int(i[1])
    visited=[False for _ in range(maximum+1)]
    s=stack(maximum+1)
    result=[]
    v=start
    visited[v]=True
    result=0

    while(True):
        if nodes[v].near!=[]:
            s.push(v)
            minimum=nodes[v].near[0]
            index=0
            for i in range(len(nodes[v].near)):
                if nodes[v].near[i]==end:
                    result=1
                    break
                if minimum>nodes[v].near[i]:
                    minimum=nodes[v].near[i]
                    index=i
            del nodes[v].near[index]
            v=minimum
        else:
            if s.isEmpty():
                break
            else:
                v=s.pop()
    print(f"#{tc} {result}")
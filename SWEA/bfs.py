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

input_list=list(map(int,input().split(",")))
# 1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7
maximum=0
for i in input_list:
    if i>maximum:
        maximum=i

nodes=[node() for _ in range(maximum+1)]
temp1,temp2=0,0
for i in range(len(input_list)):
    if i%2:
        temp2=input_list[i]
        nodes[temp1].add(temp2)
        nodes[temp2].add(temp1)
    else:
        temp1=input_list[i]

start=int(input())
visited=[False for _ in range(maximum+1)]
s=stack(maximum+1)
result=[]
v=start
visited[v]=True
result.append(str(v))

while(True):
    temp=[]
    for i in nodes[v].near:
        if not visited[i]:
            temp.append(i)
    if temp!=[]:
        s.push(v)
        minimum=temp[0]
        for i in temp:
            if minimum>i:
                minimum=i
        v=minimum
        visited[v]=True
        result.append(str(v))
    else:
        if s.isEmpty():
            break
        else:
            v=s.pop()
print("-".join(result))
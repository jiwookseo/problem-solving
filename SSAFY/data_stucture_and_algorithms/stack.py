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
    
def check(item):
    if item=="(":
        return 1
    elif item==")":
        return 2
    else:
        return 0

s=stack(100)
result=True
for item in input():
    if check(item)==1:
        s.push(item)
    elif check(item)==2:
        if s.pop()=="UnderflowError":
            result=False
            break
if result:
    result=s.isEmpty()
print(result)
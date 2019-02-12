 # 4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사 D2

class stack:
    def __init__(self, size, init=None):
        self.top_index=-1
        self.size=size
        self.init=init
        self.storage=[init]*size

    def push(self, item):
        if self.top_index==self.size-1:
            return
        self.top_index+=1
        self.storage[self.top_index]=item
        return True

    def pop(self):
        if self.top_index==-1:
            return "UnderflowError"
        pop_item=self.storage[self.top_index]
        self.storage[self.top_index]=self.init
        self.top_index-=1
        return pop_item
    
    def isEmpty(self):
        return 1 if self.top_index==-1 else 0
    
    def top(self):
        return self.storage[self.top_index] if self.isEmpty() else "EmptyStack"
    
def check(item):
    if item=="(":
        return 1
    elif item==")":
        return 2
    elif item=="{":
        return 3
    elif item=="}":
        return 4
    else:
        return 0

for tc in range(1,int(input())+1):
    s=stack(100)
    result=1
    for item in input():
        if check(item)==1:
            s.push(item)
        elif check(item)==3:
            s.push(item)
        elif check(item)==2:
            top=s.pop()
            if top=="UnderflowError" or top=="{":
                result=0
                break
        elif check(item)==4:
            top=s.pop()
            if top=="UnderflowError" or top=="(":
                result=0
                break
    if result:
        result=s.isEmpty()
    del s
    print(f"#{tc} {result}")
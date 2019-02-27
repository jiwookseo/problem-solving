class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

class LinkedQueue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enQueue(self,data):
        node=Node(data)
        if self.isEmpty():
            self.front=node
            self.rear=node
        else :
            p=self.front
            while(p!=None):
                if p.data<data:
                    p=p.next
                else:
                    break
            if p==self.front:
                node.next=self.front
                self.front.prev=node
                self.front=node
            elif p==None:
                self.rear.next=node
                self.rear=node
            else:
                p.prev.next=node
                node.prev=p.prev
                node.next=p
                p.prev=node

    def deQueue(self):
        if self.isEmpty():
            print("Empty Queue")
            return
        result=self.front.data
        self.front=self.front.next
        if self.isEmpty():
            self.rear=None
        else:
            self.front.prev=None
        return result
        
    def isEmpty(self):
        return self.front==None

lq=LinkedQueue()
for i in range(5,0,-1):
    lq.enQueue(i)
for i in range(6,11):
    lq.enQueue(i)
while(not lq.isEmpty()):
    print(lq.deQueue())
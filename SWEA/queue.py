class linearQueue:
    def __init__(self,size,init=None):
        self.size=size
        self.init=init
        self.front=-1
        self.rear=-1
        self.storage=[init]*self.size

    def enQueue(self,item):
        if not self.isFull():
            self.rear+=1
            self.storage[self.rear]=item
        else:
            print("Queue is full")

    def deQueue(self):
        if not self.isEmpty():
            self.front+=1
            temp=self.storage[self.front]
            self.storage[self.front]=self.init
            return temp
        else:
            print("Queue is Empty")

    def isEmpty(self):
        return self.front==self.rear

    def isFull(self):
        return self.rear==(self.size-1)

    def Qpeek(self):
        return self.storage[self.front]

class CircleQueue:
    def __init__(self,size,init=None):
        self.size=size
        self.init=init
        self.front=0
        self.rear=0
        self.storage=[init]*self.size

    def enQueue(self,item):
        if not self.isFull():
            self.rear=(self.rear+1)%self.size
            self.storage[self.rear]=item
        else:
            print("Queue is full")

    def deQueue(self):
        if not self.isEmpty():
            self.front=(self.front+1)%self.size
            temp=self.storage[self.front]
            self.storage[self.front]=self.init
            return temp
        else:
            print("Queue is Empty")

    def isEmpty(self):
        return self.front==self.rear

    def isFull(self):
        return (self.rear+1)%self.size==self.front

    def Qpeek(self):
        return self.storage[self.front]

class Node:
    def __init__(self,item):
        self.item=item
        self.next=None

    def setNext(self,node):
        self.next=node

class LinkedQueue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enQueue(self,item):
        node=Node(item)
        if self.isEmpty():
            self.front=node
        else :
            self.rear.setNext(node)
        self.rear=node

    def deQueue(self):
        if self.isEmpty():
            print("Empty Queue")
            return
        result=self.front.item
        self.front=self.front.next
        if self.isEmpty():
            self.rear=None
        return result
        
    def isEmpty(self):
        return self.front==None

q=LinkedQueue()
a=1
m=1000
while(m>0):
    if q.isEmpty():
        q.enQueue((a,1))
    ta,tm=q.deQueue()
    m-=tm
    q.enQueue((ta,tm+1))
    a+=1
    q.enQueue((a,1))
    print(ta,tm)
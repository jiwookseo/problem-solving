class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

class DoubleLinkedList:
    def __init__(self):
        self.head=None

    def addtoFirst(self,data):
        self.head=Node(data,None,self.head)

    def add(self,index,data):
        pre=self.get(index-1)
        nex=self.get(index)
        if pre==None:
            print('index error')
        else:
            pre.next=Node(data,pre,pre.next)
            if nex!=None:
                nex.prev=pre.next

    def addtoLast(self,data):
        if self.head==None:
            self.addtoFirst(data)
        else:
            p=self.head
            while(p.next!=None):
                p=p.next
            p.next=Node(data,p,None)

    def delete(self,index):
        if index==0:
            self.head=self.head.next
            self.head.prev=None
        else:
            pre=self.get(index-1)
            if pre==None or pre.link==None:
                print('index error')
            else:
                pre.next=pre.next.next
                pre.next.prev=pre
                
    def get(self,index):
        tn=self.head
        for _ in range(index):
            tn=tn.next
            if tn==None:
                return None
        return tn

l=DoubleLinkedList()
l.addtoFirst(1)
print(l.get(0).data)
l.add(1,2)
l.add(2,3)
print(l.get(1).data)
print(l.get(1).prev)
print(l.get(1).next)
l.delete(0)
print(l.get(0).data)
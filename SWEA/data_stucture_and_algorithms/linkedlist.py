class Node:
    def __init__(self,data,link=None):
        self.data=data
        self.link=link

class LinkedList:
    def __init__(self):
        self.head=None

    def addtoFirst(self,data):
        self.head=Node(data,self.head)

    def add(self,index,data):
        pre=self.get(index-1)
        if pre==None:
            print('index error')
        else:
            pre.link=Node(data,pre.link)

    def addtoLast(self,data):
        if self.head==None:
            self.addtoFirst(data)
        else:
            p=self.head
            while(p.link!=None):
                p=p.link
            p.link=Node(data,None)

    def delete(self,index):
        if index==0:
            self.head=self.head.link
        else:
            pre=self.get(index-1)
            if pre==None or pre.link==None:
                print('index error')
            else:
                pre.link=pre.link.link
                
    def get(self,index):
        tn=self.head
        for _ in range(index):
            tn=tn.link
            if tn==None:
                print('index error')
                return None
        return tn

l=LinkedList()
l.addtoFirst(1)
print(l.get(0).data)
l.add(1,2)
l.add(3,3)
print(l.get(1).data)
l.delete(0)
print(l.get(0).data)
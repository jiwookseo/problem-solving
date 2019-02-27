# 5108. [파이썬 S/W 문제해결 기본] 7일차 - 숫자 추가 D3

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
    def get(self,index):
        p=self.head
        for _ in range(index):
            p=p.link
        return p

for tc in range(1,int(input())+1):
    i=input().split()
    n,m,l=int(i[0]),int(i[1]),int(i[2])
    i=input().split()
    ll=LinkedList()
    for data in i:
        ll.addtoLast(data)
    for _ in range(m):
        i=input().split()
        ll.add(int(i[0]),i[1])
    print(f"#{tc} {ll.get(l).data}")
# 5110. [파이썬 S/W 문제해결 기본] 7일차 - 수열 합치기 D3

class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.next=next
        self.prev=prev


for tc in range(1,int(input())+1):
    i=input().split()
    n,m=int(i[0]),int(i[1])
    head=[]
    tail=[]
    arr=[list(map(int,input().split())) for _ in range(m)]
    for r in range(m):
        for data in arr[r]:
            temp=Node(data)
            if len(head)==r:
                head.append(temp)
                p=temp
            else:
                p.next=temp
                temp.prev=p
                p=temp
        tail.append(p)
    for i in range(1,m):
        p=head[0]
        while(p!=None):
            if p.data>head[i].data:
                break
            p=p.next
        if p==head[0]:
            p.prev=tail[i]
            tail[i].next=p
            head[0]=head[i]
            tail[i]=tail[i-1]
        elif p==None:
            tail[i-1].next=head[i]
            head[i].prev=tail[i-1]
        else:
            p.prev.next=head[i]
            head[i].prev=p.prev
            tail[i].next=p
            p.prev=tail[i]
            tail[i]=tail[i-1]
    temp=f"#{tc} "
    p=tail[m-1]
    for i in range(10):
        temp+=f"{p.data} "
        p=p.prev
    print(temp)
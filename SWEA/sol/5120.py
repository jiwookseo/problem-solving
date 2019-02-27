# 5120. [파이썬 S/W 문제해결 기본] 7일차 - 암호 D4
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

for tc in range(1,int(input())+1):
    i=input().split()
    n,m,k=int(i[0]),int(i[1]),int(i[2])
    i=list(map(int,input().split()))
    len=0
    head=Node(i.pop(0))
    p=head
    len+=1
    for data in i:
        p.next=Node(data)
        p=p.next
        len+=1
    tail=p
    index=0
    for _ in range(k):
        index=(index+m)%len
        if index==0:
            data=head.data+tail.data
            temp=Node(data)
            tail.next=temp
            tail=temp
            index=len
            len+=1
        else:
            p=head
            for _ in range(index-1):
                p=p.next
            data=p.data+p.next.data
            p.next=Node(data,p.next)
            len+=1
    temp=f"#{tc} "
    result=[]
    p=head
    while(p!=None):
        result.append(p.data)
        p=p.next
    for i in result[-1:-11:-1]:
        temp+=f"{i} "
    print(temp)
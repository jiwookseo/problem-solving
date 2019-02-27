class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

def get(index):
    p=head
    for _ in range(index):
        p=p.next
        if p==None:
            return None
    return p

for tc in range(1,int(input())+1):
    i=list(map(int,input().split()))
    n,m,l=i[0],i[1],i[2]
    i=list(map(int,input().split()))
    head=Node(i.pop(0))
    p=head
    for data in i:
        p.next=Node(data)
        p=p.next
    for _ in range(m):
        i=input().split()
        method=i[0]
        if method=="I":
            p=get(int(i[1])-1)
            p.next=Node(int(i[2]),p.next)
        elif method=="D":
            p=get(int(i[1])-1)
            p.next=p.next.next
        else:
            get(int(i[1])).data=int(i[2])
    result=get(l)
    if result!=None:
        result=result.data
    else:
        result=-1
    print(f"#{tc} {result}")
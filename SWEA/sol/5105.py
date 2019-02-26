# 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리 D3

class Queue:
    def __init__(self,size,init=None):
        self.size=size
        self.init=init
        self.storage=[self.init]*self.size
        self.front=-1
        self.rear=-1
    def enQueue(self,item):
        self.rear+=1
        self.storage[self.rear]=item
    def deQueue(self):
        self.front+=1
        return self.storage[self.front]
    def isEmpty(self):
        return self.front==self.rear

def iswell(r,c):
    global n
    return 0<=r<n and 0<=c<n

def next(r,c,sum):
    global board
    result=[]
    dr=[0,0,1,-1]
    dc=[1,-1,0,0]
    for i in range(4):
        tr=r+dr[i]
        tc=c+dc[i]
        if iswell(tr,tc):    
            if board[tr][tc]=='3':
                return 1
            elif board[tr][tc]=='0':
                result.append((tr,tc,sum+1))
                board[tr][tc]='1'
    return result

def sol(r,c,sum):
    global board,q
    temp=next(r,c,sum)
    if temp==True:
        return sum
    else:
        for i in temp:
            q.enQueue(i)
    return 0

for tc in range(1,int(input())+1):
    n=int(input())
    board=[list(input()) for _ in range(n)]
    q=Queue(n**2)
    check=False
    for i in range(n):
        for j in range(n):
            if board[i][j]=='2':
                q.enQueue((i,j,0))
                check=True
                break
        if check:
            break
    check=False
    result=0
    while(not q.isEmpty()):
        temp=sol(*(q.deQueue()))
        if temp!=0:
            result=temp
            break
    print(f"#{tc} {result}")
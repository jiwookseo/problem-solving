# 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로 D2 

def check(node):
    global maze, sol
    row,col=node[0],node[1]
    r=[0,0,1,-1]
    c=[1,-1,0,0]
    for i in range(4):
        rt=row+r[i]
        ct=col+c[i]
        if iswall(rt,ct) and not sol:
            if maze[rt][ct]==0:
                maze[rt][ct]=1
                check((rt,ct))
            elif maze[rt][ct]==3:
                sol=1
                break

def iswall(r,c):
    global n
    return 0<=r<n and 0<=c<n

for tc in range(1,int(input())+1):
    n=int(input())
    maze=[list(map(int,input())) for _ in range(n)]
    for row in range(n):
        for col in range(n):
            if maze[row][col]==2:
                node=row,col
                break
    sol=0
    check(node)
    print(f"#{tc} {sol}")
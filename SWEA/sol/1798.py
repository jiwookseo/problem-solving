# 1798. 범준이의 제주도 여행 계획 D5
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4x9oyaCR8DFAUx
max=0
def sol(visited,v,time,day,vt,score,trv):
    global max,G,a,h,p,d,result
    visited=visited[:]
    temp=trv[:]
    temp.append(v)
    if day==d:
        visited[a]=False
        for i in h:
            visited[i]=True
    elif vt!=0:
        for i in h:
            visited[i]=False
    if v==a:
        if max<score:
            max=score
            result=temp[:]
        return
    if v in p:
        time+=p[v][0]
        score+=p[v][1]
        visited[v]=True
        vt+=1
        if time>540:
            return
    elif v in h:
        time=0
        day+=1
        vt=0
        for i in h:
            visited[i]=True
    for i in range(1,len(visited)):
        if not visited[i] and time+G[v][i]<=540:
            sol(visited,i,time+G[v][i],day,vt,score,temp)
for tc in range(1,int(input())+1):
    i=input().split()
    v,d=int(i[0]),int(i[1])
    G=[[0]*(v+1) for _ in range(v+1)]
    visited=[False]*(v+1)
    result=[]
    max=0
    for i in range(1,v):
        inp=list(map(int,input().split()))
        for j in range(v-i):
            G[i][i+1+j]=G[i+1+j][i]=inp[j]
    a=0
    h=[]
    p={}
    for i in range(1,v+1):
        inp=input().split()
        if inp[0]=='A':
            a=i
        elif inp[0]=='P':
            p[i]=(int(inp[1]),int(inp[2]))
        else:
            h.append(i)
    visited[a]=True
    for i in h:
        visited[i]=True
    for i in range(1,v+1):
        if not visited[i]:
            sol(visited,i,G[a][i],1,0,0,[])
    print(f"#{tc} {max} "+" ".join([str(i) for i in result]))
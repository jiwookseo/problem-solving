i=input().split()
k=int(input())
c,r=int(i[0]),int(i[1])
if k>c*r:
    print(0)
else:
    n=[r,c,r,c]
    dr=[1,0,-1,0]
    dc=[0,1,0,-1]
    d=0
    t=0
    tr=0
    tc=1
    while(t<k):
        d%=4
        tr+=dr[d]*n[d]
        tc+=dc[d]*n[d]
        t+=n[d]
        if d%2:
            n[0]-=1
            n[2]-=1
        else:
            n[1]-=1
            n[3]-=1
        d+=1
    if k<t:
        d-=1
        tr-=dr[d]*(t-k)
        tc-=dc[d]*(t-k)
    print(tc,tr)
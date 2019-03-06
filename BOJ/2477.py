k=int(input())
e=[list(map(int,input().split())) for _ in range(6)]
s=[1,4,2,3]
result=[[],[]]
t=None
check=False
for i in range(6):
    d,x=e[i]
    tt=s.index(d)
    if t is not None:
        if tt!=(t+1)%4:
            check=True
            r=i
    t=tt
    result[t%2].append(x)
if not check:
    r=0
a,b=e[r],e[r-1]
result[s.index(a[0])%2].remove(a[1])
result[s.index(b[0])%2].remove(b[1])
print((max(result[0])*max(result[1])-a[1]*b[1])*k)
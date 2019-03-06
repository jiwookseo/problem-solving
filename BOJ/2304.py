n=int(input())
p=[list(map(int,input().split())) for _ in range(n)]
p.sort()
m=p.index(max(p,key=lambda x:x[1]))
result=0
i=m
while p[i][1]==p[m][1]:
    i+=1
    if i==n:
        break
i-=1
if i==m:
    result+=p[m][1]
else:
    result+=(p[i][0]-p[m][0]+1)*p[m][1]

a=p[:m]
x=p[m][0]
if len(a)!=0:
    s=a[0][0]
    while True:
        t=max(a,key=lambda x:x[1])
        result+=(x-t[0])*t[1]
        x=t[0]
        if x==s:
            break
        a=a[:a.index(t)]

b=p[i+1:]
x=p[i][0]
if len(b)!=0:
    e=b[-1][0]
    while True:
        t=max(b,key=lambda x:x[1])
        result+=(t[0]-x)*t[1]
        x=t[0]
        if x==e:
            break
        b=b[b.index(t)+1:]
print(result)
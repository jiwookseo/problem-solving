def check(dice,i,m):
    if i==0:
        j=5
    elif i==1:
        j=3
    elif i==2:
        j=4
    elif i==3:
        j=1
    elif i==4:
        j=2
    else:
        j=0
    m+=max([dice[k] for k in range(6) if k!= i and k!= j])
    return dice[j],m

n=int(input())
dice=[list(map(int,input().split())) for _ in range(n)]
result=0
for i in range(6):
    m=0
    j=dice[0][i]
    for d in dice:
        j,m=check(d,d.index(j),m)
    if result<m:
        result=m
print(result)
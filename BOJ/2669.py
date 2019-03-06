g=[[False]*101 for _ in range(101)]
for _ in range(4):
    i=list(map(int,input().split()))
    for x in range(i[0],i[2]):
        for y in range(i[1],i[3]):
            if not g[x][y]:
                g[x][y]=True
print(sum([sum(x) for x in g]))
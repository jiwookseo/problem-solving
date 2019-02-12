def check(r,c):
    result=0
    if c!=0 and c!=99:
        if dots[r][c-1]==1:
            result-=1
        if dots[r][c+1]==1:
            result*=3
            result+=1
    elif c==0:
        if dots[r][c+1]==1:
            result+=1
    else :
        if dots[r][c-1]==1:
            result-=1
    return result
for i in range(1,11):
    input()
    dots=[list(map(int,input().split())) for _ in range(100)]
    r=99
    c=[i for i in range(100) if dots[r][i]==2][0]
    while(r!=0):
        res=check(r,c)
        if res!=0:
            c+=res
            while(check(r,c)==-2):
                c+=res
        r-=1
    print(f"#{i} {c}")
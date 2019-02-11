# 1211. [S/W 문제해결 기본] 2일차 - Ladder1 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14BgD6AEECFAYh&categoryId=AV14BgD6AEECFAYh&categoryType=CODE

def check(r,c):
    result=[0,0]
    if c!=0 and c!=99:
        if dots[r][c-1]==1:
            result[0]=1
        if dots[r][c+1]==1:
            result[1]=1
    if c==0:
        if dots[r][c+1]==1:
            result[1]=1
    else :
        if dots[r][c-1]==1:
            result[0]=1
    return result
for i in range(1,11):
    input()
    dots=[list(map(int,input().split())) for _ in range(100)]
    endcol=[i for i in range(100) if dots[99][i]==1]
    result=[]
    for end in endcol[::-1]:
        c=end
        r=99
        count=0
        while(r!=0):
            res=check(r,c)
            if res!=[0,0]:
                c+=res.index(1)*2-1
                count+=1
                while(check(r,c)==[1,1]):
                    c+=res.index(1)*2-1
                    count+=1
            r-=1
            count+=1
        result.append([count,c])
    print(result)
    print(f"#{i} {min(result,key=lambda x:x[0])[1]}")
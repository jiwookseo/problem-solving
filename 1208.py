# 1208. [S/W 문제해결 기본] 1일차 - Flatten
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE

for i in range(1,11):
    dump=int(input())
    box=list(map(int,input().split()))
    bl=100
    row=[0]*max(box)
    for j in box:
        for k in range(j):
            row[k]+=1
    index=0
    for _ in range(dump):
        row[-1]-=1
        while(row[index]==bl):
            index+=1
        row[index]+=1
        if (len(row)-1)==index:
            break
        if row[-1]==0:
            row.pop()
    print(f"#{i} {len(row)-row.count(100)}")
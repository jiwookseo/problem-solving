# 1208. [S/W 문제해결 기본] 1일차 - Flatten
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE

for i in range(1,11):
    dump=int(input())
    box=list(map(int,input().split()))
    bw=100
    row=[0]*max(box)
    for j in box:
        for k in range(j):
            row[k]+=1
    while(dump!=0):
        if len(row)<=1:
            break
        if row[-1]>dump:
            down=dump
            row[-1]-=down
            dump=0
        else :
            down=row.pop()
            dump-=down
        while(1):
            while(row[0]==bw):
                row.pop(0)
            temp=bw-row[0]
            if temp<=down:
                row.pop(0)
                down-=temp
            else :
                row[0]+=down
                break
    print(f"#{i} {len(row)}")
bingo=dict()
for i in range(5):
    inp=input().split()
    for j in range(5):
        bingo[int(inp[j])]=(i,j)
check=[0]*12
result=0
count=0
num=[map(int,input().split()) for _ in range(5)]
for row in num:
    for i in row:
        count+=1
        a,b=bingo[i]
        if check[a]==4:
            result+=1
        else:
            check[a]+=1
        if check[b+5]==4:
            result+=1
        else:
            check[b+5]+=1
        if a==b:
            if check[10]==4:
                result+=1
            else:
                check[10]+=1
        if a+b==4:
            if check[11]==4:
                result+=1
            else:
                check[11]+=1
        if result>=3:
            print(count)
            break
    if result>=3:
        break
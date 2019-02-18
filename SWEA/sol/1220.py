# 1220. [S/W 문제해결 기본] 5일차 - Magnetic D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14hwZqABsCFAYD&categoryId=AV14hwZqABsCFAYD&categoryType=CODE
for tc in range(1,11):
    n=int(input())
    table=[input().replace(" ","").replace("0","") for _ in range(n)]
    result=0
    for col in range(len(table)):
        check='0'
        for row in range(len(col)):
            temp=table[row][col]
            if temp=='1' and check!='1':
                result+=1
            if temp!=check:
                check=temp
        if check=='1':
            result-=1
    print(f"#{tc} {result}")
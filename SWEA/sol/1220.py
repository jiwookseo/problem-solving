# 1220. [S/W 문제해결 기본] 5일차 - Magnetic D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14hwZqABsCFAYD&categoryId=AV14hwZqABsCFAYD&categoryType=CODE
for tc in range(1,11):
    n=int(input())
    table=[input().split() for _ in range(n)]
    result=0
    for col in range(n):
        check=0
        for row in range(n):
            temp=table[row][col]
            if temp=='1':
                check=1
            if temp=='2' and check==1:
                check=2
                result+=1
    print(f"#{tc} {result}")
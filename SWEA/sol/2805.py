# 2805. 농작물 수확하기 D3
# https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB&categoryId=AV7GLXqKAWYDFAXB&categoryType=CODE
for tc in range(1,int(input())+1):
    n=int(input())
    m=n//2
    val=[list(input()) for _ in range(n)]
    count=0
    t=0
    a=1
    for i in range(n):
        count+=sum([int(val[i][j]) for j in range(m-t,m+t+1)])
        if m-t==0:
            a=-1
        t+=a
    print(f"#{tc} {count}")
# 1979. 어디에 단어가 들어갈 수 있을까 D2
# https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq&categoryId=AV5PuPq6AaQDFAUq&categoryType=CODE
# 일일히 찾는 방법
for tc in range(1,int(input())+1):
    i=input().split()
    n,k=int(i[0]),int(i[1])
    board=[list(map(int,input().split())) for _ in range(n)]
    result=0
    for r in range(n):
        check=False
        count=0
        for c in range(n):
            if board[r][c]==0:
                if check:
                    if count==k:
                        result+=1
                    check=False
                count=0
            elif count<=k:
                check=True
                count+=1
        if check:
            if count==k:
                result+=1
            check=False
    for c in range(n):
        check=False
        count=0
        for r in range(n):
            if board[r][c]==0:
                if check:
                    if count==k:
                        result+=1
                    check=False
                count=0
            elif count<=k:
                check=True
                count+=1
        if check:
            if count==k:
                result+=1
            check=False
    print(f"#{tc} {result}")
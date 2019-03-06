# 1979. 어디에 단어가 들어갈 수 있을까 D2
# https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq&categoryId=AV5PuPq6AaQDFAUq&categoryType=CODE
for tc in range(1,int(input())+1):
    i=input().split()
    n,k=int(i[0]),int(i[1])
    board=[input().replace(" ","") for _ in range(n)]
    b=board[:]
    result=0
    for i in b:
        result+=i.replace("1"*(k+1),"").count("1"*k)
    for i in range(n):
        result+="".join([board[j][i] for j in range(n)]).replace("1"*(k+1),"").count("1"*k)
    print(f"#{tc} {result}")
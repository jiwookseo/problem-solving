# 1258. [S/W 문제해결 응용] 7일차 - 행렬찾기 D4
# https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18LoAqItcCFAZN&categoryId=AV18LoAqItcCFAZN&categoryType=CODE

def check(r,c):
    global board
    tr=r
    tc=c
    while(tr<n and board[tr][tc]!='0'):
        tr+=1
    rr=tr-r
    tr=r
    while(tc<n and board[tr][tc]!='0'):
        tc+=1
    rc=tc-c
    for i in range(rr):
        for j in range(rc):
            board[r+i][c+j]='0'
    return (rr,rc)

for tc in range(1,int(input())+1):
    n=int(input())
    board=[input().split() for _ in range(n)]
    result=[]
    for r in range(n):
        for c in range(n):
            if board[r][c]!='0':
                result.append(check(r,c))
    result.sort(key=lambda x:x[0])
    result.sort(key=lambda x:x[0]*x[1])
    print(f"#{tc} {len(result)} ",end="")
    for i in result:
        print(f"{i[0]} {i[1]} ",end="")
    print()
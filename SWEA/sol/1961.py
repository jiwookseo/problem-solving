# 1961. 숫자 배열 회전 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq&categoryId=AV5Pq-OKAVYDFAUq&categoryType=CODE

for tc in range(1,int(input())+1):
    n=int(input())
    board=[input().split() for _ in range(n)]
    string=f"#{tc}\n"
    for r in range(n):
        for c in range(n):
            string+=board[n-1-c][r]
        string+=" "
        for c in range(n):
            string+=board[n-1-r][n-1-c]
        string+=" "
        for c in range(n):
            string+=board[c][n-1-r]
        string+="\n"
    print(string,end="")
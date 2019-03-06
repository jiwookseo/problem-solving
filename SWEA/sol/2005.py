# 2005. 파스칼의 삼각형 D2
# https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq&categoryId=AV5P0-h6Ak4DFAUq&categoryType=CODE&&&
for tc in range(1,int(input())+1):
    n=int(input())
    psc=[[0]*i for i in range(3,3+n)]
    psc[0][1]=1
    for r in range(1,n):
        for c in range(1,r+2):
            psc[r][c]=psc[r-1][c-1]+psc[r-1][c]
    print(f"#{tc}")
    for r in psc:
        print(" ".join([str(i) for i in r[1:-1]]))
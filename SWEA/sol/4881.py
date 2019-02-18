# 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합 D2

mini=0
def sol(a,k,sum):
    a=a[:]
    global n, queen, mini
    if sum>=mini:
        return
    elif k==(n-1):
        if mini>sum:
            mini=sum
    else:
        k+=1
        for i in range(n):
            check=True
            for j in a:
                if i==j:
                    check=False
                    break
            if check:
                a[k]=i
                sol(a,k,sum+queen[k][i])
                
for tc in range(1,int(input())+1):
    n=int(input())
    queen=[list(map(int,input().split())) for _ in range(n)]
    a=[n]*n
    mini=n*10
    sol(a,-1,0)
    print(f"#{tc} {mini}")
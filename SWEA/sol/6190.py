# 6190. 정곤이의 단조 증가하는 수 D3
# https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWcPjEuKAFgDFAU4&categoryId=AWcPjEuKAFgDFAU4&categoryType=CODE
for tc in range(1,int(input())+1):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    result=-1
    for i in range(n):
        for j in range(i+1,n):
            tt=t=a[i]*a[j]
            check=True
            while tt>0:
                ttt=tt%10
                tt//=10
                if ttt<tt%10:
                    check=False
                    break
            if check and result<t:
                result=t
    print(f"#{tc} {result}")
# 1216. [S/W 문제해결 기본] 3일차 - 회문2 D3

def check(array,n,m):
    for r in range(n):
        for i in range(n-m+1):
            temp=m//2
            for j in range(temp):
                if array[r][i+j]!=array[r][i+m-1-j]:
                    break
            if j==temp:
                return m
    return None
 
def check_T(array,n,m):
    for c in range(n):
        for i in range(n-m+1):
            temp=m//2
            for j in range(temp):
                if array[i+j][c]!=array[i+m-1-j][c]:
                    break
            if j==temp:
                return m
    return None
 
for _ in range(10):
    tc=int(input())
    n=100
    array=[[]]*n
    for r in range(n):
        array[r]=list(input())
    m=1
    check1=1
    check2=1
    result=1
    while(1):
        m+=1
        if check1!=0:
            temp=check(array,n,m)
            if temp!=None:
                check1=m
                result=m
            elif m-check1>2:
                check1=0
        if check1!=m and check2!=0:
            temp=check_T(array,n,m)
            if temp!=None:
                check2=m
                result=m
            elif check_T(array,n,m-1)==None:
                check2=0
        if check1==0 and check2==0:
            break
    print(f"#{tc} {result}")
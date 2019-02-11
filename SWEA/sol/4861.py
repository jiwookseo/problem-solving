# 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문 D2

def check(array,n):
    check=False
    for r in range(n):
        for i in range(n-m+1):
            for j in range(m//2):
                if array[r][i+j]!=array[r][i+m-1-j]:
                    check=False
                    break
                check=True
            if check:
                return array[r][i:i+m]
    return None

def check_T(array,n):
    check=False
    for c in range(n):
        for i in range(n-m+1):
            for j in range(m//2+1):
                if array[i+j][c]!=array[i+m-1-j][c]:
                    check=False
                    break
                check=True
            if check:
                return [x[c] for x in array[i:i+m]]
    return None

for tc in range(1, int(input()) + 1):
    nnm=input().split()
    n,m=int(nnm[0]),int(nnm[1])
    array=[[]]*n
    for r in range(n):
        array[r]=list(input())
    result=check(array,n)
    if result==None:
        result=check_T(array,n)
    joinStr="".join(result)
    print(f"{tc} {joinStr}")

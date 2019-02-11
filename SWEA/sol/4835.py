# 4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합 D2

def sumK(num,k):
    result=[]
    for i in range(len(num)-k+1):
        result.append(sum(num[i:i+k]))
    return result

testNum=int(input())
for i in range(1,testNum+1):
    m=int(input().split()[1])
    num=list(map(int,input().split()))
    result=sumK(num,m)
    print(f"#{i} {max(result)-min(result)}")
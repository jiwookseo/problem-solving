# 4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합 D3

arr=list(range(1,13))
def checkSubset(arr,n,k):
    size=len(arr)
    count=0
    for i in range(1,1<<size):
        subset=[arr[j] for j in range(size) if i&(1<<j)]
        if sum(subset)==k and len(subset)==n:
            count+=1
    return count

for tc in range(1,int(input())+1):
    inp=list(map(int,input().split()))
    n,k=inp[0],inp[1]
    print(f"#{tc} {checkSubset(arr,n,k)}")
# 4828. [파이썬 S/W 문제해결 기본] 1일차 - min max

testNum=int(input())
for i in range(1,testNum+1):
    input()
    num=list(map(int,input().split()))
    print(f"#{i} {max(num)-min(num)}")
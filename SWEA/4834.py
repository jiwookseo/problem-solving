# 4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드

testNum=int(input())
for i in range(1,testNum+1):
    input()
    num=input()
    count=[]
    for j in range(9,-1,-1):
        count.append([j,num.count(str(j))])
    temp=max(count,key=lambda x:x[1])
    print(f"#{i} {temp[0]} {temp[1]}")
# 1206. [S/W 문제해결 기본] 1일차 - View
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE

for i in range(1,11):
    caselen=int(input())
    buliding=list(map(int,input().split()))
    result=0
    for j in range(2,caselen-2):
       	temp=buliding[j-2:j+3]
        result+= max((temp.pop(2)-max(temp)),0)
    print(f"#{i} {result}")
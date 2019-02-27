# 1767. [SW Test 샘플문제] 프로세서 연결하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf
from pprint import pprint as pp
number=0
mini=0

def remove(li,item):
    for i in range(len(li)):
        if li[i]==item:
            del li[i]
            return

def check(row,col):
    dr=[0,0,1,-1] #동서남북
    dc=[1,-1,0,0]
    result=[]
    for i in range(4):
        c=True
        tr=row
        tc=col
        while(0<tr<n-1 and 0<tc<n-1 and c):
            tr+=dr[i]
            tc+=dc[i]
            if cell[tr][tc]!="0":
                c=False
        if c:
            result.append(i)
    return result

def line(key,route,i,result,sum):
    global mini
    global number
    if i==0:
        sum+=(n-1-key[1])
    elif i==1:
        sum+=key[1]
    elif i==2:
        sum+=(n-1-key[0])
    else:
        sum+=key[0]
    tempRoute=copy(route)
    del tempRoute[key]
    temp=[]
    for k in tempRoute:
        if (i==0 and key[1]<k[1]) or (i==1 and key[1]>k[1]):
            if key[0]>k[0]:
                remove(tempRoute[k],3)
            elif key[0]<k[0]:
                remove(tempRoute[k],2)
        elif (i==2 and key[0]<k[0]) or (i==3 and key[0]>k[0]):
            if key[1]>k[0]:
                remove(tempRoute[k],0)
            elif key[1]<k[0]:
                remove(tempRoute[k],1)
        if tempRoute[k]==[]:
            temp.append(k)
    for k in temp:
        del tempRoute[k]

    if len(tempRoute)+result+1<number and mini<sum:
        return

    if len(tempRoute)==0:
        result+=1
        if result>number:
            number=result
            mini=sum
        elif result==number and mini>sum:    
            mini=sum
        return
    
    for k,v in tempRoute.items():
        if len(v)==1:
            line(k,tempRoute,v[0],result+1,sum)
    for k,v in tempRoute.items():
        if len(v)!=1:
            for vv in v:
                line(k,tempRoute,vv,result+1,sum)

def copy(some):
    result=dict()
    for k,v in some.items():
        result[k]=v[:]
    return result

for tc in range(1,int(input())+1):
    n=int(input())
    number=0
    mini=n**2
    cell=[input().split() for _ in range(n)]
    result=0
    for i in range(0,n):
        if cell[0][i]=="1" and i!=0 and i!=n-1:
            result+=1
        if cell[n-1][i]=="1" and i!=0 and i!=n-1:
            result+=1
        if cell[i][0]=="1":
            result+=1
        if cell[i][n-1]=="1":
            result+=1
    route=dict()
    for row in range(1,n-1):
        for col in range(1,n-1):
            if cell[row][col]=="1":
                temp=check(row,col)
                if temp!=[]:
                    route[row,col]=temp
    for k,v in route.items():
        if len(v)==1:
            line(k,route,v[0],result,0)
    for k,v in route.items():
        if len(v)!=1:
            for vv in v:
                line(k,route,vv,result,0)
    print(number, mini)
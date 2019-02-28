# 1974 스도쿠 검증 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq&categoryId=AV5Psz16AYEDFAUq&categoryType=CODE
# 3가지 version으로 작성하였는데, 메모리, 퍼포먼스 모두 비슷한 수준
# 가장 익숙한, 빨리 짤 수 있는 코드로 작성하는 것이 좋겠다.

# ver.1
# 메모리 49,100 kb
# 실행시간 142 ms
for tc in range(1,int(input())+1):
    b=[]
    result=1
    for _ in range(9):
        a=[False]*10
        if result==1:
            temp=list(map(int,input().split()))
            t=[0]*10
            for i in temp:
                if a[i]:
                    result=0
                else:
                    a[i]=True
            b.append(temp)
        else :
            input()
    c=0
    while(result==1 and c<9):
        a=[False]*10
        for i in range(9):
            t=b[i][c]
            if a[t]:
                result=0
                break
            else:
                a[t]=True
        c+=1
    r=c=0
    while(result==1 and r<3):
        a=[False]*10
        for dr in range(3):
            for dc in range(3):
                t=b[3*r+dr][3*c+dc]
                if a[t]:
                   result=0
                   break
                else:
                    a[t]=True
        c+=1
        if c==3:
            c=0
            r+=1
    print(f"#{tc} {result}")
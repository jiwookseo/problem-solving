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
    t=set(range(1,10))
    for _ in range(9):
        if result==1:
            temp=list(map(int,input().split()))
            if (t-set(temp))!=set():
                result=0
                continue
            b.append(temp)
        else :
            input()
    r=c=0
    while(result==1 and r<3):
        tmp=3*r+c
        if (t-{b[i][tmp] for i in range(9)})!=set():
            result=0
        elif (t-{b[3*r+dr][3*c+dc] for dr in range(3) for dc in range(3)})!=set():
            result=0
        c+=1
        if c==3:
            c=0
            r+=1
    print(f"#{tc} {result}")
# 1974 스도쿠 검증 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq&categoryId=AV5Psz16AYEDFAUq&categoryType=CODE
# ver.3
# board를 저장하지 않고 원소 별로 인덱스를 저장해 처리하는 방식
# 메모리 48,052 kb
# 실행시간 143 ms

for tc in range(1,int(input())+1):
    rb=[[] for _ in range(10)]
    cb=[[] for _ in range(10)]
    for r in range(9):
        temp=list(map(int,input().split()))
        t=[0]*10
        tcb=[]
        for c in range(9):
            rb[temp[c]].append(r)
            cb[temp[c]].append(c)
    t=list(range(9))
    tt=set(range(9))
    result=1
    for i in range(1,10):
        if rb[i]!=t:
            result=0
            break
        elif set(cb[i])!=tt:
            result=0
            break
        for j in range(0,9,3):
            check=[False]*3
            for k in cb[i][j:j+3]:
                if k<3:
                    if check[0]:
                        result=0
                        break
                    else:
                        check[0]=True
                elif k<6:
                    if check[1]:
                        result=0
                        break
                    else:
                        check[1]=True
                else:
                    if check[2]:
                        result=0
                        break
                    else:
                        check[2]=True
            if result==0:
                break
    print(f"#{tc} {result}")
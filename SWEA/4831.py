# 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스 D3

testNum=int(input())
for i in range(1,testNum+1):
    num=list(map(int,input().split()))
    k,n=num[0],num[1]
    charge=list(map(int,input().split()))
    current=0
    move=0
    while(1):
        move+=1
        if current+k>=n:
            move-=1
            break
        else :
            enable=[x for x in charge if x>current and x<=current+k]
            if enable==[]:
                move=0
                break
            else:
                current=enable[-1]
    print(f"#{i} {move}")
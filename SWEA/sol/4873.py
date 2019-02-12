# 4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기 D2
for tc in range(1,int(input())+1):
    inp=list(input())
    check=True
    while(check):
        check=False
        temp=""
        for i in range(len(inp)):
            if temp==inp[i]:
                inp=inp[:i-1]+inp[i+1:]
                check=True
                break
            temp=inp[i]
    print(f"#{tc} {len(inp)}")
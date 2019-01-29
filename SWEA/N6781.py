# 6781. 삼삼 트리플 게임 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWgqpQV6r8gDFAW0&categoryId=AWgqpQV6r8gDFAW0&categoryType=CODE

def check(data):
    result=0
    for i in range(3):
        if len(data[i])-len(set(data[i]))>=2:
            for j in data[i]:
                if data[i].count(j)>=3:
                    result+=1
                    for _ in range(3):
                        data[i].remove(j)
        else:
            temp=sorted(data[i])
            while(len(temp)>=3):
                if temp[1]==temp[0]+1:
                    if temp[2]==temp[0]+2:
                        result+=1
                        for _ in range(3):
                            del temp[0]
                else:
                    del temp[0]
    return "Win" if result>=3 else "Continue"

for tc in range(1,int(input())+1):
    num=map(int,input())
    col=input()
    card=zip(num,col)
    data=[[],[],[]]
    for n,c in card:
        if c=='R':
            data[0].append(n)
        elif c=='G':
            data[1].append(n)
        else:
            data[2].append(n)
    print(f"#{tc} {check(data)}")

# Python 제출 불가능
# C코드로 작성해 제출하였다.
# 오답 41/50 맞음
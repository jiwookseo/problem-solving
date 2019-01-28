# 5954. 지루하지 않은 수열 D7
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWZ2Mq4aDFsDFAUQ

for tc in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    t=1
    ans = 1
    b = len(a)-1
    while ans and t!=n and b:
        for i in range(n-t):
            ans = 0
            a1 = a[i:i+t+1]
            a2 = set(a1)
            for j in a2:
                if a1.count(j) == 1:
                    ans = 1
                    break
            if ans == 0:
                break
        t+=1
    print(f"#{tc+1} {ans}")
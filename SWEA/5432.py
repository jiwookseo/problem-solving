# 5432. 쇠막대기 자르기 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVl47b6DGMDFAXm&categoryId=AWVl47b6DGMDFAXm&categoryType=CODE

tc=int(input())
for i in range(1,tc+1):
    ins=input().replace("()","o")
    current=[]
    count=0
    for s in ins:
        if s=="(":
            count+=1
            current.append(0)
        elif s==")":
            current.pop()
        else:
            count+=len(current)
    print(f"#{i} {count}")
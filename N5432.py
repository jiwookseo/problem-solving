# 5432. 쇠막대기 자르기 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVl47b6DGMDFAXm&categoryId=AWVl47b6DGMDFAXm&categoryType=CODE

tc=int(input())
for i in range(1,tc+1):
    ins=input().replace("()","o")
    result=[]
    current=[]
    count=0
    for s in ins:
        if s=="(":
            if result==[]:
                result=[[0]]
                current=[0]
                count+=1
            else :
                temp=result
                for i in current:
                    temp=temp[i]
                temp.append([0])
                count+=1
                current.append(1)
        elif s==")":
            current.pop()
        else:
            count+=len(current)
    print(f"#{i} {count}")
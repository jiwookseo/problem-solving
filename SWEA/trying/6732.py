# 6732. 현주의 기차 여행
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWef0pSq5RADFAUh&categoryId=AWef0pSq5RADFAUh&categoryType=CODE
# not yet

T=int(input())
for case in range(1,T+1):
    inp=list(map(int,input().split()))
    n,m,z=inp[0],inp[1],inp[2]
    locate={str(i):list() for i in range(n+1)}
    count=set()
    for _ in range(m):
        [a,b]=input().split()
        locate[a].append(b)
        locate[b].append(a)
    for i in range(1,n):
        result=["0"+str(i)]
        for _ in range(z):
            tempList=[]
            for j in range(len(result)):
                for k in [x for x in locate[result[j][-1]] if x!=result[j][-2]]:
                    temp=result[j]
                    temp+=k
                    tempList.append(temp)
            result=tempList
        for j in result:
            count.add((min(j[1],j[-1]),max(j[1],j[-1])))
    print(f"#{case} {len(count)}")
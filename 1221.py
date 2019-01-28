num=["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1,int(input())+1):
    input()
    string=input().split()
    count=[0]*10
    for item in string:
        count[num.index(item)]+=1
    print(f"#{tc}")
    ans=""
    for i in range(len(count)):
        ans+=count[i]*(num[i]+" ")
    print(ans)
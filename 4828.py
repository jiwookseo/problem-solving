testNum=int(input())
for i in range(1,testNum+1):
    input()
    num=list(map(int,input().split()))
    print(f"#{i} {max(num)-min(num)}")
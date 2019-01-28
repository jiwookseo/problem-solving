# 6109. 추억의 2048게임
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWbrg9uabZsDFAWQ&categoryId=AWbrg9uabZsDFAWQ&categoryType=CODEs


T = int(input())
for test_case in range(1, T + 1):
    inp = input().rstrip().split(" ")
    caseLen = int(inp[0])
    method = inp[1]
    array = []
    for i in range(caseLen):
        array.append(list(map(int,input().split())))
    if method=="up" or method=="down":
        array=list(map(list,zip(*array)))
    for i in range(caseLen):
        if method=="right" or method=="down":
            array[i].reverse()
        for j in range(caseLen-1):
            for _ in range(array[i].count(0)):
                temp=array[i].index(0)
                array[i][temp:-1]=array[i][temp+1:]
                array[i][-1]=-1
            if array[i][j]==-1:
                pass
            elif array[i][j]==array[i][j+1]:
                array[i][j]*=2
                array[i][j+1]=-1
        c=array[i].count(-1)
        for _ in range(c):
            array[i].remove(-1)
            array[i].append(0)
        if method=="right" or method=="down":
            array[i].reverse()
    if method=="up" or method=="down":
        array=list(map(list,zip(*array)))
    print(f"#{test_case}")
    print("\n".join([" ".join([str(x) for x in i]) for i in array]))
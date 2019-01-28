# 1259. [S/W 문제해결 응용] 7일차 - 금속막대 D5
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18NaZqIt8CFAZN&categoryId=AV18NaZqIt8CFAZN&categoryType=CODE

for tc in range(1,int(input())+1):
    input()
    inp=input().split()
    start=[]
    end=[]
    while(len(inp)!=0):
        start.append(inp.pop(0))
        end.append(inp.pop(0))
    result=[start.pop(0),end.pop(0)]
    while(len(start)!=0):
        delindex=[]
        for i in range(len(start)):
            if result[0]==end[i]:
                result.insert(0,end[i])
                result.insert(0,start[i])
                delindex.append(i)
            elif result[-1]==start[i]:
                result.append(start[i])
                result.append(end[i])
                delindex.append(i)
        for i in delindex[::-1]:
            del start[i]
            del end[i]
    resultStr=" ".join(result)
    print(f"#{tc} {resultStr}")
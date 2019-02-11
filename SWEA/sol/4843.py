# 4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬 D3

def specialSort(li):
    result=[]
    for _ in range(5):
        minimum=li[0]
        minind=0
        maximum=li[0]
        maxind=0
        for i in range(len(li)):
            if li[i]>maximum:
                maximum=li[i]
                maxind=i
        result.append(str(li.pop(maxind)))
        for i in range(len(li)):
            if li[i]<minimum:
                minimum=li[i]
                minind=i
        result.append(str(li.pop(minind)))
    return result

for tc in range(1,int(input())+1):
    input()
    inp=list(map(int,input().split()))
    string=" ".join(specialSort(inp))
    print(f"#{tc} {string}")
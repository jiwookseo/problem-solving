# 4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색 D2

def binarySearch(p,aim):
    l=1
    r=p
    c=int((l+r)/2)
    count=1
    while(c!=aim):
        l=c if aim>c else l
        r=r if aim>c else c
        c=int((l+r)/2)
        count+=1
    return count

def check(a,b):
    if a<b:
        return "A"
    elif a>b:
        return "B"
    else:
        return "0"

for tc in range(1,int(input())+1):
    inp=list(map(int,input().split()))
    p,a,b=inp[0],inp[1],inp[2]
    print(f"#{tc} {check(binarySearch(p,a),binarySearch(p,b))}")
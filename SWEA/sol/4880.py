#  4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임 D2

def rcp(a,b):
    if a.item=="3":
        return b if b.item=="1" else a
    elif b.item=="3":
        return a if a.item=="1" else b
    return a if a.item>=b.item else b

def tnm(a,b):
    la,lb=len(a)-1,len(b)-1
    if la==0 and lb==0:
        return [rcp(a[0],b[0])]
    elif la!=0:
        return tnm(tnm(a[:la//2+1],a[la//2+1:]),b)
    elif lb!=0:
        return tnm(a,tnm(b[:lb//2+1],b[lb//2+1:]))

class card:
    num=0
    def __init__(self,item):
        card.num+=1
        self.num=card.num
        self.item=item

for tc in range(1,int(input())+1):
    n=int(input())
    c=[card(i) for i in input().split()]
    lc=len(c)-1
    card.num=0
    result=tnm(c[:lc//2+1],c[lc//2+1:])[0].num
    print(f"#{tc} {result}")
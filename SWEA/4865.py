# 4865. [파이썬 S/W 문제해결 기본] 3일차 - 글자수 D2
for tc in range(1,int(input())+1):
    a=input()
    b=input()
    la=len(a)
    lb=len(b)
    strList=[0]*la
    count=[0]*la
    for i in range(la):
        check=True
        for j in range(la):
            if a[i]==strList[j]:
                check=False
        if check:
            for j in range(lb):
                if a[i]==b[j]:
                    count[i]+=1
    max=0
    for i in count:
        max=i if i>max else max
    print(f"#{tc} {max}")
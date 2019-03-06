for _ in range(4):
    i=list(map(int,input().split()))
    x=i[::2]
    y=i[1::2]
    a=len(set(range(x[0],x[1]+1)).intersection(set(range(x[2],x[3]+1))))
    b=len(set(range(y[0],y[1]+1)).intersection(set(range(y[2],y[3]+1))))
    if a>1 and b>1:
        print("a")
    elif (a==1 and b>1) or (a>1 and b==1):
        print("b")
    elif a==1 and b==1:
        print("c")
    else:
        print("d")
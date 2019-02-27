def sol(a,k):
    global max
    c=[True,False]
    sum=check(a)
    if sum>10:
        return
    elif k==max:
        if sum==10:
            print("{"+", ".join([str(i) for i in range(1,max+1) if a[i]])+"}")
    else:
        k+=1
        for i in c:
            a[k]=i
            sol(a,k)

def check(a):
    global max
    sum=0
    for i in range(1,max+1):
        if a[i]: sum+=i
    return sum

max=10
a=[None]*(max+1)
sol(a,0)
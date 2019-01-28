m=int(input())
num=[]
for i in range(m):
    num.append(int(input()))
maximum=max(num)
count={}
def gen():
    a0=1
    b0=0
    yield a0,b0
    a1=0
    b1=1
    yield a1,b1
    for _ in range(maximum-1):
        a2=a0+a1
        b2=b0+b1
        yield a2,b2
        a0,a1=a1,a2
        b0,b1=b1,b2
for i, fib in enumerate(gen()):
    if i in num:
        count[i]=fib
for i in num:
    print(*count[i])
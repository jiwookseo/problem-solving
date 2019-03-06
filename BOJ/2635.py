n=int(input())
def check(s):
    a=n
    b=s
    result=[str(n),str(s)]
    while(b>=0):
        a,b=b,a-b
        result.append(str(b))
    return result[:-1]
m=0
for i in range(1,n+1):
    t=check(i)
    if m<len(t):
        m=len(t)
        result=t
print(m)
print(" ".join(result))
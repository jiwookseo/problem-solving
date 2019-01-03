n=int(input())
def gen():
    a0=1
    yield a0
    a1=1
    yield a1
    for _ in range(n-2):
        a2=a0+a1
        yield a2%100000
        a0,a1=a1,a2
for i in gen():
    pass
print(i)

# Not successful yet
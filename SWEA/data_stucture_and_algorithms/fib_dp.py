fib=[0,1,1]
n=int(input())
for i in range(n+1):
    if i==len(fib):
        fib.append(fib[i-1]+fib[i-2])
print(fib[n])
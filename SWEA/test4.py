n=int(input())
f_list=[1,1]
def f(n):
    for i in range(n+1):
        if i==len(f_list):
            f_list.append(f_list[i-1]*i)
    return f_list[n]
count=0
for i in range(n//2+1):
    count+=int(f(n-i)/(f(n-i*2)*f(i)))
print(count)
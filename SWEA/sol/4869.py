# 4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기 D2

f_list=[1,1]
def f(n):
    for i in range(n+1):
        if i==len(f_list):
            f_list.append(f_list[i-1]*i)
    return f_list[n]

for tc in range(1,int(input())+1):
    n=int(input())//10
    count=0
    for i in range(n//2+1):
        count+=int(f(n-i)/(f(n-i*2)*f(i)))*2**i
    print(count)
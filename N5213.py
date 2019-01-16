# 5213. 진수의 홀수 약수 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWT-hF8KdBADFAVT&categoryId=AWT-hF8KdBADFAVT&categoryType=CODE

def ordprime(p,k):
    return int((p**(k+1)-1)/(p-1))

def f(num):
    if result[num]!=None:
        return result[num]
    if num==1:
        return 1
    if num%2==0:
        while(num%2==0):
            num//=2
        return f(num)
    else:
        index=0
        while(num!=1):
            count=0
            p=prime[index]
            while(num%p==0):
                num//=p
                count+=1
            if count!=0:
                return f(num)*result[p**count]
            index+=1

def is_prime(n):
    if n<3:
        return False
    if n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    if n<9:
        return True
    k,l=5,n**0.5
    while(k<=l):
        if n%k==0 or n%(k+2)==0:
            return False
        k+=6
    return True

result=[None]*1000001
prime=[x for x in range(3,1000001) if is_prime(x)]
for p in prime:
    temp=p
    k=1
    while(temp<=1000000):
        if result[temp]==None:
            result[temp]=ordprime(p,k)
        k+=1
        temp*=p
for j in range(1,1000001):
    if result[j]==None:
        result[j]=f(j)

testNum=int(input())
for i in range(1,testNum+1):
    num=input().split()
    l,r=int(num[0]),int(num[1])
    print(f"#{i} {int(sum([result[x] for x in range(l,r+1)]))}")
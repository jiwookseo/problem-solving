i=input().split()
n,k=int(i[0]),int(i[1])
seq=list(map(int,input().split()))
result=t=sum(seq[:k])
for i in range(n-k):
    t-=seq[i]
    t+=seq[i+k]
    if result<t:
        result=t
print(result)
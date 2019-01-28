import random
n=10
arr=random.sample(range(-100, 100), n)
for i in range(1,1<<n):
    subset=[arr[j] for j in range(n) if i&(1<<j)]
    if sum(subset)==0:
        print(subset)
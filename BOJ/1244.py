input()
swc=[-1]+list(map(int,input().split()))
n=int(input())
for _ in range(n):
    std=input().split()
    num=int(std[1])
    if std[0]=='1':
        for i in range(num,len(swc),num):
            swc[i] = 1 if swc[i] == 0 else 0
    else:
        swc[num] = 1 if swc[num] == 0 else 0
        i=1
        while (num+i)<len(swc) and (num-i)>=0:
            if swc[num+i]!=swc[num-i]:
                break
            swc[num-i] = swc[num+i] = 1 if swc[num+i] == 0 else 0
            i+=1
swc.pop(0)
t=0
while(t*20<len(swc)):
    print(" ".join([str(i) for i in swc[20*t:min(20*t+20,len(swc))]]))
    t+=1
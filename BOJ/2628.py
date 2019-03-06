i=input().split()
x=[0,int(i[0])]
y=[0,int(i[1])]
n=int(input())
for _ in range(n):
    i=input().split()
    if int(i[0])==0:
        y.append(int(i[1]))
    else:
        x.append(int(i[1]))
x.sort()
y.sort()
x2=x[1:]
y2=y[1:]
mx=my=0
for i in range(len(x2)):
    dx=x2[i]-x[i]
    mx=dx if mx<dx else mx
    for j in range(len(y2)):
        dy=y2[j]-y[j]
        my=dy if my<dy else my
print(mx*my)
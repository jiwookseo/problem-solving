import random
from pprint import pprint as pp

size=5

def nbhd(array,r,c):
    n=[]
    dr=[-1,0,1,0]
    dc=[0,-1,0,1]
    for i in range(4):
        tempR=r+dr[i]
        tempC=c-dc[i]
        if tempR>=size or tempR<0 or tempC>=size or tempC<0:
            pass
        else:
            n.append(array[tempR][tempC])
    result=0
    m=array[r][c]
    for i in n:
        result+=i-m if i>=m else m-i
    return result

a=[[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
result=[[nbhd(a,i,j) for j in range(size)] for i in range(size)]
pp(a)
pp(result)
print(sum(map(sum,result)))
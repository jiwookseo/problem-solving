# 6058. 새해 축하 파티 D5
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWbHe_w6AHIDFAV0&categoryId=AWbHe_w6AHIDFAV0&categoryType=CODE

def gen():
    a=0
    for i in range(1,401):
        a+=i
        yield a

for tc in range(1,int(input())+1):
    inp=list(map(int,input().split()))
    b,l,k=3*inp[0],inp[1],inp[2]
    genN=gen()

# 너무 어렵다. 그래프? 트리?
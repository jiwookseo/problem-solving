# 1232. [S/W 문제해결 기본] 9일차 - 사칙연산 D4
# https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV141J8KAIcCFAYD&categoryId=AV141J8KAIcCFAYD&categoryType=CODE
class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def preorder(nd):
    global s
    if nd:
        preorder(nd.left)
        preorder(nd.right)
        if not isinstance(nd.data, int):
            b=s.pop()
            a=s.pop()
            if nd.data=="*":
                s.append(a*b)
            elif nd.data=="/":
                s.append(a/b)
            elif nd.data=="+":
                s.append(a+b)
            else:
                s.append(a-b)
        else:
            s.append(nd.data)

for tc in range(1,11):
    n=int(input())
    ns=[Node(None) for _ in range(n+1)]
    s=[]
    for _ in range(n):
        i=input().split()
        if len(i)==2:
            ns[int(i[0])].data=int(i[1])
        else:
            nd=ns[int(i[0])]
            nd.data=i[1]
            nd.left=ns[int(i[2])]
            nd.right=ns[int(i[3])]
    preorder(ns[1])
    print(f"#{tc} {int(s.pop())}")
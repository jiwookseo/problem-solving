# 1231. [S/W 문제해결 기본] 9일차 - 중위순회 D4
# https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV140YnqAIECFAYD&categoryId=AV140YnqAIECFAYD&categoryType=CODE
class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def inorder(nd):
    global result
    if nd:
        inorder(nd.left)
        result+=nd.data
        inorder(nd.right)

for tc in range(1,11):
    n=int(input())
    ns=[None]
    ns+=[Node("") for i in range(1,n+1)]
    for _ in range(n):
        i=input().split()
        i+=[0,0]
        nd=ns[int(i[0])]
        nd.data=i[1]
        nd.left=ns[int(i[2])]
        nd.right=ns[int(i[3])]
    result=""
    inorder(ns[1])
    print(f"#{tc} {result}")
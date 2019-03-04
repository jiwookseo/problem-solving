# 5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree D2
class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right


def preorder(nd):
    global count
    if nd:
        count+=1
        preorder(nd.left)
        preorder(nd.right)


for tc in range(1, int(input())+1):
    i=input().split()
    e,n=int(i[0]),int(i[1])
    ns=[Node(i) for i in range(e+2)]
    edge=list(map(int,input().split()))
    while(len(edge)!=0):
        p=ns[edge.pop(0)]
        c=ns[edge.pop(0)]
        if p.left is None:
            p.left=c
        else:
            p.right=c
    count=0
    preorder(ns[n])
    print("#{} {}".format(tc,count))
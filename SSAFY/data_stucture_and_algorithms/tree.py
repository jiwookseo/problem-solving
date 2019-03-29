class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def preorder(nd):
    if nd:
        print(nd.data,end=" ")
        preorder(nd.left)
        preorder(nd.right)

def inorder(nd):
    if nd:
        inorder(nd.left)
        print(nd.data,end=" ")
        inorder(nd.right)

def postorder(nd):
    if nd:
        postorder(nd.left)
        postorder(nd.right)
        print(nd.data,end=" ")

n=int(input())
ns=[Node(i) for i in range(n+1)]
edge=list(map(int,input().split()))
while(len(edge)!=0):
    p=ns[edge.pop(0)]
    c=ns[edge.pop(0)]
    if p.left==None:
        p.left=c
    else:
        p.right=c
preorder(ns[1])
print("")
inorder(ns[1])
print("")
postorder(ns[1])
print("")
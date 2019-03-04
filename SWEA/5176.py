# 5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색 D2
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inorder(nd):
    global count
    if nd:
        inorder(nd.left)
        count += 1
        result[nd.data]=count
        inorder(nd.right)


for tc in range(1, int(input())+1):
    n = int(input())
    ns = [Node(i) for i in range(n+1)]
    i = 1
    while i < n + 1:
        nd = ns[i]
        nd.left = ns[2*i] if 2*i < n+1 else None
        nd.right = ns[2*i+1] if 2*i < n else None
        i += 1
    result = [None] * (n+1)
    count = 0
    inorder(ns[1])
    print("#{} {} {}".format(tc, result[1], result[n//2]))
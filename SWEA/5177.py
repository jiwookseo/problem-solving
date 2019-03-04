# 5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙 D2
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


for tc in range(1, int(input()) + 1):
    n = int(input())
    ns = [Node(0)]
    ns += [Node(i) for i in map(int, input().split())]
    count = 1
    end = 1
    for i in range(2, n + 1):
        t = i
        while ns[t // 2].data > ns[t].data and t != 1:
            ns[t // 2].data, ns[t].data = ns[t].data, ns[t // 2].data
            t //= 2
    sum = 0
    t = (len(ns) - 1) // 2
    while t >= 1:
        sum += ns[t].data
        t //= 2
    print("#{} {}".format(tc, sum))
# 5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색 D2


def inorder(i):
    global count
    if i in ns:
        inorder(2*i)
        count += 1
        result[i] = count
        inorder(2*i+1)


for tc in range(1, int(input())+1):
    n = int(input())
    ns = list(range(n + 1))
    result = [None] * (n+1)
    count = 0
    inorder(ns[1])
    print("#{} {} {}".format(tc, result[1], result[n // 2]))
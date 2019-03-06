# 5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙 D2
for tc in range(1, int(input()) + 1):
    n = int(input())
    ns = [0]
    ns += list(map(int, input().split()))
    count = 1
    end = 1
    for i in range(2, n + 1):
        t = i
        while ns[t // 2] > ns[t] and t != 1:
            ns[t // 2], ns[t] = ns[t], ns[t // 2]
            t //= 2
    sum = 0
    t = (len(ns) - 1) // 2
    while t >= 1:
        sum += ns[t]
        t //= 2
    print("#{} {}".format(tc, sum))
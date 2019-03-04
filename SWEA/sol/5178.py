# 5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합 D3
for tc in range(1, int(input()) + 1):
    i = input().split()
    n, m, l = int(i[0]), int(i[1]), int(i[2])
    ns = [None] * (n + 1)
    for _ in range(m):
        i = input().split()
        ns[int(i[0])] = int(i[1])
    t = n
    if n % 2 == 0:
        ns[t // 2] = ns[t]
        t -= 1
    while t > 1:
        ns[t // 2] = ns[t] + ns[t - 1]
        t -= 2
    print("#{} {}".format(tc, ns[l]))
# 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리 D4


def dijkstra(s):
    global g, v, n
    u = {s}
    while u != v:
        temp = v - u
        mini = 1000
        w = 0
        for e in temp:
            if mini > g[s][e]:
                mini = g[s][e]
                w = e
        u.add(w)
        for i in range(n):
            if 0 < g[w][i] < 100:
                g[s][i] = min(g[s][i], g[s][w] + g[w][i])


for TC in range(1, int(input()) + 1):
    n, e = map(int, input().split())
    n += 1
    g = [[100000] * n for _ in range(n)]
    v = set(range(n))
    for _ in range(e):
        start, end, w = map(int, input().split())
        g[start][end] = w
    dijkstra(0)
    print("#{} {}".format(TC, g[0][n - 1]))

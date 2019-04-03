# 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리 D4
# Prim algorithm


def prim(start):
    global g, nds, result, v
    q = list(range(v + 1))
    while q:
        u = extract(q)
        for i in range(v + 1):
            if g[u][i] <= 10:
                if i in q and g[u][i] < nds[i]:
                    nds[i] = g[u][i]


def extract(q):
    global g, nds, v
    mini = 11
    extract_result = 0
    for i in q:
        if mini > nds[i]:
            mini = nds[i]
            extract_result = i
    q.remove(extract_result)
    return extract_result


for TC in range(1, int(input()) + 1):
    v, e = map(int, input().split())
    g = [[11] * (v + 1) for _ in range(v + 1)]
    for _ in range(e):
        a, b, w = map(int, input().split())
        g[a][b] = g[b][a] = w
    result = 0
    nds = [11] * (v + 1)
    nds[0] = 0
    prim(0)
    print("#{} {}".format(TC, sum(nds)))

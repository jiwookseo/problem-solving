def check(s, v, count):
    global g, test, result
    for i in g[v]:
        if not visited[i]:
            visited[i] = True
            if visited == test:
                if result[s] > count:
                    result[s] = count
                return
            q.append((s, i, count + 1))


n = int(input())
g = [[] for _ in range(n+1)]
test = [False]+[True]*n
result = [n] * (n+1)
while True:
    i = input().split()
    if i[0] == "-1":
        break
    a, b = int(i[0]), int(i[1])
    g[a].append(b)
    g[b].append(a)
for i in range(1, n+1):
    visited = [False] * (n + 1)
    visited[i] = True
    q = [(i, i, 1)]
    while len(q) != 0:
        check(*q.pop(0))
m = min(result)
rr = []
for i in range(1, n+1):
    if result[i] == m:
        rr.append(str(i))
print(m, len(rr))
print(" ".join(rr))

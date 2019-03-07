def check(v):
    for nd in ns[v]:
        if not visited[nd]:
            visited[nd] = True
            check(nd)


n = int(input())
ns = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
e = int(input())
for _ in range(e):
    i = input().split()
    a, b = int(i[0]), int(i[1])
    ns[a].append(b)
    ns[b].append(a)
visited[1] = True
check(1)
print(sum(visited) - 1)
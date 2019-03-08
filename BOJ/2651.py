def check(a, r):
    global n, m, result, visited
    tx = x = a[-1]
    if x == -1:
        pass
    elif result[x] == -1 or result[x] > r:
        result[x] = r
        if x == m:
            visited = [str(i+1) for i in a[1:-1]]
    else:
        return
    t = 0
    while t <= n:
        tx += 1
        if tx == m+1:
            break
        t += c[tx]
    for i in range(tx-1, x, -1):
        check(a+[i], r+f[i])


n, m = int(input()), int(input())
c, f = list(map(int, input().split())), list(map(int, input().split())) + [0]
result = [-1]*(m+1)
visited = []
check([-1], 0)
print(result[m])
print(len(visited))
print(" ".join(visited))

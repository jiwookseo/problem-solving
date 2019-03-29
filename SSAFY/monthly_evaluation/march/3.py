def dfs(i=0, count=0):
    global result, s, r, n, visited
    if count >= result:
        return
    if i == n:
        result = count
        return
    rx, ry = r[i]
    for j in range(n):
        if not visited[j]:
            visited[j] = True
            sx, sy = s[j]
            dfs(i + 1, count + abs(rx - sx) + abs(ry - sy))
            visited[j] = False
    return


for TC in range(1, int(input()) + 1):
    n = int(input())
    sm = map(int, input().split())
    rm = map(int, input().split())
    s = []
    r = []
    flag = 1
    for i in sm:
        if flag:
            t = i
        else:
            s.append((t, i))
        flag = 1 - flag
    for i in rm:
        if flag:
            t = i
        else:
            r.append((t, i))
        flag = 1 - flag
    visited = [False] * n
    result = 0
    for i in range(n):  # find greedy result
        rx, ry = r[i]
        mini = 300
        ind = 0
        for j in range(n):
            if not visited[j]:
                sx, sy = s[j]
                temp = abs(rx - sx) + abs(ry - sy)
                if temp < mini:
                    mini = temp
                    ind = j
            result += mini
            visited[ind] = True
    visited = [False] * n
    dfs()
    print("#{} {}".format(TC, result))

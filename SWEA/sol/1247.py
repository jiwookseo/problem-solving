# 1247. [S/W 문제해결 응용] 3일차 - 최적 경로 D5
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15OZ4qAPICFAYD
# recursive 보다 stack 이 퍼포먼스가 좋다. Why? copy 보다 재귀 호출이 많은 것이 더 시간을 소요하는 것으로 보임.


def dfs(i, count):
    global result, visited, bp, lc
    if result < count:
        return
    if visited == bp:
        count += v[i][n + 1]
        if result > count:
            result = count
        return
    for j in range(1, n + 1):
        if not visited[j]:
            visited[j] = True
            dfs(j, count + v[i][j])
            visited[j] = False


for TC in range(1, int(input()) + 1):
    n = int(input())
    lm = map(int, input().split())
    lc, flag, temp = [], 1, None
    for i in lm:
        if flag:
            temp = i
        else:
            lc.append((temp, i))
        flag = 1 - flag
    lc.append(lc.pop(1))
    v = [[0] * (n + 2) for _ in range(n + 2)]
    for i in range(n + 1):
        for j in range(i, n + 2):
            x1, y1 = lc[i]
            x2, y2 = lc[j]
            v[i][j] = v[j][i] = abs(x1 - x2) + abs(y1 - y2)
    visited = [True] + [False] * n
    bp = [True] * (n + 1)
    result = 100000
    dfs(0, 0)
    print("#{} {}".format(TC, result))

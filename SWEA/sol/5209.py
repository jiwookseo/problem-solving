# 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용 D3
def dfs(i=0, count=0):
    global result, visited
    if count >= result:
        return
    if i == n:
        result = count
    for j in range(n):
        if not visited[j]:
            visited[j] = True
            dfs(i + 1, count + fact[i][j])
            visited[j] = False


for TC in range(1, int(input()) + 1):
    n = int(input())
    fact = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    result = 0  # greedy result
    for i in range(n):
        mini = 100
        ind = 0
        for j in range(n):
            if not visited[j]:
                if mini > fact[i][j]:
                    mini = fact[i][j]
                    ind = j
            visited[ind] = True
            result += fact[i][ind]
    visited = [False] * n
    dfs()
    print("#{} {}".format(TC, result))

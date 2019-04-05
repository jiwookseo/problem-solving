# 1949. [모의 SW 역량테스트] 등산로 조성
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]


def dfs(r, c, h, dig=False, count=1):
    global result
    check = False
    for i in range(4):
        tr, tc = r + dr[i], c + dc[i]
        if 0 <= tr < n and 0 <= tc < n:
            if not visited[tr][tc]:
                nh = board[tr][tc]
                visited[tr][tc] = True
                if nh < h:
                    check = True
                    dfs(tr, tc, nh, dig, count + 1)
                elif not dig:
                    for j in range(1, k + 1):
                        if nh - j < h:
                            check = True
                            dfs(tr, tc, nh - j, True, count + 1)
                visited[tr][tc] = False
    if not check and result < count:
        result = count
    return


for TC in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    s = []
    maxi = 0
    for r in range(n):
        for c in range(n):
            h = board[r][c]
            if maxi == h:
                s.append((r, c, h))
            elif maxi < h:
                maxi = h
                s = [(r, c, h)]
    result = 0
    visited = [[False] * n for _ in range(n)]
    for r, c, h in s:
        visited[r][c] = True
        dfs(r, c, h)
        visited[r][c] = False
    print("#{} {}".format(TC, result))

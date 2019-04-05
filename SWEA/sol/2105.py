# 2105. [모의 SW 역량테스트] 디저트 카페
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu
dr, dc = [-1, 1, 1, -1], [1, 1, -1, -1]


def dfs(r, c, d=0, x=0, count=1):
    global result
    tr, tc = r + dr[d], c + dc[d]
    if sr == tr and sc == tc:
        if result < count:
            result = count
        return
    if 0 <= tr < n and 0 <= tc < n:
        nd = board[tr][tc]
        if not visited[nd]:  # 중복 X
            visited[nd] = True
            if d == 0:
                dfs(tr, tc, 0, x + 1, count + 1)  # 직진
                dfs(tr, tc, 1, x + 1, count + 1)  # 회전
            elif d == 1:
                dfs(tr, tc, 1, x, count + 1)  # 직진
                dfs(tr, tc, 2, x, count + 1)  # 회전
            elif d == 2:
                if x > 1:
                    dfs(tr, tc, 2, x - 1, count + 1)  # 직진
                else:
                    dfs(tr, tc, 3, 0, count + 1)  # 회전
            else:
                dfs(tr, tc, 3, 0, count + 1)  # 직진
            visited[nd] = False


for TC in range(1, int(input()) + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    result = -1
    visited = [False] * 101
    for r in range(1, n - 1):
        for c in range(n - 2):
            sr, sc = r, c
            visited[board[sr][sc]] = True
            dfs(sr, sc)
            visited[board[sr][sc]] = False
    print("#{} {}".format(TC, result))

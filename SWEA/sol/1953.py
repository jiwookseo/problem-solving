# 1953. [모의 SW 역량테스트] 탈주범 검거
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq&categoryId=AV5PpLlKAQ4DFAUq&categoryType=CODE
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
st = [None, [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
for TC in range(1, int(input()) + 1):
    n, m, r, c, l = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    result = 1
    visited[r][c] = True
    q = [(r, c, 1)]
    front = 0
    while len(q) > front:
        r, c, count = q[front]
        front += 1
        if count == l:
            continue
        tunnel = board[r][c]
        for i in st[tunnel]:
            tr, tc = r + dr[i], c + dc[i]
            if 0 <= tr < n and 0 <= tc < m:
                nxt = board[tr][tc]
                if nxt:
                    if (1 - i) % 4 in st[nxt] and not visited[tr][tc]:
                        visited[tr][tc] = True
                        q.append((tr, tc, count + 1))
                        result += 1
    print("#{} {}".format(TC, result))

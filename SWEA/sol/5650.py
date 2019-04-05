# 5650. [모의 SW 역량테스트] 핀볼 게임
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRF8s6ezEDFAUo
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
block = [None, [1, 3, 0, 2], [3, 0, 1, 2], [2, 0, 3, 1], [1, 2, 3, 0], [1, 0, 3, 2]]
for TC in range(1, int(input()) + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    worm = [[] for _ in range(5)]
    start = []
    for r in range(n):
        for c in range(n):
            if board[r][c] == 0:
                start.append((r, c))
            elif 6 <= board[r][c] <= 10:
                worm[board[r][c] - 6].append((r, c))

    result = 0
    for r, c in start:
        sr, sc = r, c
        for d in range(4):
            score = 0
            r, c = sr, sc
            while True:
                tr, tc = r + dr[d], c + dc[d]
                if tr == sr and tc == sc:
                    break
                if 0 <= tr < n and 0 <= tc < n:
                    what = board[tr][tc]
                    if what == -1:
                        break
                    elif what == 0:
                        r, c = tr, tc
                    elif what < 6:
                        score += 1
                        r, c, d = tr, tc, block[what][d]
                    else:
                        w = worm[what - 6]
                        r, c = w[1] if (tr, tc) == w[0] else w[0]
                else:
                    if r == sr and c == sc:
                        break
                    r, c = tr, tc
                    score += 1
                    d = block[5][d]
            if score > result:
                result = score
    print("#{} {}".format(TC, result))

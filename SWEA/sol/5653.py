# 5653. [모의 SW 역량테스트] 줄기세포배양
# https://www.swexpertacademy.com/main/code/problem/problemSolverCodeDetail.do

# list 이용한 방법
# 86,044 kb
# 2,600 ms
# 1,381


for TC in range(int(input())):
    n, m, k = map(int, input().split())  # n * m 행렬, k 시간
    board = [[None] * (m + 2 * k) for _ in range(n + 2 * k)]
    for r in range(n):
        row = list(map(int, input().split()))
        for c in range(m):
            if row[c]:
                board[r + k][c + k] = (0, row[c])
                # time, health
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    for ct in range(1, k + 1):  # current_time
        for tr in range(k - ct, n + k + ct):
            for tc in range(k - ct, m + k + ct):
                if board[tr][tc]:
                    time, health = board[tr][tc]
                    if 2 * health >= ct - time > health:  # active
                        for i in range(4):
                            nxt = board[tr + dr[i]][tc + dc[i]]
                            if nxt:
                                if nxt[0] == ct and nxt[1] < health:
                                    board[tr + dr[i]][tc +
                                                      dc[i]] = (ct, health)
                            else:
                                board[tr + dr[i]][tc + dc[i]] = (ct, health)
    result = 0
    for row in board:
        for cell in row:
            if cell:
                time, health = cell
                if k - time < health * 2:  # alive
                    result += 1
    print(f"#{TC + 1} {result}")

# 2819. 격자판의 숫자 이어 붙이기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB&categoryId=AV7I5fgqEogDFAXB&categoryType=CODE
# ver.1 BFS / Pass 358 ms
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
for TC in range(1, int(input()) + 1):
    board = [input().split() for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            q = [(i, j, board[i][j], 1)]
            t = 0
            while len(q) > t:
                r, c, s, n = q[t]
                t += 1
                if n == 7:
                    result.add(s)
                    continue
                for k in range(4):
                    tr, tc = r + dr[k], c + dc[k]
                    if 0 <= tr < 4 and 0 <= tc < 4:
                        q.append((tr, tc, s + board[tr][tc], n + 1))
    print("#{} {}".format(TC, len(result)))

# ver.2 DFS / Pass 387 ms
# def dfs(r, c, s, n):
#     global board, dr, dc, result
#     if n == 7:
#         result.add(s)
#         return
#     for k in range(4):
#         tr, tc = r + dr[k], c + dc[k]
#         if 0 <= tr < 4 and 0 <= tc < 4:
#             dfs(tr, tc, s + board[tr][tc], n + 1)
#
#
# dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
# for TC in range(1, int(input()) + 1):
#     board = [input().split() for _ in range(4)]
#     result = set()
#     for i in range(4):
#         for j in range(4):
#             dfs(i, j, board[i][j], 1)
#     print("#{} {}".format(TC, len(result)))

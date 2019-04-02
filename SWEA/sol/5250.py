# 5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용 D3
# BFS, Dijkstra algorithm 변형
# Ver.1 Queue 구현
# Pass
dr, dc = [-1, 0, 0, 1], [0, 1, -1, 0]
for TC in range(1, int(input()) + 1):
    n = int(input())
    nn = n ** 2
    board = [list(map(int, input().split())) for _ in range(n)]
    fuel = [[10000000] * n for _ in range(n)]
    fuel[0][0] = 0
    q = [None] * nn
    q[1] = (0, 0)
    rear = 1
    front = 0
    while rear != front:
        front = (front + 1) % nn
        r, c = q[front]
        q[front] = None
        height = board[r][c]
        for i in range(4):
            tr, tc = r + dr[i], c + dc[i]
            if 0 <= tr < n and 0 <= tc < n:
                f = fuel[r][c] + 1 + max(0, board[tr][tc] - height)
                if f < fuel[tr][tc]:
                    fuel[tr][tc] = f
                    rear = (rear + 1) % nn
                    q[rear] = (tr, tc)
    print("#{} {}".format(TC, fuel[n - 1][n - 1]))

# BFS, Dijkstra algorithm 변형
# Ver.2 list.pop(0) method 사용
# Pass
# dr, dc = [-1, 0, 0, 1], [0, 1, -1, 0]
# for TC in range(1, int(input()) + 1):
#     n = int(input())
#     board = [list(map(int, input().split())) for _ in range(n)]
#     fuel = [[10000000] * n for _ in range(n)]
#     fuel[0][0] = 0
#     q = [(0, 0)]
#     while q:
#         r, c = q.pop(0)
#         height = board[r][c]
#         for i in range(4):
#             tr, tc = r + dr[i], c + dc[i]
#             if 0 <= tr < n and 0 <= tc < n:
#                 f = fuel[r][c] + 1 + max(0, board[tr][tc] - height)
#                 if f < fuel[tr][tc]:
#                     fuel[tr][tc] = f
#                     q.append((tr, tc))
#     print("#{} {}".format(TC, fuel[n - 1][n - 1]))

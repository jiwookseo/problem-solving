# 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합 D3
dr, dc = [0, 1], [1, 0]
for TC in range(1, int(input()) + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    result = None
    stack = [(0, 0, board[0][0])]
    while stack:
        r, c, count = stack.pop()
        if result:
            if count >= result:
                continue
        if r == c == (n - 1):
            result = count
            continue
        for i in range(2):
            tr, tc = r + dr[i], c + dc[i]
            if tr < n and tc < n:
                stack.append((tr, tc, count + board[tr][tc]))
    print("#{} {}".format(TC, result))

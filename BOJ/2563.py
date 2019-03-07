n = int(input())
board = [[0]*101 for _ in range(101)]
for _ in range(n):
    i = input().split()
    x, y = int(i[0]), int(i[1])
    for r in range(x, x + 10):
        for c in range(y, y + 10):
            board[r][c] = 1
print(sum([sum(row) for row in board]))

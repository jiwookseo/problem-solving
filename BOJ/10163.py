board = [[0]*101 for _ in range(101)]
n = int(input())
result = [0] * (n+1)
for tc in range(1, n+1):
    i = list(map(int, input().split()))
    result[tc] = i[2] * i[3]
    for r in range(i[0], i[0] + i[2]):
        for c in range(i[1], i[1] + i[3]):
            if board[r][c] != 0:
                result[board[r][c]] -= 1
            board[r][c] = tc
for i in result[1:]:
    print(i)

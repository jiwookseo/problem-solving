for TC in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    maxi = 0
    for i in range(1, n):
        for j in range(1, m - 1):
            for k in range(j + 1, m):
                count = [0] * 6
                for r in range(i):
                    for c in range(j):
                        count[0] += board[r][c]
                    for c in range(j, k):
                        count[1] += board[r][c]
                    for c in range(k, m):
                        count[2] += board[r][c]
                for r in range(i, n):
                    for c in range(j):
                        count[3] += board[r][c]
                    for c in range(j, k):
                        count[4] += board[r][c]
                    for c in range(k, m):
                        count[5] += board[r][c]
                for a in range(4):
                    for b in range(a + 1, 5):
                        for c in range(b + 1, 6):
                            temp = abs(count[a] - count[b]) + abs(count[b] - count[c]) + abs(count[c] - count[a])
                            if temp > maxi:
                                maxi = temp
    print("#{} {}".format(TC, maxi))

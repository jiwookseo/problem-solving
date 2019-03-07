# 4615. 재미있는 오셀로 게임 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQmA4uK8ygDFAXj&categoryId=AWQmA4uK8ygDFAXj&categoryType=CODE
def check(r, c, s):
    global board
    dr = [0, 0, 1, 1, 1, -1, -1, -1]
    dc = [1, -1, 0, 1, -1, 0, -1, 1]
    board[r][c]=s
    result=[]
    for i in range(8):
        tr = r + dr[i]
        tc = c + dc[i]
        temp = []
        flag = False
        while 1 <= tr <= n and 1 <= tc <= n:
            if board[tr][tc] == 3 - s:
                temp.append((tr, tc))
                tr += dr[i]
                tc += dc[i]
            else:
                if board[tr][tc] == s:
                    flag = True
                break
        if flag:
            result += temp
    for tr, tc in result:
        board[tr][tc] = s


for tc in range(1, int(input())+1):
    i = input().split()
    n, m = int(i[0]), int(i[1])
    board = [[0] * (n + 1) for _ in range(n + 1)]
    t = n // 2
    board[t][t] = board[t + 1][t + 1] = 2
    board[t + 1][t] = board[t][t + 1] = 1
    for _ in range(m):
        r, c, s = tuple(map(int, input().split()))
        check(r, c, s)
    a = b = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if board[i][j] == 1:
                a += 1
            elif board[i][j] == 2:
                b += 1
    print("#{} {} {}".format(tc, a, b))
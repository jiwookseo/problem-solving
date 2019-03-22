dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]


def check(grp, res, s):
    global maximum
    while len(s) != 0:
        vr, vc = s.pop()
        for t in range(4):
            tr, tc = vr + dr[t], vc + dc[t]
            if 0 <= tr < n and 0 <= tc < m:
                if grp[tr][tc] == 0:
                    grp[tr][tc] = 2
                    s.append((tr, tc))
                    res -= 1
    if res > maximum:
        maximum = res


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
result = 0
maximum = 0
vir = []
wall = []
for r in range(n):
    for c in range(m):
        if board[r][c] == 0:
            result += 1
            wall.append((r, c))
        elif board[r][c] == 2:
            vir.append((r, c))
for i in range(result-2):
    for j in range(i + 1, result-1):
        for k in range(j + 1, result):
            temp = [board[l][:] for l in range(n)]
            for l in i, j, k:
                temp[wall[l][0]][wall[l][1]] = 1
            check(temp, result - 3, vir[:])
print(maximum)

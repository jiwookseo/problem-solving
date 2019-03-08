dr = [0, 1, -1, 0]
dc = [1, 0, 0, -1]
def one(r, c):
    global er, ec, s
    for i in range(4):
        tr, tc = r + dr[i], c + dc[i]
        if 0 <= tr < n and 0 <= tc < n:
            if board[tr][tc] == "1":
                if er <= tr and ec <= tc:
                    er, ec = tr, tc
                board[tr][tc] = "0"
                s.append((tr, tc))

n = int(input())
u, v, w, x, y = input().split()
board = [input().split() for _ in range(n)]
check = True
while check:
    check = False
    for r in range(n):
        for c in range(n):
            if board[r][c] == "1":
                # print("\n".join([" ".join(i) for i in board]))
                check = True
                board[r][c] = "0"
                sr = er = r
                sc = ec = c
                break
        if check:
            break
    if check:
        s = [(sr, sc)]
        while len(s) != 0:
            one(*s.pop())
        print(sr, er, sc, ec)
# 아이디어 사물함 종이에
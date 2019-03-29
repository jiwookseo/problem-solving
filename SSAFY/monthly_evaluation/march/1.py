dx = [2, 3, 2, 3, -2, -3, -2, -3]
dy = [3, 2, -3, -2, 3, 2, -3, -2]
for TC in range(1, int(input()) + 1):
    n = int(input())
    x, y, rx, ry = map(int, input().split())
    q = [(x, y, 0)]
    s = set()
    check = False
    while q and not check:
        x, y, count = q.pop(0)
        for i in range(8):
            tx, ty = x + dx[i], y + dy[i]
            if tx == rx and ty == ry:
                count += 1
                check = True
                break
            if 0 <= tx < n and 0 <= ty < n and (tx, ty) not in s:
                q.append((tx, ty, count + 1))
                s.add((tx, ty))
    print("#{} {}".format(TC, count))

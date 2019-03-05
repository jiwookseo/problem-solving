i = input().split()
w, h = int(i[0]), int(i[1])
i = input().split()
x, y = int(i[0]), int(i[1])
t = int(input())
xv = 1
yv = 1
m = dict()
while t > 0:
    if 0 < x < w and 0 < y < h:
        if (x, y, xv, yv) in m:
            tt, tv = m[(x, y, xv, yv)]
            cycle = tt - t
            t %= cycle
            tv = tv if tv < t else t
        else:
            tx = w - x if xv > 0 else x
            ty = h - y if yv > 0 else y
            tv = tx if tx < ty else ty
            tv = tv if tv < t else t
            m[(x, y, xv, yv)] = (t, tv)
        x += xv * tv
        y += yv * tv
        t -= tv
    else:
        if not 0 < x < w:
            xv *= -1
        if not 0 < y < h:
            yv *= -1
        x += xv
        y += yv
        t -= 1
print(x, y)
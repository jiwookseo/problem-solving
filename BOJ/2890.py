# https://www.acmicpc.net/problem/2980
# 도로와 신호등

n, l = map(int, input().split())
ct = 0
cd = 0
for _ in range(n):
    d, r, g = map(int, input().split())
    ct += d - cd
    cd = d
    t = ct % (r + g)
    if t < r:
        ct += r - t
print(ct + l - cd)

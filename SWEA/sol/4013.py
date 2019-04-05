# 4013. [모의 SW 역량테스트] 특이한 자석
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeV9sKkcoDFAVH


def check(t, f, n, d):
    f[n] = d
    if n > 1:
        if not f[n - 1] and t[n - 1]:
            check(t, f, n - 1, -d)
    if n < 4:
        if not f[n + 1] and t[n]:
            check(t, f, n + 1, -d)


def spin(n, d):
    temp = (
        None,
        m[0][r[0]] != m[1][(r[1] + 4) % 8],
        m[1][r[1]] != m[2][(r[2] + 4) % 8],
        m[2][r[2]] != m[3][(r[3] + 4) % 8])
    f = [0] * 5
    check(temp, f, n, d)
    for i in range(1, 5):
        if f[i]:
            r[i - 1] = (r[i - 1] - f[i]) % 8


for TC in range(1, int(input()) + 1):
    k = int(input())
    m = [input().split() for _ in range(4)]
    r = [2, 2, 2, 2]
    for _ in range(k):
        n, d = map(int, input().split())
        spin(n, d)
    result = int("".join([str(m[i][(r[i] - 2) % 8]) for i in range(3, -1, -1)]), 2)
    print("#{} {}".format(TC, result))

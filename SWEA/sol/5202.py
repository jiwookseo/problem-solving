# 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크 D3
for TC in range(1, int(input()) + 1):
    n = int(input())
    work = [tuple(map(int, input().split())) for _ in range(n)]
    work.sort(key=(lambda x: x[1]))
    time = work.pop(0)[1]
    result = 1
    while work:
        s, e = work.pop(0)
        if s < time:
            continue
        time = e
        result += 1
    print("#{} {}".format(TC, result))
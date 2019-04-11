# 5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2 D3
for TC in range(1, int(input()) + 1):
    m = list(map(int, input().split()))
    n = m.pop(0)
    s = [(m[0], 0, 0)]
    result = 1000000
    while s:
        charge, start, count = s.pop()
        if result <= count:
            continue
        for i in range(1, charge + 1):
            if i + start == n - 1:
                result = count
                break
            s.append((m[start + i], start + i, count + 1))
    print("#{} {}".format(TC, result))

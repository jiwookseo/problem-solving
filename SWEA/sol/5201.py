# 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반 D3
for TC in range(1, int(input()) + 1):
    cn = int(input().split()[0])
    cs = list(map(int, input().split()))
    ts = list(map(int, input().split()))
    cs.sort(reverse=True)
    result = 0
    for limit in ts:
        i = 0
        while cs[i] > limit:
            i += 1
            if i == cn:
                break
        if i != cn:
            result += cs.pop(i)
            cn -= 1
    print("#{} {}".format(TC, result))

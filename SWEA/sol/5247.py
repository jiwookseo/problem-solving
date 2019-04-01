# 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산 D4
# pop 을 사용하는 방법은 시간초과, Memoization 등을 사용하는 방법은 메모리초과
# index 로 접근하는 방법, 메모리를 최소한으로 사용하기 위한 가지치기 등으로 퍼포먼스 최적화
for TC in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    tree = {n: (n, 0)}
    q = [tree[n]]
    i = 0
    while True:
        num, depth = q[i]
        result = depth + 1
        cd = []
        if num <= 500000:
            cd += [num * 2, num + 1]
        elif num < 1000000:
            cd += [num + 1]
        if num > 11:
            cd += [num - 1, num - 10]
        elif num > 2:
            cd += [num - 1]
        if m in cd:
            break
        for item in cd:
            if item not in tree:
                nex = (item, result)
                q.append(nex)
                tree[item] = nex
        i += 1
    print("#{} {}".format(TC, result))

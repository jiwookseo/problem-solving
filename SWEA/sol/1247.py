# 1247. [S/W 문제해결 응용] 3일차 - 최적 경로 D5
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15OZ4qAPICFAYD
# recursive 보다 stack 이 퍼포먼스가 좋다. Why? copy 보다 재귀 호출이 많은 것이 더 시간을 소요하는 것으로 보임.


for TC in range(1, int(input()) + 1):
    n = int(input())
    lm = map(int, input().split())
    lc = []
    flag = 1
    x = None
    for i in lm:
        if flag:
            x = i
        else:
            lc.append((x, i))
        flag = 1 - flag
    start = lc.pop(0)
    end = lc.pop(0)
    stack = [(start, [False] * n, 0)]
    bp = [True] * n
    result = None
    while stack:
        (x, y), visited, count = stack.pop()
        if result:
            if result < count:
                continue
        if visited == bp:
            nx, ny = end
            count += abs(nx - x) + abs(ny - y)
            if result:
                if result > count:
                    result = count
            else:
                result = count
            continue
        for i in range(n):
            if not visited[i]:
                nx, ny = lc[i]
                temp = visited[:]
                temp[i] = True
                stack.append(((nx, ny), temp, count + abs(nx - x) + abs(ny - y)))
    print("#{} {}".format(TC, result))

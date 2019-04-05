# 2383. [모의 SW 역량테스트] 점심 식사시간
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5-BEE6AK0DFAVl&categoryId=AV5-BEE6AK0DFAVl&categoryType=CODE


def step(temp):
    global time, count
    time += temp
    for j in range(len(tw)):
        if tw[j] >= temp:
            tw[j] -= temp
        elif tw[j] >= 0:
            if count < 3:
                tw[j] -= temp
                count += 1
                if tw[j] <= st:
                    count -= 1
            else:
                tw[j] = 0
        elif st < tw[j] < 0:
            tw[j] -= temp
            if tw[j] <= st:
                count -= 1


for TC in range(1, int(input()) + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    stair = list()
    person = list()
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                person.append((r, c))
            elif board[r][c] > 1:
                stair.append((r, c, -board[r][c] - 1))
    result = 10000000
    p = len(person)
    g = [[0] * p for _ in range(2)]
    for sn in range(2):
        sr, sc = stair[sn][:2]
        for pn in range(p):
            pr, pc = person[pn]
            g[sn][pn] = abs(pr - sr) + abs(pc - sc)
    for i in range(1 << p):
        w = [[], []]
        for pn in range(p):
            if i & (1 << pn):
                w[1].append(g[1][pn])
            else:
                w[0].append(g[0][pn])
        w[0].sort()
        w[1].sort()
        times = 0
        for sn in range(2):
            tw = w[sn]
            if not tw:
                continue
            st = stair[sn][2]
            time = 0
            count = 0
            i = 0
            while tw[-1] > 0:
                while tw[i] <= 0:
                    i += 1
                step(tw[i])
            while tw[-1] > st:
                step(1)
            times = max(times, time)
            if result <= time:
                break
        if result > times:
            result = times
    print("#{} {}".format(TC, result))

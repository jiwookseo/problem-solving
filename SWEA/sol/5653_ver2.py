# 5653. [모의 SW 역량테스트] 줄기세포배양
# https://www.swexpertacademy.com/main/code/problem/problemSolverCodeDetail.do

# dictionary 이용한 방법
# 185,936 kb
# 3,008 ms
# 1,010

for TC in range(int(input())):
    n, m, k = map(int, input().split())  # n * m 행렬, k 시간
    cell = dict()
    for r in range(n):
        row = list(map(int, input().split()))
        for c in range(m):
            if row[c]:
                cell[(r, c)] = [0, row[c]]
                # time, health

    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    for ct in range(1, k + 1):  # current_time
        for key, value in list(cell.items()):
            r, c = key
            time, health = value
            if 2 * health >= ct - time > health:  # active
                for i in range(4):
                    nxt = (r + dr[i], c + dc[i])
                    if nxt in cell:
                        if cell[nxt][0] == ct:
                            cell[nxt][1] = max(cell[nxt][1], health)
                    else:
                        cell[nxt] = [ct, health]
    result = 0
    for time, health in cell.values():
        if 2 * health > k - time:
            result += 1
    print(f"#{TC + 1} {result}")

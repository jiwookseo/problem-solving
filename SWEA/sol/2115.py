# 2115. [모의 SW 역량테스트] 벌꿀채취
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V4A46AdIDFAWu&categoryId=AV5V4A46AdIDFAWu&categoryType=CODE
for TC in range(1, int(input()) + 1):
    n, m, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    result = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n - m + 1):
            for i in range(1, 1 << m):
                honey = 0
                temp_res = 0
                for j in range(m):
                    temp = board[r][c + j]
                    if i & (1 << j):
                        if honey + temp > h:
                            break
                        honey += temp
                        temp_res += temp ** 2
                if temp_res > result[r][c]:
                    result[r][c] = temp_res
    flatten = []
    for i in range(n):
        for j in range(n):
            flatten.append(result[i][j])
    fl = len(flatten)
    maxi = 0
    for i in range(fl):
        for j in range(i + m, fl):
            temp = flatten[i] + flatten[j]
            if maxi < temp:
                maxi = temp
    print("#{} {}".format(TC, maxi))

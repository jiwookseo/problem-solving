# 2115. [모의 SW 역량테스트] 벌꿀채취
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V4A46AdIDFAWu&categoryId=AV5V4A46AdIDFAWu&categoryType=CODE
for TC in range(1, int(input()) + 1):
    n, m, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    result = [[0] * (n - m + 1) for _ in range(n)]
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
    row_maxi = []
    for row in result:
        maxi = 0  # 한 줄에 한 개 선택
        for i in range(min(n - m + 1, m)):
            temp = sorted(row[i::m], reverse=True)
            if temp[0] > maxi:
                maxi = temp[0]
            if len(temp) > 1:  # 한 줄에 두 개 선택
                two = temp[0] + temp[1]
                if two > answer:
                    answer = two
        row_maxi.append(maxi)
    row_maxi.sort(reverse=True)
    temp = row_maxi[0] + row_maxi[1]
    if temp > answer:
        answer = temp
    print("#{} {}".format(TC, answer))

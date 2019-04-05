# 4014. [모의 SW 역량테스트] 활주로 건설
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeW7FakkUDFAVH


def check(temp):
    global prev, flag, count
    if prev == temp:
        count += 1
        if not flag and count == x:
            count = 0
            flag = 1
    elif prev - temp == 1 and flag:
        prev = temp
        count = 1
        flag = 0
    elif temp - prev == 1 and count >= x:
        prev = temp
        count = 1
    else:
        flag = 0
        return False
    return True


for TC in range(1, int(input()) + 1):
    n, x = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    for i in range(n):
        prev = board[i][0]
        flag = 1
        count = 0
        for c in range(n):
            if not check(board[i][c]):
                break
        result += flag
        prev = board[0][i]
        flag = 1
        count = 0
        for r in range(n):
            if not check(board[r][i]):
                break
        result += flag
    print("#{} {}".format(TC, result))

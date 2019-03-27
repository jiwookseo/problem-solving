# 5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트 D3
def perm(visited, k, count, prev):
    global result
    if result:
        if result <= count:
            return
    if k == n - 1:
        count += board[prev][0]
        if not result:
            result = count
        elif result > count:
            result = count
        return
    for i in range(1, n):
        if not visited[i]:
            temp = visited[:]
            temp[i] = True
            perm(temp, k + 1, count + board[prev][i], i)


for TC in range(1, int(input()) + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    result = None
    a = [False] * n
    perm(a, 0, 0, 0)
    print("#{} {}".format(TC, result))

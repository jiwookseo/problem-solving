# 4008. [모의 SW 역량테스트] 숫자 만들기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeRZV6kBUDFAVH
# ver.1 DFS / Pass 236 ms


def dfs(i, res):
    global n, mini, maxi, oper, num
    if i == n:
        if mini > res:
            mini = res
        if maxi < res:
            maxi = res
    if oper[0]:
        oper[0] -= 1
        dfs(i + 1, res + num[i])
        oper[0] += 1
    if oper[1]:
        oper[1] -= 1
        dfs(i + 1, res - num[i])
        oper[1] += 1
    if oper[2]:
        oper[2] -= 1
        dfs(i + 1, res * num[i])
        oper[2] += 1
    if oper[3]:
        oper[3] -= 1
        dfs(i + 1, int(res / num[i]))
        oper[3] += 1


for TC in range(1, int(input()) + 1):
    n = int(input())
    oper = list(map(int, input().split()))
    num = list(map(int, input().split()))
    mini = 100000000
    maxi = -100000000
    dfs(1, num[0])
    print("#{} {}".format(TC, maxi - mini))

# ver.2 BFS / Pass 545 ms
# for TC in range(1, int(input()) + 1):
#     n = int(input())
#     pl, mi, mu, di = map(int, input().split())
#     num = list(map(int, input().split()))
#     q = [(1, pl, mi, mu, di, num[0])]
#     front = 0
#     mini = 100000000
#     maxi = -100000000
#     while len(q) > front:
#         i, pl, mi, mu, di, res = q[front]
#         front += 1
#         if i == n:
#             if mini > res:
#                 mini = res
#             if maxi < res:
#                 maxi = res
#         if pl:
#             q.append((i + 1, pl - 1, mi, mu, di, res + num[i]))
#         if mi:
#             q.append((i + 1, pl, mi - 1, mu, di, res - num[i]))
#         if mu:
#             q.append((i + 1, pl, mi, mu - 1, di, res * num[i]))
#         if di:
#             q.append((i + 1, pl, mi, mu, di - 1, int(res / num[i])))
#     print("#{} {}".format(TC, maxi - mini))

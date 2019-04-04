# 2112. [모의 SW 역량테스트] 보호 필름
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V1SYKAaUDFAWu&categoryId=AV5V1SYKAaUDFAWu&categoryType=CODE
# DFS, BFS 혼합


def check():
    for c in range(w):
        temp = ''
        for r in range(d):
            if admin[r]:
                temp += admin[r]
            else:
                temp += bar[r][c]
        if temp.count('0' * k):
            continue
        if temp.count('1' * k):
            continue
        return False
    return True


def dfs(ind=0, count=0):
    global maxi, admin, result, complete
    if complete:
        return
    if maxi == count:
        if check():
            result = count
            complete = True
        return
    for i in range(ind, d):
        if not admin[i]:
            admin[i] = '0'
            dfs(i, count + 1)
            admin[i] = '1'
            dfs(i, count + 1)
            admin[i] = ''


for TC in range(1, int(input()) + 1):
    d, w, k = map(int, input().split())
    bar = [input().split() for _ in range(d)]
    result = k
    complete = False
    for maxi_count in range(k):
        admin = [''] * d
        maxi = maxi_count
        dfs()
        if complete:
            break
    print("#{} {}".format(TC, result))

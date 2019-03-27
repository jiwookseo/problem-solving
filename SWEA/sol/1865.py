# 1865. 동철이의 일 분배 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LuHfqDz8DFAXc&categoryId=AV5LuHfqDz8DFAXc&categoryType=CODE
# recursive 형태가 stack 형태보다 퍼포먼스가 40% 이상 좋다.
# Because, stack 형태에 visited array 를 담기 위해서는 copy 를 해주어야 하기 때문에 시간 소모가 크다.


def dfs(i, p):
    global visited, result
    if result >= p:
        return
    if i == n:
        result = p
        return
    for j in range(n):
        if not visited[j]:
            visited[j] = True
            dfs(i + 1, p * pct[i][j])
            visited[j] = False


for TC in range(1, int(input()) + 1):
    n = int(input())
    pct = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(n)]
    visited = [False] * n
    result = 0
    dfs(0, 1)
    print("#{} {:.6f}".format(TC, round(result * 100, 6)))

n, m, v = map(int, input().split())
board = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    board[a][b] = board[b][a] = True
visited = [False] * (n + 1)
stack = [v]
while stack:
    node = stack.pop()
    if not visited[node]:
        print(node, end=" ")
        visited[node] = True
        for i in range(n, 0, -1):
            if board[node][i] and not visited[i]:
                stack.append(i)
print()
visited = [False] * (n + 1)
queue = [v]
while queue:
    node = queue.pop(0)
    if not visited[node]:
        print(node, end=" ")
        visited[node] = True
        for i in range(1, n + 1):
            if board[node][i] and not visited[i]:
                queue.append(i)

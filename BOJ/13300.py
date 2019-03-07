check = [[0, 0] for _ in range(7)]
i = input().split()
k = int(i[1])
for _ in range(int(i[0])):
    i = input().split()
    s, y = int(i[0]), int(i[1])
    check[y][s] += 1
print(sum([check[i][j]//k+1 if check[i][j] % k else check[i][j]//k for i in range(1, 7) for j in range(2)]))

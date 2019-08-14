from sys import stdin
n, m = map(int, stdin.readline().split())
able = [[None] * m for _ in range(n)]
for i in range(n):
    check = 0
    ind = 0
    line = stdin.readline()
    for j in range(m):
        if line[j] == "1":
            if not check:
                ind = j
            check += 1
        elif check:
            for k in range(check):
                able[i][ind + k] = check - k
            check = 0
    if check:
        for k in range(check):
            able[i][ind + k] = check - k
result = 0
for i in range(n):
    for j in range(m):
        if able[i][j]:
            temp = able[i][j]
            while temp > result:
                if i + temp > n:
                    break
                check = True
                for k in range(1, temp):
                    if not able[i + k][j]:
                        check = False
                        break
                    elif able[i + k][j] < temp:
                        check = False
                        break
                if check:
                    result = temp
                    break
                else:
                    temp -= 1
print(result * result)

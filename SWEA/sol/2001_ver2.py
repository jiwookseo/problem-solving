# 2001. 파리 퇴치 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq
# sum 값을 유지하며 한 줄씩 빼주고 더해주고를 반복해 계산을 줄인 방법
# ver1 에 비해 퍼포먼스가 좋다.

for tc in range(1, int(input())+1):
    i = input().split()
    n, m = int(i[0]), int(i[1])
    fly = [list(map(int, input().split())) for _ in range(n)]
    r = 0
    c = 0
    result = t = sum([fly[i][j] for i in range(m) for j in range(m)])
    while True:
        for i in range(r, r + m):
            t -= fly[i][c]
            t += fly[i][c+m]
        if result < t:
            result = t
        c += 1
        if c == n-m:
            c = 0
            r += 1
            if r == n-m+1:
                break
            t = sum([fly[i][j] for i in range(r, r + m) for j in range(m)])
            if result < t:
                result = t
    print("#{} {}".format(tc, result))

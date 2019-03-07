# 2001. 파리 퇴치 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq
# sum 라이브러리를 사용해 매번 계산하는 방법. 코드가 짧다.

for tc in range(1, int(input())+1):
    i = input().split()
    n, m = int(i[0]), int(i[1])
    fly = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    for r in range(n-m+1):
        for c in range(n-m+1):
            t = sum([fly[i][j] for i in range(r, r + m) for j in range(c, c + m)])
            if t > result:
                result = t
    print("#{} {}".format(tc, result))

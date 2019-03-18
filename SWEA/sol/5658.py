# 5658. [모의 SW 역량테스트] 보물상자 비밀번호
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo
for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    c = input()
    result = set()
    m = n // 4
    for _ in range(m):
        for i in range(4):
            result.add(c[i*m:(i+1)*m])
        c = c[1:] + c[0]
    print(f"#{tc} {int(sorted(result, reverse=True)[k - 1],16)}")

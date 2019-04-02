# 5521. 상원이의 생일파티 D5
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWWO3kT6F2oDFAV4&categoryId=AWWO3kT6F2oDFAV4&categoryType=CODE
# ver.1 python set structure 이용 / Pass 333 ms
for TC in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    frd = [set() for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        frd[a].add(b)
        frd[b].add(a)
    if not frd[1]:
        print("#{} 0".format(TC))
        continue
    for i in frd[1].copy():
        frd[1].update(frd[i])
    print("#{} {}".format(TC, len(frd[1]) - 1))

# ver.2 인접 행렬 이용 / Pass 362 ms
# for TC in range(1, int(input()) + 1):
#     n, m = map(int, input().split())
#     frd = [[False] * (n + 1) for _ in range(n + 1)]
#     for _ in range(m):
#         a, b = map(int, input().split())
#         frd[a][b] = frd[b][a] = True
#     result = 0
#     for i in range(1, n + 1):
#         if frd[1][i]:
#             result += 1
#     if result == 0:
#         print("#{} 0".format(TC))
#         continue
#     temp = frd[1][:]
#     for i in range(2, n + 1):
#         if temp[i]:
#             for j in range(2, n + 1):
#                 if frd[i][j] and not frd[1][j]:
#                     frd[1][j] = True
#                     result += 1
#     print("#{} {}".format(TC, result))

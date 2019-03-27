# 1486. 장훈이의 높은 선반 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b7Yf6ABcBBASw&categoryId=AV2b7Yf6ABcBBASw&categoryType=CODE
# binary subset 을 이용하는 방식보다 Stack 을 이용하는 방식이 퍼포먼스가 좋다.
for TC in range(1, int(input()) + 1):
    n, b = map(int, input().split())
    t = list(map(int, input().split()))
    a = [False] * n
    stack = [(a[:], 1, 0)]
    a[0] = True
    stack.append((a, 1, t[0]))
    result = 100000
    while stack:
        flag, i, count = stack.pop()
        if count >= b:
            if result > count:
                result = count
            continue
        if i == n:
            continue
        stack.append((flag[:], i + 1, count))
        flag[i] = True
        stack.append((flag, i + 1, count + t[i]))
    print("#{} {}".format(TC, result-b))

# method : binary subset
# for TC in range(1, int(input()) + 1):
#     n, b = map(int, input().split())
#     t = list(map(int, input().split()))
#     result = 100000
#     for i in range(1 << n):
#         count = 0
#         for j in range(n):
#             if i & (1 << j):
#                 count += t[j]
#             if count >= b:
#                 if result > count:
#                     result = count
#                 break
#     print("#{} {}".format(TC, result - b))

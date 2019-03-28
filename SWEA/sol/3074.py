# 3074. 입국심사 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV_XEokaAEcDFAX7&categoryId=AV_XEokaAEcDFAX7&categoryType=CODE
#######################################################################################################################
# Ver.1
# Binary Search


def bs(s, e):
    global t, n, m
    while e - s != 1:  # s 는 미만 e 는 초과일 때 e 반환
        mt = (s + e) // 2
        count = 0
        for i in range(n):
            count += mt // t[i]
        if count >= m:
            e = mt
        else:
            s = mt
    return e


for TC in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    t = [int(input()) for _ in range(n)]
    print("#{} {}".format(TC, bs(0, m * max(t))))

#######################################################################################################################
# Ver.2 Fail : Time Limit 3/10
# linked list 를 이용한 방식, Static list 를 이용한 최솟값 비교보다 1개의 추가 정답
#
#
# class Desk:
#     def __init__(self, time, link=None):
#         self.count = time
#         self.time = time
#         self.link = link
#
#     def add(self):
#         self.count += self.time
#
#
# for TC in range(1, int(input()) + 1):
#     n, m = map(int, input().split())
#     head = Desk(int(input()))
#     for _ in range(n - 1):
#         time = int(input())
#         nd = Desk(time)
#         if not head.link:
#             if time < head.time:
#                 nd.link = head
#                 head = nd
#             else:
#                 head.link = nd
#         elif time < head.time:
#             nd.link = head
#             head = nd
#         else:
#             p = head
#             while p.link.time < time:
#                 p = p.link
#                 if not p.link:
#                     break
#             if not p.link:
#                 p.link = nd
#             else:
#                 nd.link = p.link
#                 p.link = nd
#     for _ in range(m):
#         head.add()
#         p = head
#         while p.link.count < head.count:
#             p = p.link
#             if not p.link:
#                 break
#         if p == head:
#             pass
#         elif not p.link:
#             p.link, head.link, head = head, p.link, head.link
#         else:
#             temp = head
#             p.link, head.link, head = head, p.link, head.link
#     p = head
#     result = 0
#     while p:
#         if result < p.count - p.time:
#             result = p.count - p.time
#         p = p.link
#     print("#{} {}".format(TC, result))

#######################################################################################################################
# Ver.3 Fail : Time Limit 2/10
# static list 를 이용한 최솟값 비교 방식
#
# for TC in range(1, int(input()) + 1):
#     n, m = map(int, input().split())
#     t = [int(input()) for _ in range(n)]
#     tt = t[:]
#     for _ in range(m):
#         mini = 100000
#         ind = 0
#         check = False
#         for i in range(n):
#             if mini > tt[i]:
#                 mini = tt[i]
#                 ind = i
#         tt[ind] += t[ind]
#     maxi = 0
#     for i in range(n):
#         if maxi < tt[i] - t[i]:
#             maxi = tt[i] - t[i]
#     print("#{} {}".format(TC, maxi))

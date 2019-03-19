# 4366. 정식이의 은행업무 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWMeRLz6kC0DFAXd&categoryId=AWMeRLz6kC0DFAXd&categoryType=CODE
for tc in range(1, int(input()) + 1):
    two = input().rstrip()
    three = input().rstrip()
    s2, s3 = set(), set()
    for i in range(1, len(two)):
        s2.add(int(two[:i] + str(1 - int(two[i])) + two[i + 1:], 2))
    s3.add(int('2' + three[1:] if three[0] == '1' else '1' + three[1:], 3))
    for i in range(1, len(three)):
        t = set('012')
        t.remove(three[i])
        for j in t:
            s3.add(int(three[:i] + j + three[i + 1:], 3))
    print("#{} {}".format(tc, s3.intersection(s2).pop()))
#
# for tc in range(1, int(input()) + 1):
#     two = input()
#     three = input()
#     l2, l3 = len(two), len(three)
#     s2, s3 = [], []
#     for i in range(1, l2):
#         t = '0' if two[i] == '1' else '1'
#         temp = two[:i] + t + two[i + 1:]
#         sum = 0
#         for j in range(l2):
#             sum += int(temp[j]) * (1 << (l2 - j - 1))
#         s2.append(sum)
#     for i in range(l3):
#         t = set('012') if i != 0 else set('12')
#         t.remove(three[i])
#         for j in t:
#             temp = three[:i] + j + three[i + 1:]
#             sum = 0
#             for j in range(l3):
#                 sum += int(temp[j]) * (3 ** (l3 - j - 1))
#             s3.append(sum)
#     for i in s2:
#         for j in s3:
#             if i == j:
#                 print("#{} {}".format(tc, i))
"""
2
10100
221
1010
212
"""

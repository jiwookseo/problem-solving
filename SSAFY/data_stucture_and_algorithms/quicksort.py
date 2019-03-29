# def qs(li):
#     n = len(li)
#     if n <= 1:
#         return li
#     pivot = li[n - 1]
#     left = []
#     right = []
#     for i in li[:n - 1]:
#         if i <= pivot:
#             left.append(i)
#         else:
#             right.append(i)
#     left = qs(left)
#     right = qs(right)
#     return left + [pivot] + right


def qs(li):
    n, p = len(li), len(li)//2 - 1
    if n <= 1:
        return li


print(qs([11, 45, 23, 81, 28, 34]))
print(qs([11, 45, 22, 81, 23, 34, 99, 22, 17, 8]))
print(qs([1, 1, 1, 1, 1, 0, 0, 0, 0, 0]))

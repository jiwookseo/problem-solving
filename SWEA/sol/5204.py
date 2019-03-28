# 5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬 D3
#######################################################################################################################
# Ver.1 Pass
# 아래 Version 들로 아무리 해도 안돼서 Merge Sort 과정 중 병합하는 부분을 sorted method 사용..
# def merge_sort(li):
#     global count, N, M
#     n = len(li)
#     if n == 1:
#         return li
#     m = n // 2
#     left, right = merge_sort(li[:m]), merge_sort(li[m:])
#     if left[-1] > right[-1]:
#         count += 1
#     return sorted(left + right)
#
#
# for TC in range(1, int(input()) + 1):
#     count = 0
#     N = int(input())
#     M = N // 2
#     result = merge_sort(list(map(int, input().split())))[M]
#     print("#{} {} {}".format(TC, result, count))


#######################################################################################################################
# Ver.2 Fail : Time Limit 9/10
# Memory Exceeded 방지 위해 list copy 를 최소한으로 한다. > 메모리는 허용되나 시간이 초과
def merge_sort(a, s, n):
    global count, N, result
    if n <= 1:
        return
    m = n // 2
    i, j = s, s + m
    ie, je = s + m, s + n
    merge_sort(a, i, m)
    merge_sort(a, j, n - m)
    if a[ie - 1] > a[je - 1]:
        count += 1
    if n == N:  # 마지막 병합 때는 N//2 index 원소만 구하여 반환해준다.
        t = 0
        while i < ie and j < je:
            if t == m:
                return a[i] if a[i] <= a[j] else a[j]
            if a[i] <= a[j]:
                i += 1
            else:
                j += 1
            t += 1
        return a[m - j] if i < ie else a[n - i]
    else:
        temp = []
        while i < ie and j < je:
            if a[i] <= a[j]:
                temp.append(a[i])
                i += 1
            else:
                temp.append(a[j])
                j += 1
        temp += a[i:ie] + a[j:je]
        for i in range(n):
            a[s + i] = temp[i]


for TC in range(1, int(input()) + 1):
    count = 0
    N = int(input())
    inp = list(map(int, input().split()))
    result = merge_sort(inp, 0, N)
    print("#{} {} {}".format(TC, result, count))

#######################################################################################################################
# Ver.3 RunTime Error : Memory Exceeded Error 9/10
# Merge Sort + 마지막 병합 때는 N//2 원소만 구한다.
#
#
# def merge_sort(li):
#     global count, N, M
#     n = len(li)
#     if n == 1:
#         return li
#     m = n // 2
#     left, right = merge_sort(li[:m]), merge_sort(li[m:])
#     temp = []
#     i = j = 0
#     while i < m and j < n - m:
#         if left[i] <= right[j]:
#             temp.append(left[i])
#             i += 1
#         else:
#             temp.append(right[j])
#             j += 1
#     if i < m:
#         count += 1
#         temp += left[i:]
#     else:
#         temp += right[j:]
#     return temp
#
#
# for TC in range(1, int(input()) + 1):
#     count = 0
#     N = int(input())
#     M = N // 2
#     inp = list(map(int, input().split()))
#     left, right = merge_sort(inp[:M]), merge_sort(inp[M:])
#     i = j = 0
#     result = None
#     while i < M and j < N - M:
#         if left[i] <= right[j]:
#             i += 1
#             if i + j == M + 1:
#                 result = left[i - 1]
#         else:
#             j += 1
#             if i + j == M + 1:
#                 result = right[j - 1]
#     if i < M:
#         count += 1
#         if not result:
#             result = left[M - j]
#     elif not result:
#         result = right[M - i]
#     print("#{} {} {}".format(TC, result, count))
#
#######################################################################################################################
# Ver.4 RunTime Error : Memory Exceeded Error 9/10
# 일반적인 Merge Sort 구현
#
#
# def merge_sort(li):
#     global count
#     n = len(li)
#     if n == 1:
#         return li
#     m = n // 2
#     left, right = merge_sort(li[:m]), merge_sort(li[m:])
#     temp = []
#     i = j = 0
#     while i < m and j < n - m:
#         if left[i] <= right[j]:
#             temp.append(left[i])
#             i += 1
#         else:
#             temp.append(right[j])
#             j += 1
#     if i < m:
#         count += 1
#         temp += left[i:]
#     else:
#         temp += right[j:]
#     return temp
#
# for TC in range(1, int(input()) + 1):
#     count = 0
#     N = int(input())
#     inp = list(map(int, input().split()))
#     result = merge_sort(inp)[N // 2]
#     print("#{} {} {}".format(TC, result, count))

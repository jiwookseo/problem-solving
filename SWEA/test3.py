import random
from pprint import pprint as pp


def selectsort(array):
    for i in range(len(array) - 1):
        index = i
        for j in range(i + 1, len(array)):
            if array[index] > array[j]:
                index = j
        array[i], array[index] = array[index], array[i]
    return array


def whelk(li, n):
    dc = [1, 0, -1, 0]
    dr = [0, 1, 0, -1]
    r, c = 0, 0
    loop = 0
    result = [[0] * 5 for _ in range(5)]
    turn = False
    for i in li:
        result[r][c] = i
        r += dr[loop % 4]
        c += dc[loop % 4]
        if r == n or c == n or r == -1 or c == -1:
            turn = True
        elif result[r][c] != 0:
            turn = True
        if turn:
            r -= dr[loop % 4]
            c -= dc[loop % 4]
            loop += 1
            r += dr[loop % 4]
            c += dc[loop % 4]
            turn = False
    return result


n = 5
# arr=random.sample(range(1,26), n**2)
# arr=[[arr[r*n+c] for c in range(n)] for r in range(n)]
arr = [[16, 9, 3, 15, 14], [17, 4, 22, 19, 11], [23, 25, 2, 1, 10], [18, 12, 24, 5, 13], [21, 6, 7, 20, 8]]
li = [arr[r][c] for c in range(n) for r in range(n)]
sortedList = selectsort(li)
whelkArray = whelk(sortedList, n)
pp(whelkArray)

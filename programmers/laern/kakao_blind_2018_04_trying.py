# https://programmers.co.kr/learn/courses/30/lessons/42891
# ver.1 정확성 테스트만 모두 통과, 효율성 테스트 모두 실패


def solution(food_times, k):
    n = len(food_times)
    mini = min(food_times)
    food_times = [[i + 1, food_times[i]] for i in range(len(food_times))]
    while k > n * mini:
        k -= mini * n
        check = []
        for i in range(n):
            if food_times[i][1] > mini:
                food_times[i][1] -= mini
            else:
                check.append(i)
        for i in check[::-1]:
            del food_times[i]
            n -= 1
            if n == 0:
                return -1
        mini = min(food_times, key=lambda x: x[1])[1]
    i = 0
    while k:
        while not food_times[i][1]:
            i = (i + 1) % n
        food_times[i][1] -= 1
        k -= 1
        if food_times[i][1] == 0:
            del food_times[i]
            n -= 1
            if n == 0:
                return -1
        else:
            i += 1
        i %= n
    return food_times[i][0]

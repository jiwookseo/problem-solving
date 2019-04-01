# https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3
def solution(prices):
    n = len(prices)
    answer = [1] * (n - 1) + [0]
    for i in range(n - 1):
        j = i
        while j < n - 1:
            j += 1
            if prices[i] > prices[j]:
                break
        answer[i] = j - i
    return answer

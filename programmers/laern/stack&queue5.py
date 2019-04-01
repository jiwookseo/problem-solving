# https://programmers.co.kr/learn/courses/30/lessons/42588
def solution(heights):
    n = len(heights)
    answer = [0] * n
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if heights[j] > heights[i]:
                answer[i] = j + 1
                break
    return answer

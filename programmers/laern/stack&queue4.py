# https://programmers.co.kr/learn/courses/30/lessons/42586
import math


def solution(progresses, speeds):
    n = len(progresses)
    answer = []
    time = [0] * n
    for i in range(n):
        time[i] = math.ceil((100 - progresses[i]) / speeds[i])
    while time:
        t = time.pop(0)
        count = 1
        while time:
            if time[0] <= t:
                time.pop(0)
                count += 1
            else:
                break
        answer.append(count)
    return answer

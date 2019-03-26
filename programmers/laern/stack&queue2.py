# https://programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    answer = 0
    pri = [0 for _ in range(10)]
    for p in priorities:
        pri[p] += 1
    while pri[-1] == 0:
        del pri[-1]
    while True:
        p = priorities.pop(0)
        if p == len(pri) - 1:
            answer += 1
            if location == 0:
                return answer
            pri[p] -= 1
            while pri[-1] == 0:
                del pri[-1]
        else:
            priorities.append(p)
        location -= 1
        location %= len(priorities)


print(solution([2, 1, 3, 2], 2))

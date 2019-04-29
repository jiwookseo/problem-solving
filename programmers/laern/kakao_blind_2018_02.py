# https://programmers.co.kr/learn/courses/30/lessons/42889


def solution(N, stages):
    reach = [0] * N
    reside = [0] * N
    for stage in stages:
        if stage == N + 1:
            reach = [i + 1 for i in reach]
        else:
            for i in range(stage):
                reach[i] += 1
            reside[stage - 1] += 1
    fail = [(i + 1, reside[i] / reach[i] if reach[i] != 0 else 0) for i in range(N)]
    fail.sort(key=lambda x: x[1], reverse=True)
    answer = [i[0] for i in fail]
    return answer


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])

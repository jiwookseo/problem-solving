# https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    pd = dict()
    for item in participant:
        if item in pd:
            pd[item] += 1
        else:
            pd[item] = 1
    for item in completion:
        pd[item] -= 1
    for k, v in pd.items():
        if v != 0:
            ans = k
    return ans


print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
